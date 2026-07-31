#!/usr/bin/env python3
"""
validate_extraction.py — mechanical self-check for ICT-VISION output.
 
This does NOT judge whether the ICT interpretation is *correct* (that requires
looking at the actual chart). It only catches the class of errors that are
checkable from the JSON alone: structural mistakes and internal arithmetic
contradictions. Run this against your own draft output before returning it.
 
Usage:
    python3 validate_extraction.py path/to/output.json
    cat output.json | python3 validate_extraction.py -
"""
 
import json
import sys
 
REQUIRED_TOP_KEYS = [
    "charts", "htf_context", "market_structure", "liquidity", "pd_arrays",
    "ote", "time_and_price", "smt_divergence", "ict_2022_model_checklist",
    "annotations", "confidence", "raw_observations",
]
 
VALID_TIMEFRAMES = {"D1", "H1", "M5", "unknown"}
 
 
def load(path):
    raw = sys.stdin.read() if path == "-" else open(path, "r", encoding="utf-8").read()
    return json.loads(raw)
 
 
def walk_timeframe_tags(node, path=""):
    """Yield (path, timeframe_value) for every dict that has a 'timeframe' key."""
    if isinstance(node, dict):
        if "timeframe" in node and isinstance(node["timeframe"], str):
            yield (path, node["timeframe"])
        for k, v in node.items():
            yield from walk_timeframe_tags(v, f"{path}.{k}" if path else k)
    elif isinstance(node, list):
        for i, item in enumerate(node):
            yield from walk_timeframe_tags(item, f"{path}[{i}]")
 
 
def classify_pd(price, low, high):
    if high is None or low is None or price is None or high == low:
        return None
    pct = (price - low) / (high - low)
    if pct < 0.45:
        return "discount"
    if pct > 0.55:
        return "premium"
    return "equilibrium"
 
 
def recompute_fib(start, end, ratio):
    return end - ratio * (end - start)
 
 
def main():
    if len(sys.argv) != 2:
        print("Usage: validate_extraction.py <path-to-json>|-")
        sys.exit(2)
 
    errors = []
    warnings = []
    passed = []
 
    try:
        data = load(sys.argv[1])
    except Exception as e:
        print(f"FATAL: could not parse JSON at all: {e}")
        sys.exit(1)
 
    # 1. Must be a single object, not an array.
    if not isinstance(data, dict):
        errors.append(
            f"Top-level output is a {type(data).__name__}, not a JSON object. "
            f"This breaks any downstream script that reads e.g. data.chart_meta or data['charts']. "
            f"Wrap correctly as a single {{...}} object."
        )
    else:
        passed.append("Top-level output is a single JSON object (not an array).")
 
        # 2. Required keys present.
        missing = [k for k in REQUIRED_TOP_KEYS if k not in data]
        if missing:
            errors.append(f"Missing required top-level keys: {missing}")
        else:
            passed.append("All required top-level keys are present.")
 
        # 3. charts[] sanity + collect which timeframes were actually provided.
        charts = data.get("charts", [])
        provided_timeframes = set()
        if not isinstance(charts, list):
            errors.append("'charts' must be a list, one entry per uploaded image.")
        else:
            for i, c in enumerate(charts):
                tf = c.get("timeframe")
                if tf not in VALID_TIMEFRAMES:
                    warnings.append(f"charts[{i}].timeframe = {tf!r} is not one of {VALID_TIMEFRAMES}.")
                elif tf != "unknown":
                    provided_timeframes.add(tf)
            passed.append(f"Timeframes actually provided as images: {sorted(provided_timeframes) or 'none'}")
 
        # 4. No field anywhere may be tagged with a timeframe that wasn't provided.
        phantom_tags = []
        for path, tf in walk_timeframe_tags(data):
            if tf in ("D1", "H1", "M5") and tf not in provided_timeframes:
                phantom_tags.append((path, tf))
        if phantom_tags:
            for path, tf in phantom_tags:
                errors.append(
                    f"{path} is tagged timeframe={tf!r}, but no {tf} image was listed in 'charts'. "
                    f"This is fabricated data for an unseen timeframe — must be removed or set to unknown."
                )
        else:
            passed.append("No field is tagged with a timeframe that wasn't actually provided as an image.")
 
        # 5. If M5 wasn't provided, ote must stay empty/null.
        if "M5" not in provided_timeframes:
            ote = data.get("ote", {})
            ote_touched = (
                ote.get("applicable") not in (False, None)
                or ote.get("impulse_leg", {}).get("start") is not None
                or ote.get("impulse_leg", {}).get("end") is not None
                or ote.get("price_in_ote") not in (False, None)
            )
            if ote_touched:
                errors.append(
                    "No M5 image was provided, but 'ote' has non-null/non-false values. "
                    "Step 6 (Entry/OTE) is normally an M5-timeframe read and should stay null/false "
                    "when M5 wasn't uploaded."
                )
            else:
                passed.append("'ote' correctly left empty since no M5 image was provided.")
 
        # 6. Dealing range equilibrium arithmetic.
        dr = data.get("htf_context", {}).get("dealing_range", {})
        high, low, eq = dr.get("high"), dr.get("low"), dr.get("equilibrium")
        if high is not None and low is not None and eq is not None:
            expected_eq = (high + low) / 2
            if abs(expected_eq - eq) > max(1.0, 0.005 * abs(high - low)):
                errors.append(
                    f"dealing_range.equilibrium={eq} does not match (high+low)/2={expected_eq:.2f}."
                )
            else:
                passed.append("dealing_range.equilibrium is arithmetically consistent with high/low.")
 
            # 7. Premium/discount label vs current_price, if we have one.
            derived_tf = data.get("htf_context", {}).get("derived_from_timeframe")
            current_price = None
            for c in charts if isinstance(charts, list) else []:
                if c.get("timeframe") == derived_tf and c.get("current_price") is not None:
                    current_price = c["current_price"]
                    break
            if current_price is not None:
                stated = data.get("htf_context", {}).get("premium_discount_state")
                computed = classify_pd(current_price, low, high)
                if computed and stated and stated != "unclear" and computed != stated:
                    errors.append(
                        f"premium_discount_state='{stated}' but current_price={current_price} against "
                        f"dealing_range [{low}, {high}] computes to '{computed}'. Self-contradiction — "
                        f"this is the exact class of error the schema was hardened against."
                    )
                elif computed:
                    passed.append(
                        f"premium_discount_state='{stated}' matches computed position ('{computed}')."
                    )
 
        # 8. OTE fib level arithmetic, only if M5 was provided and impulse_leg is filled in.
        ote = data.get("ote", {})
        leg = ote.get("impulse_leg", {})
        start, end = leg.get("start"), leg.get("end")
        if start is not None and end is not None:
            fibs = ote.get("fib_levels", {})
            for ratio_str in ("0.5", "0.62", "0.705", "0.79"):
                given = fibs.get(ratio_str)
                if given is None:
                    continue
                ratio = float(ratio_str)
                expected = recompute_fib(start, end, ratio)
                tolerance = max(1.0, 0.01 * abs(end - start))
                if abs(expected - given) > tolerance:
                    errors.append(
                        f"ote.fib_levels['{ratio_str}']={given} does not match recomputed level "
                        f"{expected:.2f} from impulse_leg start={start}, end={end}. "
                        f"Check retracement direction (this is exactly the inverted-fib bug class)."
                    )
            if not any(fibs.get(r) is None for r in ("0.5", "0.62", "0.705", "0.79")):
                passed.append("ote.fib_levels are arithmetically consistent with impulse_leg.")
 
    print("=" * 60)
    print(f"PASSED  ({len(passed)})")
    for p in passed:
        print(f"  \u2713 {p}")
    print(f"\nWARNINGS ({len(warnings)})")
    for w in warnings:
        print(f"  ! {w}")
    print(f"\nERRORS  ({len(errors)})")
    for e in errors:
        print(f"  \u2717 {e}")
    print("=" * 60)
 
    sys.exit(1 if errors else 0)
 
 
if __name__ == "__main__":
    main()