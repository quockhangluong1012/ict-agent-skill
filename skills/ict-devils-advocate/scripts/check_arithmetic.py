#!/usr/bin/env python3
"""
check_arithmetic.py — mechanical contradiction finder for a trader's own stated numbers.

This does NOT judge whether an ICT reading of a chart is correct. It only catches the
class of error that is decidable from the numbers alone: a label that disagrees with the
arithmetic behind it, a level that doesn't recompute, an R multiple that isn't what was
claimed, a drawn box that doesn't match the candles it was drawn around, a win rate whose
confidence interval swallows the claim being made from it. Those objections are valuable
precisely because they are not matters of opinion.

Extract whatever numbers the user's analysis actually asserted into a claims JSON and run
this before arguing about interpretation. Omit any block the analysis didn't state — the
checker skips what it isn't given rather than assuming values. It never invents a level,
a swing, or a candle.

Usage:
    python3 check_arithmetic.py claims.json
    python3 check_arithmetic.py claims.json --sensitivity
    cat claims.json | python3 check_arithmetic.py -
    python3 check_arithmetic.py --schema

Options:
    --sensitivity   Report how far each dealing-range boundary would have to move to flip
                    the premium/discount conclusion, and evaluate any alternative boundary
                    pairs supplied in dealing_range.alternatives. This turns "the
                    boundaries were chosen, not derived" from an assertion into a number.

Exit codes:
    0  no contradictions found
    1  at least one CONTRADICTION
    2  bad input
"""

import json
import math
import sys

SCHEMA = {
    "instrument": "NDX",
    "direction": "long | short",
    "_comment": "Every block is optional. Include only what the analysis actually stated.",
    "dealing_range": {
        "high": 21800.0,
        "low": 21100.0,
        "claimed_equilibrium": 21450.0,
        "claimed_state": "premium | discount | equilibrium",
        "_alternatives": "optional; boundary pairs you can actually see on the chart",
        "alternatives": [
            {"label": "next external swing high up", "high": 21980.0, "low": 21100.0}
        ],
    },
    "current_price": 21620.0,
    "impulse_leg": {
        "start": 21100.0,
        "end": 21800.0,
        "claimed_fib": {"0.5": None, "0.62": None, "0.705": None, "0.79": None},
    },
    "fvg": [
        {
            "label": "H1 bullish FVG",
            "high": 21500.0,
            "low": 21440.0,
            "claimed_ce": 21470.0,
        }
    ],
    "annotations": [
        {
            "_comment": "drawn_* is what the user's box says; candle_* is what you measured "
                        "off the three candles. Both required for the drift check.",
            "label": "H1 FVG box",
            "drawn_high": 21640.0,
            "drawn_low": 21600.0,
            "candle_high": 21638.0,
            "candle_low": 21602.0,
        }
    ],
    "dol": {
        "label": "PDH",
        "price": 21800.0,
        "claimed_untaken": True,
        "already_swept": False,
        "sweep_note": "e.g. wick to 21,832 two sessions prior, close 21,741",
    },
    "trade": {
        "entry": 21470.0,
        "stop": 21400.0,
        "target": 21800.0,
        "claimed_rr": 4.0,
        "spread_points": 0.0,
        "slippage_points": 0.0,
    },
    "account": {
        "balance": 10000.0,
        "risk_pct": 1.0,
        "value_per_point": 1.0,
        "claimed_position_size": 1.4,
        "daily_loss_limit_pct": 5.0,
        "max_drawdown_pct": 10.0,
    },
    "backtest": {
        "_comment": "for BACKTEST mode; distinct_* are the real sample size",
        "setups": 20,
        "wins": 12,
        "claimed_win_rate_pct": 60.0,
        "distinct_days": 7,
        "distinct_htf_legs": 4,
        "instruments": ["NDX"],
    },
}

# Matches the premium/discount convention used by the extract-screenshot-data validator
# and by ict-audit's check_facts.py, so the three tools never disagree on the same numbers.
DISCOUNT_MAX = 0.45
PREMIUM_MIN = 0.55
FIB_RATIOS = ("0.5", "0.62", "0.705", "0.79")
OTE_LO, OTE_HI = 0.62, 0.79
Z95 = 1.959964

findings = []


def add(level, code, message):
    findings.append((level, code, message))


def num(x):
    return isinstance(x, (int, float)) and not isinstance(x, bool)


def close(a, b, scale):
    """Tolerant compare: 0.25% of the relevant scale, or 1e-9 if scale is degenerate."""
    tol = max(abs(scale) * 0.0025, 1e-9)
    return abs(a - b) <= tol


def fmt(x):
    if not num(x):
        return str(x)
    return f"{x:,.4f}".rstrip("0").rstrip(".")


def classify_pd(price, low, high):
    if high == low:
        return None, None
    frac = (price - low) / (high - low)
    if frac < DISCOUNT_MAX:
        state = "discount"
    elif frac > PREMIUM_MIN:
        state = "premium"
    else:
        state = "equilibrium"
    return state, frac


def fib_level(start, end, ratio):
    """Retracement level at `ratio` of the leg start->end. Works for both directions."""
    return end - ratio * (end - start)


def wilson(wins, n, z=Z95):
    """Wilson score interval — behaves sanely at the small n this domain actually has."""
    if n <= 0:
        return None, None
    p = wins / n
    denom = 1 + z * z / n
    centre = (p + z * z / (2 * n)) / denom
    half = z / denom * math.sqrt(p * (1 - p) / n + z * z / (4 * n * n))
    return max(0.0, centre - half), min(1.0, centre + half)


def check_dealing_range(claims, sensitivity=False):
    dr = claims.get("dealing_range") or {}
    high, low = dr.get("high"), dr.get("low")
    if not (num(high) and num(low)):
        return
    if high <= low:
        add("CONTRADICTION", "DR-INVERTED",
            f"dealing_range.high ({fmt(high)}) is not above dealing_range.low ({fmt(low)}). "
            "The range as stated is inverted or degenerate, so every premium/discount and "
            "OTE conclusion drawn from it is undefined.")
        return
    span = high - low

    eq = (high + low) / 2.0
    claimed_eq = dr.get("claimed_equilibrium")
    if num(claimed_eq):
        if close(claimed_eq, eq, span):
            add("OK", "DR-EQ", f"equilibrium {fmt(claimed_eq)} matches midpoint {fmt(eq)}.")
        else:
            add("CONTRADICTION", "DR-EQ",
                f"claimed equilibrium {fmt(claimed_eq)} is not the midpoint of the stated range. "
                f"Midpoint of {fmt(low)}–{fmt(high)} is {fmt(eq)} "
                f"(off by {fmt(abs(claimed_eq - eq))}).")

    price = claims.get("current_price")
    if num(price):
        state, frac = classify_pd(price, low, high)
        claimed_state = (dr.get("claimed_state") or "").strip().lower()
        pos = f"price {fmt(price)} sits at {frac * 100:.1f}% of the range {fmt(low)}–{fmt(high)}"
        if claimed_state in ("premium", "discount", "equilibrium"):
            if claimed_state == state:
                add("OK", "PD-STATE", f"{pos} → {state}, which matches the claim.")
            else:
                add("CONTRADICTION", "PD-STATE",
                    f"{pos} → {state}, but the analysis claims {claimed_state}. "
                    "The premium/discount label contradicts the range and price the analysis "
                    "itself stated; either the label is wrong or the boundary swings are.")
        else:
            add("INFO", "PD-STATE", f"{pos} → {state} (no state claimed to compare against).")

        direction = (claims.get("direction") or "").strip().lower()
        if direction == "long" and state == "premium":
            add("FLAG", "SIDE-OF-RANGE",
                "long taken from premium. Not automatically invalid — continuation entries exist — "
                "but the analysis needs to say why it is buying the expensive half of its own range.")
        elif direction == "short" and state == "discount":
            add("FLAG", "SIDE-OF-RANGE",
                "short taken from discount. Same objection in mirror: state the continuation case "
                "explicitly rather than leaving the range argument unaddressed.")

        if sensitivity:
            _boundary_sensitivity(price, low, high, state)

    if sensitivity:
        _alternative_boundaries(claims, dr, low, high)


def _boundary_sensitivity(price, low, high, state):
    """How far does a boundary have to move to change the conclusion?

    Nothing is invented here: this reports the distance to the nearest boundary value that
    would flip the label, which is a property of the numbers the analysis already stated.
    A small distance means the premium/discount conclusion is a choice, not a measurement.
    """
    span = high - low
    targets = [t for t in (DISCOUNT_MAX, PREMIUM_MIN)]
    moves = []
    for t in targets:
        # move the high, holding the low
        new_high = low + (price - low) / t
        if new_high > price:
            moves.append(("high", new_high, new_high - high, t))
        # move the low, holding the high
        if abs(1 - t) > 1e-12:
            new_low = (price - t * high) / (1 - t)
            if new_low < price:
                moves.append(("low", new_low, new_low - low, t))

    if not moves:
        add("INFO", "PD-SENSITIVITY", "no boundary move produces a different label.")
        return

    for which, new_val, delta, t in moves:
        band = "discount" if t == DISCOUNT_MAX else "premium"
        edge = "into" if band != state else "out of"
        pct = abs(delta) / span * 100
        add("INFO", "PD-SENSITIVITY",
            f"moving the {which} from {fmt(low if which == 'low' else high)} to {fmt(new_val)} "
            f"({'+' if delta > 0 else ''}{fmt(delta)}, {pct:.1f}% of the current span) puts price "
            f"exactly on the {band} boundary — i.e. that move takes the read {edge} {band}.")

    nearest = min(moves, key=lambda m: abs(m[2]))
    pct = abs(nearest[2]) / span * 100
    if pct <= 10:
        add("FLAG", "PD-FRAGILE",
            f"the premium/discount conclusion flips on a {pct:.1f}% move of one boundary "
            f"({fmt(abs(nearest[2]))} points on the {nearest[0]}). At that fragility the label is "
            "reporting the boundary choice, not the market. Ask which two swings define the range "
            "and why those two — the answer has to be independent of where it puts price.")


def _alternative_boundaries(claims, dr, low, high):
    alts = dr.get("alternatives") or []
    price = claims.get("current_price")
    claimed_state = (dr.get("claimed_state") or "").strip().lower()
    base_state, _ = classify_pd(price, low, high) if num(price) else (None, None)
    if not alts:
        add("INFO", "PD-ALT",
            "no alternative boundary pairs supplied. If the chart shows an adjacent external swing, "
            "add it to dealing_range.alternatives — a nearby alternative that flips the conclusion "
            "is the strongest available evidence that the boundaries were chosen rather than derived.")
        return
    for i, alt in enumerate(alts):
        label = alt.get("label") or f"alternatives[{i}]"
        a_high, a_low = alt.get("high", high), alt.get("low", low)
        if not (num(a_high) and num(a_low)) or a_high <= a_low:
            add("FLAG", "PD-ALT", f"{label}: unusable boundary pair, skipped.")
            continue
        if not num(price):
            continue
        state, frac = classify_pd(price, a_low, a_high)
        flipped = base_state is not None and state != base_state
        level = "FLAG" if flipped else "INFO"
        add(level, "PD-ALT",
            f"{label} ({fmt(a_low)}–{fmt(a_high)}): price sits at {frac * 100:.1f}% → {state}"
            + (f", which REVERSES the stated {claimed_state or base_state}. The read's side-of-range "
               "argument depends entirely on which of these two swing pairs is the operative range, "
               "and the analysis has not defended that choice."
               if flipped else " — same conclusion as the stated range, so the boundary choice is not "
                               "doing the work here."))


def check_fib(claims):
    leg = claims.get("impulse_leg") or {}
    start, end = leg.get("start"), leg.get("end")
    if not (num(start) and num(end)):
        return
    if start == end:
        add("CONTRADICTION", "LEG-DEGENERATE",
            "impulse_leg start equals end; no retracement levels can be derived from it.")
        return
    span = abs(end - start)
    leg_dir = "bullish" if end > start else "bearish"
    direction = (claims.get("direction") or "").strip().lower()
    if direction in ("long", "short"):
        expected = "bullish" if direction == "long" else "bearish"
        if leg_dir != expected:
            add("FLAG", "LEG-DIRECTION",
                f"stated {direction} but the impulse leg runs {leg_dir} "
                f"({fmt(start)} → {fmt(end)}). OTE measured off a leg pointing the other way "
                "usually means the wrong swing pair was chosen.")

    claimed = (leg.get("claimed_fib") or {})
    for ratio_str in FIB_RATIOS:
        ratio = float(ratio_str)
        computed = fib_level(start, end, ratio)
        c = claimed.get(ratio_str)
        if num(c):
            if close(c, computed, span):
                add("OK", f"FIB-{ratio_str}", f"{ratio_str} level {fmt(c)} recomputes correctly.")
            else:
                add("CONTRADICTION", f"FIB-{ratio_str}",
                    f"claimed {ratio_str} level {fmt(c)} does not recompute from the stated leg "
                    f"{fmt(start)} → {fmt(end)}; the correct value is {fmt(computed)} "
                    f"(off by {fmt(abs(c - computed))}).")
        else:
            add("INFO", f"FIB-{ratio_str}", f"{ratio_str} of the stated leg = {fmt(computed)}.")

    ote_a, ote_b = fib_level(start, end, OTE_LO), fib_level(start, end, OTE_HI)
    lo, hi = min(ote_a, ote_b), max(ote_a, ote_b)
    trade = claims.get("trade") or {}
    entry = trade.get("entry")
    if num(entry):
        pct = (end - entry) / (end - start)
        if lo <= entry <= hi:
            add("OK", "OTE-ENTRY",
                f"entry {fmt(entry)} is inside the OTE band {fmt(lo)}–{fmt(hi)} "
                f"(retracement {pct * 100:.1f}%).")
        else:
            add("FLAG", "OTE-ENTRY",
                f"entry {fmt(entry)} is OUTSIDE the OTE band {fmt(lo)}–{fmt(hi)}; it sits at "
                f"{pct * 100:.1f}% of the leg. If the analysis calls this an OTE entry, that claim "
                "fails on the analysis's own numbers.")


def check_fvg(claims):
    for i, gap in enumerate(claims.get("fvg") or []):
        label = gap.get("label") or f"fvg[{i}]"
        high, low = gap.get("high"), gap.get("low")
        if not (num(high) and num(low)):
            continue
        if high <= low:
            add("CONTRADICTION", "FVG-INVERTED",
                f"{label}: high ({fmt(high)}) is not above low ({fmt(low)}).")
            continue
        span = high - low
        ce = (high + low) / 2.0
        claimed_ce = gap.get("claimed_ce")
        if num(claimed_ce):
            if close(claimed_ce, ce, span):
                add("OK", "FVG-CE", f"{label}: CE {fmt(claimed_ce)} matches midpoint {fmt(ce)}.")
            else:
                add("CONTRADICTION", "FVG-CE",
                    f"{label}: claimed CE {fmt(claimed_ce)} is not the midpoint of "
                    f"{fmt(low)}–{fmt(high)}, which is {fmt(ce)}.")
        else:
            add("INFO", "FVG-CE", f"{label}: CE (midpoint) = {fmt(ce)}.")

        entry = (claims.get("trade") or {}).get("entry")
        if num(entry):
            if low <= entry <= high:
                where = "at CE" if close(entry, ce, span) else (
                    "in the upper half" if entry > ce else "in the lower half")
                add("OK", "FVG-ENTRY",
                    f"{label}: entry {fmt(entry)} is inside the gap, {where} "
                    f"(CE = {fmt(ce)}). If the analysis claims a CE entry, check this line.")
            else:
                add("FLAG", "FVG-ENTRY",
                    f"{label}: entry {fmt(entry)} is OUTSIDE the gap {fmt(low)}–{fmt(high)}. "
                    "An 'entered at the FVG' claim does not hold for this gap.")


def check_annotations(claims):
    """Drawn box versus the candles it was drawn around.

    Every downstream number — CE, OTE band membership, R multiple — is measured off the box
    rather than off the candles, so a box drawn wide is a silent arithmetic error running
    through the whole analysis. Nobody re-measures their own boxes, which is exactly why
    this check lands.
    """
    for i, ann in enumerate(claims.get("annotations") or []):
        label = ann.get("label") or f"annotations[{i}]"
        dh, dl = ann.get("drawn_high"), ann.get("drawn_low")
        ch, cl = ann.get("candle_high"), ann.get("candle_low")
        if not all(num(v) for v in (dh, dl, ch, cl)):
            continue
        if ch <= cl or dh <= dl:
            add("FLAG", "ANN-DEGENERATE", f"{label}: inverted or zero-height box, skipped.")
            continue
        true_span = ch - cl
        d_high, d_low = dh - ch, dl - cl
        drawn_ce, true_ce = (dh + dl) / 2.0, (ch + cl) / 2.0
        if close(dh, ch, true_span) and close(dl, cl, true_span):
            add("OK", "ANN-DRIFT", f"{label}: drawn box matches the candle extremes.")
            continue
        add("CONTRADICTION", "ANN-DRIFT",
            f"{label}: the drawn box is {fmt(dl)}–{fmt(dh)} but the candles give "
            f"{fmt(cl)}–{fmt(ch)} (top off by {fmt(d_high)}, bottom off by {fmt(d_low)}; the box is "
            f"{abs(dh - dl) / true_span * 100:.1f}% of the true height). Claimed CE {fmt(drawn_ce)} "
            f"vs true CE {fmt(true_ce)}. Every level measured off this box inherits the error.")

        entry = (claims.get("trade") or {}).get("entry")
        if num(entry):
            in_drawn, in_true = dl <= entry <= dh, cl <= entry <= ch
            if in_drawn != in_true:
                add("CONTRADICTION", "ANN-ENTRY-FLIP",
                    f"{label}: entry {fmt(entry)} is "
                    f"{'inside the drawn box but OUTSIDE' if in_drawn else 'outside the drawn box but INSIDE'}"
                    " the actual gap. The 'entered at the FVG' claim is decided entirely by the "
                    "drawing error.")


def check_dol(claims):
    dol = claims.get("dol") or {}
    if not dol:
        return
    label = dol.get("label") or "DOL"
    price = dol.get("price")
    swept = bool(dol.get("already_swept"))
    untaken = dol.get("claimed_untaken")
    note = dol.get("sweep_note") or ""
    if swept and untaken:
        add("CONTRADICTION", "DOL-SWEPT",
            f"{label} at {fmt(price)} is asserted as untaken liquidity and also recorded as already "
            f"swept{(' — ' + note) if note else ''}. Both cannot hold. If it was swept, step 8 has no "
            "draw and the reward side of the setup is measured against a level that is no longer a "
            "pool.")
    elif swept:
        add("FLAG", "DOL-SWEPT",
            f"{label} at {fmt(price)} was already swept{(' — ' + note) if note else ''}. The target "
            "is not resting liquidity; say what the draw is instead.")

    target = (claims.get("trade") or {}).get("target")
    if num(price) and num(target) and not close(price, target, max(abs(price), 1.0)):
        add("FLAG", "DOL-TARGET-MISMATCH",
            f"stated target {fmt(target)} is not the stated DOL {fmt(price)}. Two different levels "
            "are in play; the R figure and the narrative are describing different trades.")


def check_trade(claims):
    trade = claims.get("trade") or {}
    entry, stop, target = trade.get("entry"), trade.get("stop"), trade.get("target")
    direction = (claims.get("direction") or "").strip().lower()
    if not (num(entry) and num(stop)):
        return
    if direction not in ("long", "short"):
        add("INFO", "RR", "direction not stated; skipping R computation.")
        return

    risk = (entry - stop) if direction == "long" else (stop - entry)
    if risk <= 0:
        add("CONTRADICTION", "STOP-SIDE",
            f"for a {direction}, stop {fmt(stop)} is on the wrong side of entry {fmt(entry)}. "
            "As stated, the position has no defined risk.")
        return
    add("INFO", "RISK", f"risk per unit = {fmt(risk)} points ({fmt(entry)} → {fmt(stop)}).")

    if num(target):
        reward = (target - entry) if direction == "long" else (entry - target)
        if reward <= 0:
            add("CONTRADICTION", "TARGET-SIDE",
                f"for a {direction}, target {fmt(target)} is on the wrong side of entry "
                f"{fmt(entry)}; the trade as stated cannot profit.")
            return
        rr = reward / risk
        add("INFO", "RR", f"computed R multiple = 1:{rr:.2f} "
                          f"(reward {fmt(reward)} / risk {fmt(risk)}).")
        claimed_rr = trade.get("claimed_rr")
        if num(claimed_rr):
            tol = max(0.15, 0.05 * claimed_rr)
            if abs(rr - claimed_rr) <= tol:
                add("OK", "RR-CLAIM", f"claimed 1:{claimed_rr:g} agrees with computed 1:{rr:.2f}.")
            elif claimed_rr > rr:
                # Overstatement is the failure that matters: the decision was justified
                # against a reward the levels never offered.
                add("CONTRADICTION", "RR-CLAIM",
                    f"claimed R of 1:{claimed_rr:g} overstates what the stated levels give; "
                    f"entry/stop/target compute to 1:{rr:.2f}. The decision was evaluated against "
                    "a reward figure the levels do not support.")
            else:
                add("FLAG", "RR-CLAIM",
                    f"claimed 1:{claimed_rr:g} understates the computed 1:{rr:.2f}. Conservative "
                    "rounding is harmless, but confirm the target used for the claim is the same "
                    "target stated here — a mismatch usually means two different targets are in play.")

        cost = 0.0
        for key in ("spread_points", "slippage_points"):
            v = trade.get(key)
            if num(v) and v > 0:
                cost += v
        if cost > 0:
            rr_net = (reward - cost) / (risk + cost)
            degrade = (rr - rr_net) / rr * 100 if rr else 0.0
            level = "FLAG" if degrade >= 15 else "INFO"
            add(level, "RR-NET",
                f"with {fmt(cost)} points of spread+slippage, the R multiple is 1:{rr_net:.2f} "
                f"rather than 1:{rr:.2f} ({degrade:.0f}% worse). A backtested R assumes fills at "
                "the tick and is an upper bound; if the plan needs the upper bound it has no margin.")


def check_risk(claims):
    acct = claims.get("account") or {}
    balance, risk_pct = acct.get("balance"), acct.get("risk_pct")
    if not (num(balance) and num(risk_pct)):
        return
    risk_amount = balance * risk_pct / 100.0
    add("INFO", "RISK-BUDGET",
        f"{risk_pct:g}% of {fmt(balance)} = {fmt(risk_amount)} at risk per trade.")

    if risk_pct > 1.0:
        add("FLAG", "RISK-PCT",
            f"{risk_pct:g}% per trade. On a small evaluation account the binding constraint is the "
            "daily-loss and overall-drawdown allowance, not the balance — count how many "
            "consecutive losses this survives and whether that number is realistic for a "
            "discretionary sequence.")

    for key, name in (("daily_loss_limit_pct", "daily loss limit"),
                      ("max_drawdown_pct", "overall drawdown allowance")):
        lim = acct.get(key)
        if num(lim) and lim > 0 and risk_pct > 0:
            n = lim / risk_pct
            level = "FLAG" if n < 4 else "INFO"
            add(level, "DD-HEADROOM",
                f"{name} {lim:g}% ÷ {risk_pct:g}% per trade = {n:.1f} losing trades to breach. "
                + ("Discretionary losses cluster, so a run that short is the normal case rather "
                   "than the tail." if n < 4 else "State whether a losing streak of that length is "
                   "inside what the sample has already produced."))

    trade = claims.get("trade") or {}
    entry, stop = trade.get("entry"), trade.get("stop")
    vpp = acct.get("value_per_point")
    direction = (claims.get("direction") or "").strip().lower()
    if num(entry) and num(stop) and num(vpp) and vpp > 0 and direction in ("long", "short"):
        risk_points = (entry - stop) if direction == "long" else (stop - entry)
        if risk_points > 0:
            size = risk_amount / (risk_points * vpp)
            add("INFO", "SIZE", f"implied position size = {fmt(size)} unit(s) "
                                f"({fmt(risk_amount)} / ({fmt(risk_points)} pts × {fmt(vpp)})).")
            claimed_size = acct.get("claimed_position_size")
            if num(claimed_size):
                if close(claimed_size, size, max(size, 1.0)):
                    add("OK", "SIZE-CLAIM", f"claimed size {fmt(claimed_size)} agrees.")
                else:
                    implied_risk = claimed_size * risk_points * vpp
                    add("CONTRADICTION", "SIZE-CLAIM",
                        f"claimed size {fmt(claimed_size)} does not match the stated risk budget. "
                        f"That size risks {fmt(implied_risk)} "
                        f"({implied_risk / balance * 100:.2f}% of balance), not {risk_pct:g}%.")


def check_backtest(claims):
    bt = claims.get("backtest") or {}
    n, wins = bt.get("setups"), bt.get("wins")
    if not (num(n) and num(wins)):
        return
    n, wins = int(n), int(wins)
    if n <= 0 or wins < 0 or wins > n:
        add("CONTRADICTION", "BT-COUNTS",
            f"setups={n}, wins={wins} is not a possible tally.")
        return
    p = wins / n
    lo, hi = wilson(wins, n)
    add("INFO", "BT-RATE",
        f"{wins}/{n} = {p * 100:.1f}%; 95% Wilson interval {lo * 100:.1f}%–{hi * 100:.1f}%.")

    claimed = bt.get("claimed_win_rate_pct")
    if num(claimed) and abs(claimed / 100.0 - p) > 0.005:
        add("CONTRADICTION", "BT-RATE-CLAIM",
            f"claimed win rate {claimed:g}% does not match {wins}/{n} = {p * 100:.1f}%.")

    interval = f"{wins}/{n} = {p * 100:.1f}%, 95% interval {lo * 100:.1f}%–{hi * 100:.1f}%"
    if lo <= 0.5 <= hi:
        add("FLAG", "BT-INTERVAL",
            f"{interval} — the interval contains 50%. This sample is compatible with a coin flip and "
            "with a real edge simultaneously, so it cannot support a conclusion about whether the "
            "edge exists. Any claim resting on the point estimate is a [METHOD] failure regardless "
            "of how carefully each individual setup was read.")
    elif hi - lo > 0.30:
        add("FLAG", "BT-INTERVAL",
            f"{interval} — a span of {(hi - lo) * 100:.0f} percentage points. The point estimate is "
            "far more precise-looking than the sample warrants; quote the interval, not the number.")

    for key, label in (("distinct_days", "distinct days"),
                       ("distinct_htf_legs", "distinct HTF legs")):
        v = bt.get(key)
        if num(v) and v > 0 and v < n:
            eff_lo, eff_hi = wilson(round(p * v), int(v))
            add("FLAG", "BT-INDEPENDENCE",
                f"{n} setups but only {int(v)} {label}. Setups sharing a day or an HTF leg are not "
                f"independent draws, so the effective sample size is nearer {int(v)} than {n}. At "
                f"n={int(v)} the same win rate carries a 95% interval of "
                f"{eff_lo * 100:.1f}%–{eff_hi * 100:.1f}%.")

    instruments = bt.get("instruments")
    if isinstance(instruments, list) and len(instruments) == 1 and n >= 10:
        add("FLAG", "BT-REGIME",
            f"all {n} setups come from {instruments[0]}. One instrument over one period is one "
            "regime; the result may be a fact about that regime rather than about the model.")


def main():
    args = [a for a in sys.argv[1:]]
    if not args or args[0] in ("-h", "--help"):
        print(__doc__)
        return 0
    if args[0] == "--schema":
        print(json.dumps(SCHEMA, indent=2))
        return 0

    sensitivity = "--sensitivity" in args
    positional = [a for a in args if not a.startswith("--")]
    if not positional:
        print("ERROR: no input file given (use '-' for stdin).", file=sys.stderr)
        return 2
    src = positional[0]

    try:
        raw = sys.stdin.read() if src == "-" else open(src, encoding="utf-8").read()
        claims = json.loads(raw)
    except FileNotFoundError:
        print(f"ERROR: no such file: {src}", file=sys.stderr)
        return 2
    except json.JSONDecodeError as e:
        print(f"ERROR: input is not valid JSON: {e}", file=sys.stderr)
        return 2
    if not isinstance(claims, dict):
        print("ERROR: top level must be a JSON object, not an array or scalar.", file=sys.stderr)
        return 2

    checks = [
        lambda c: check_dealing_range(c, sensitivity),
        check_fib,
        check_fvg,
        check_annotations,
        check_dol,
        check_trade,
        check_risk,
        check_backtest,
    ]
    for fn in checks:
        name = getattr(fn, "__name__", "check_dealing_range")
        try:
            fn(claims)
        except Exception as e:  # a malformed block shouldn't silently skip the other checks
            add("FLAG", "CHECK-ERROR", f"{name} could not run: {e}")

    order = {"CONTRADICTION": 0, "FLAG": 1, "OK": 2, "INFO": 3}
    findings.sort(key=lambda f: order.get(f[0], 9))

    instrument = claims.get("instrument") or "(instrument not stated)"
    print(f"=== check_arithmetic: {instrument} ===\n")
    for level, code, message in findings:
        print(f"[{level}] {code}: {message}")

    n_contra = sum(1 for f in findings if f[0] == "CONTRADICTION")
    n_flag = sum(1 for f in findings if f[0] == "FLAG")
    print(f"\n{n_contra} contradiction(s), {n_flag} flag(s), "
          f"{len(findings) - n_contra - n_flag} informational.")
    if n_contra:
        print("Contradictions are [ARITHMETIC] objections: the analysis disagrees with its own "
              "numbers, which is not a matter of interpretation.")
    print("Flags are leads, not findings: each one still needs a [CHART] or [DOCTRINE] argument "
          "before it can be shipped as an objection.")
    return 1 if n_contra else 0


if __name__ == "__main__":
    sys.exit(main())
