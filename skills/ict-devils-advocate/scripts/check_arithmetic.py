#!/usr/bin/env python3
"""
check_arithmetic.py — mechanical contradiction finder for a trader's own stated numbers.

This does NOT judge whether an ICT reading of a chart is correct. It only catches the
class of error that is decidable from the numbers alone: a label that disagrees with the
arithmetic behind it, a level that doesn't recompute, an R multiple that isn't what was
claimed. Those objections are valuable precisely because they are not matters of opinion.

Extract whatever numbers the user's analysis actually asserted into a claims JSON and run
this before arguing about interpretation. Omit any block the analysis didn't state — the
checker skips what it isn't given rather than assuming values.

Usage:
    python3 check_arithmetic.py claims.json
    cat claims.json | python3 check_arithmetic.py -
    python3 check_arithmetic.py --schema

Exit codes:
    0  no contradictions found
    1  at least one CONTRADICTION
    2  bad input
"""

import json
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
    "trade": {
        "entry": 21470.0,
        "stop": 21400.0,
        "target": 21800.0,
        "claimed_rr": 4.0,
    },
    "account": {
        "balance": 10000.0,
        "risk_pct": 1.0,
        "value_per_point": 1.0,
        "claimed_position_size": 1.4,
    },
}

# Matches the premium/discount convention used by the extract-screenshot-data validator,
# so the two tools never disagree with each other on the same numbers.
DISCOUNT_MAX = 0.45
PREMIUM_MIN = 0.55

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


def check_dealing_range(claims):
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
    for ratio_str in ("0.5", "0.62", "0.705", "0.79"):
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

    ote_a, ote_b = fib_level(start, end, 0.62), fib_level(start, end, 0.79)
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


def main():
    args = sys.argv[1:]
    if not args or args[0] in ("-h", "--help"):
        print(__doc__)
        return 0
    if args[0] == "--schema":
        print(json.dumps(SCHEMA, indent=2))
        return 0

    try:
        raw = sys.stdin.read() if args[0] == "-" else open(args[0], encoding="utf-8").read()
        claims = json.loads(raw)
    except FileNotFoundError:
        print(f"ERROR: no such file: {args[0]}", file=sys.stderr)
        return 2
    except json.JSONDecodeError as e:
        print(f"ERROR: input is not valid JSON: {e}", file=sys.stderr)
        return 2
    if not isinstance(claims, dict):
        print("ERROR: top level must be a JSON object, not an array or scalar.", file=sys.stderr)
        return 2

    for fn in (check_dealing_range, check_fib, check_fvg, check_trade, check_risk):
        try:
            fn(claims)
        except Exception as e:  # a malformed block shouldn't silently skip the other checks
            add("FLAG", "CHECK-ERROR", f"{fn.__name__} could not run: {e}")

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
    return 1 if n_contra else 0


if __name__ == "__main__":
    sys.exit(main())