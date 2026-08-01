#!/usr/bin/env python3
"""
check_facts.py - deterministic evidence spine for ict-audit.

Given an ICT 2022 extraction JSON (output of the extract-screenshot-data /
ICT-VISION skill, matching its schema.json), this prints the facts that can be
established *mechanically* - no chart reading, no ICT judgment. The auditor leans
on this instead of re-deriving arithmetic or eyeballing self-consistency, which
is where an LLM silently goes wrong.

It reports, deterministically:
  - Timeframes present, and which steps become UNEVALUABLE (esp. M5 -> Entry/OTE).
  - Premium/discount/equilibrium of current price vs the stated label.
  - equilibrium == (high+low)/2, FVG CE == (high+low)/2, OTE fib recompute.
  - OTE band membership when price_in_ote is asserted.
  - CHECKLIST <-> DATA contradictions: a checklist flag set true while the block
    it summarizes is empty/false (the JSON contradicting itself).
  - A structure + liquidity snapshot (MSS/BOS body-close, which pools are swept,
    stated bias/killzone) so the auditor attacks with real fields, not vibes.
  - Phantom timeframe tags (data claimed for a timeframe never provided).

Everything under CONTRADICTIONS is ground truth: a prose claim matching one is an
EVIDENCE error. Everything under GAPS is null/absent: a prose claim there is
UNSUPPORTED, not wrong. Keep those two apart.

Usage:  python3 check_facts.py path/to/extraction.json
        cat extraction.json | python3 check_facts.py -

Exit code is always 0 - this is a reporter, not a gate. Robust to missing keys
and minor schema drift; unknown-shaped input degrades to "could not check".
"""

import json
import sys

VALID_TF = {"D1", "H1", "M5", "unknown"}
STEP_TF = {"1 HTF bias / dealing range": "D1", "6 Entry / OTE": "M5"}
UNCLEAR = {"", "unclear", "unknown", None}


def load(path):
    raw = sys.stdin.read() if path == "-" else open(path, encoding="utf-8").read()
    return json.loads(raw)


def g(d, *keys, default=None):
    cur = d
    for k in keys:
        if not isinstance(cur, dict) or k not in cur:
            return default
        cur = cur[k]
    return cur


def classify_pd(price, low, high):
    if None in (price, low, high) or high == low:
        return None
    pct = (price - low) / (high - low)
    if pct < 0.45:
        return "discount"
    if pct > 0.55:
        return "premium"
    return "equilibrium"


def fib(start, end, ratio):
    return end - ratio * (end - start)


def nonempty(x):
    return isinstance(x, list) and len(x) > 0


def walk_tf_tags(node, path=""):
    if isinstance(node, dict):
        if isinstance(node.get("timeframe"), str):
            yield (path or "root", node["timeframe"])
        for k, v in node.items():
            yield from walk_tf_tags(v, f"{path}.{k}" if path else k)
    elif isinstance(node, list):
        for i, item in enumerate(node):
            yield from walk_tf_tags(item, f"{path}[{i}]")


def current_price_for(data, charts, derived_tf):
    if isinstance(charts, list):
        for c in charts:
            if isinstance(c, dict) and c.get("timeframe") == derived_tf and c.get("current_price") is not None:
                return c["current_price"]
        for c in charts:
            if isinstance(c, dict) and c.get("current_price") is not None:
                return c["current_price"]
    return None


def main():
    if len(sys.argv) != 2:
        print("Usage: check_facts.py <path-to-json>|-")
        sys.exit(0)

    facts, contra, gaps, notes = [], [], [], []

    try:
        data = load(sys.argv[1])
    except Exception as e:
        print("DETERMINISTIC FACT CHECK")
        print("could not parse JSON: %s" % e)
        print("Treat the extraction as unavailable; audit the prose on its own logic only.")
        sys.exit(0)

    if not isinstance(data, dict):
        print("DETERMINISTIC FACT CHECK")
        print("top-level JSON is %s, not an object - cannot map facts." % type(data).__name__)
        sys.exit(0)

    charts = data.get("charts", [])
    present = set()
    if isinstance(charts, list):
        for c in charts:
            tf = c.get("timeframe") if isinstance(c, dict) else None
            if tf in VALID_TF and tf != "unknown":
                present.add(tf)
    facts.append("timeframes present: %s" % (sorted(present) or "none stated"))
    for step, tf in STEP_TF.items():
        if tf not in present:
            gaps.append("step %s usually needs %s, absent -> UNEVALUABLE from this JSON" % (step, tf))

    # phantom timeframe tags
    for path, tf in walk_tf_tags(data):
        if tf in ("D1", "H1", "M5") and tf not in present:
            contra.append("%s is tagged timeframe=%r but no %s chart is listed -> any prose relying on it is fabricated." % (path, tf, tf))

    # --- dealing range / premium-discount ---
    high = g(data, "htf_context", "dealing_range", "high")
    low = g(data, "htf_context", "dealing_range", "low")
    eq = g(data, "htf_context", "dealing_range", "equilibrium")
    stated_pd = g(data, "htf_context", "premium_discount_state")
    derived_tf = g(data, "htf_context", "derived_from_timeframe")
    price = current_price_for(data, charts, derived_tf)

    if None not in (high, low) and high != low:
        exp_eq = (high + low) / 2
        facts.append("dealing_range=[%s, %s], equilibrium(computed)=%.6g" % (low, high, exp_eq))
        if eq is not None and abs(exp_eq - eq) > max(1e-9, 0.005 * abs(high - low)):
            contra.append("stated equilibrium=%s != (high+low)/2=%.6g" % (eq, exp_eq))
        if price is not None:
            computed = classify_pd(price, low, high)
            if computed:
                facts.append("current_price=%s -> computed zone=%s (stated: %s)" % (price, computed, stated_pd))
                if stated_pd not in UNCLEAR and computed != stated_pd:
                    contra.append("stated premium_discount_state='%s' but price computes to '%s' -> any bias built on '%s' is on false footing." % (stated_pd, computed, stated_pd))
        else:
            gaps.append("no current_price on HTF chart -> premium/discount UNEVALUABLE; a prose claim of zone here is UNSUPPORTED.")
    else:
        gaps.append("dealing_range high/low incomplete -> PD-array position UNEVALUABLE.")

    # --- OTE arithmetic + band membership ---
    start = g(data, "ote", "impulse_leg", "start")
    end = g(data, "ote", "impulse_leg", "end")
    fibs = g(data, "ote", "fib_levels", default={}) or {}
    price_in_ote = g(data, "ote", "price_in_ote")
    ote_applicable = g(data, "ote", "applicable")
    if None not in (start, end):
        for r in ("0.5", "0.62", "0.705", "0.79"):
            given = fibs.get(r)
            if given is None:
                continue
            exp = fib(start, end, float(r))
            if abs(exp - given) > max(1e-9, 0.01 * abs(end - start)):
                contra.append("ote.fib_levels['%s']=%s != recompute %.6g from leg [%s->%s] (check retrace direction / inverted fib)." % (r, given, exp, start, end))
        facts.append("OTE leg=[%s->%s]; fib levels present: %s" % (start, end, sorted(fibs.keys()) or "none"))
        f62, f79 = fibs.get("0.62"), fibs.get("0.79")
        if price_in_ote is True and None not in (f62, f79) and price is not None:
            lo_b, hi_b = min(f62, f79), max(f62, f79)
            if not (lo_b <= price <= hi_b):
                contra.append("price_in_ote=true but current_price=%s is outside OTE band [%.6g, %.6g]." % (price, lo_b, hi_b))
    else:
        if "M5" in present and ote_applicable:
            gaps.append("ote.applicable but impulse_leg empty -> Entry/OTE (step 6) UNEVALUABLE though M5 present.")

    # --- FVG CE arithmetic ---
    for i, fvg in enumerate(g(data, "pd_arrays", "fvg", default=[]) or []):
        if not isinstance(fvg, dict):
            continue
        fh, fl, ce = fvg.get("high"), fvg.get("low"), fvg.get("consequent_encroachment")
        if None not in (fh, fl) and ce is not None and fh != fl:
            exp_ce = (fh + fl) / 2
            if abs(exp_ce - ce) > max(1e-9, 0.02 * abs(fh - fl)):
                contra.append("pd_arrays.fvg[%d].consequent_encroachment=%s != midpoint %.6g of [%s,%s]." % (i, ce, exp_ce, fl, fh))

    # --- CHECKLIST <-> DATA contradictions (JSON contradicting itself) ---
    ck = data.get("ict_2022_model_checklist", {})
    if isinstance(ck, dict) and ck:
        mss = g(data, "market_structure", "mss", default=[])
        cisd = g(data, "market_structure", "cisd", default=[])
        disp = g(data, "market_structure", "displacement", "present")
        fvgs = g(data, "pd_arrays", "fvg", default=[])
        buyside = g(data, "liquidity", "buyside", default=[]) or []
        sellside = g(data, "liquidity", "sellside", default=[]) or []
        any_swept = any(isinstance(x, dict) and x.get("swept") for x in buyside + sellside)
        kz = g(data, "time_and_price", "killzone")

        def flag(key):
            return ck.get(key) is True

        if flag("mss_or_cisd_confirmed") and not nonempty(mss) and not nonempty(cisd):
            contra.append("checklist mss_or_cisd_confirmed=true but market_structure.mss and cisd are both empty -> JSON self-contradiction.")
        if flag("displacement_present") and disp is False:
            contra.append("checklist displacement_present=true but market_structure.displacement.present=false -> JSON self-contradiction.")
        if flag("fvg_created_by_displacement") and not nonempty(fvgs):
            contra.append("checklist fvg_created_by_displacement=true but pd_arrays.fvg is empty -> JSON self-contradiction.")
        if flag("fvg_created_by_displacement") and disp is False:
            contra.append("checklist fvg_created_by_displacement=true but displacement.present=false -> the FVG cannot be displacement-born.")
        if flag("liquidity_sweep_confirmed") and not any_swept:
            contra.append("checklist liquidity_sweep_confirmed=true but no buyside/sellside pool has swept=true -> JSON self-contradiction.")
        if flag("inside_valid_killzone") and kz in ("outside_killzone", "unknown", "", None):
            contra.append("checklist inside_valid_killzone=true but time_and_price.killzone='%s' -> JSON self-contradiction." % kz)
        if flag("entry_inside_fvg_or_ote") and not nonempty(fvgs) and not (ote_applicable and price_in_ote):
            contra.append("checklist entry_inside_fvg_or_ote=true but no FVG and price_in_ote is not set -> unsupported by the JSON.")
        if flag("htf_pd_array_aligned") and stated_pd in UNCLEAR:
            gaps.append("checklist htf_pd_array_aligned=true but premium_discount_state is '%s' -> alignment UNSUPPORTED." % stated_pd)

        trues = [k for k, v in ck.items() if v is True]
        falses = [k for k, v in ck.items() if v is not True]
        notes.append("checklist TRUE: %s" % (trues or "none"))
        notes.append("checklist not-true: %s" % (falses or "none"))

    # --- structure + liquidity snapshot (ammunition, not verdicts) ---
    mss = g(data, "market_structure", "mss", default=[]) or []
    bos = g(data, "market_structure", "bos", default=[]) or []
    notes.append("market_structure: mss=%d entr%s, bos=%d entr%s" % (len(mss), "y" if len(mss) == 1 else "ies", len(bos), "y" if len(bos) == 1 else "ies"))
    bos_bad = [b for b in bos if isinstance(b, dict) and b.get("confirmed_by_body_close") is False]
    if bos_bad:
        notes.append("bos entries with confirmed_by_body_close=false: %d -> a body-close-confirmed break is NOT established there." % len(bos_bad))
    swept = []
    for side, arr in (("buy", g(data, "liquidity", "buyside", default=[]) or []), ("sell", g(data, "liquidity", "sellside", default=[]) or [])):
        for x in arr:
            if isinstance(x, dict) and x.get("swept"):
                swept.append("%s:%s@%s" % (side, x.get("type", "?"), x.get("price", "?")))
    notes.append("swept pools: %s | htf_bias=%s | killzone=%s" % (swept or "none", g(data, "htf_context", "htf_bias"), g(data, "time_and_price", "killzone")))
    conf = g(data, "confidence", "overall")
    miss = g(data, "confidence", "missing_timeframes", default=[])
    if conf is not None:
        notes.append("confidence.overall=%s | missing_timeframes=%s" % (conf, miss or "none"))

    # --- print ---
    print("=" * 66)
    print("DETERMINISTIC FACT CHECK  (ground truth for the audit)")
    print("=" * 66)
    print("\nFACTS (%d)" % len(facts))
    for f in facts:
        print("  . " + f)
    print("\nCONTRADICTIONS in the JSON itself (%d)  -> hard EVIDENCE errors" % len(contra))
    for c in contra:
        print("  x " + c)
    print("\nEVIDENCE GAPS (%d)  -> claims here are UNSUPPORTED, not necessarily wrong" % len(gaps))
    for gp in gaps:
        print("  ? " + gp)
    print("\nSNAPSHOT / NOTES (%d)" % len(notes))
    for n in notes:
        print("  - " + n)
    print("=" * 66)
    sys.exit(0)


if __name__ == "__main__":
    main()