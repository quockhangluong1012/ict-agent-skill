#!/usr/bin/env bash
# Regression harness for check_facts.py. Run after any change to the script.
# Asserts the deterministic spine behaves on three fixtures:
#   - flawed:        1 real contradiction (premium vs discount), 1 gap (M5 absent)
#   - clean:         0 contradictions, 0 gaps  (must NOT false-positive)
#   - self-contra:   >=6 checklist<->data contradictions
set -u
cd "$(dirname "$0")/.."
SCRIPT="scripts/check_facts.py"
pass=0; fail=0

count() { python3 "$SCRIPT" "$1" | grep -A0 "$2" | grep -oE '\([0-9]+\)' | head -1 | tr -d '()'; }

check() { # label file "CONTRA_EXPR" "GAP_EXPR"
  local label="$1" file="tests/$2" cexp="$3" gexp="$4"
  local c g; c=$(count "$file" "CONTRADICTIONS in the JSON")
  g=$(count "$file" "EVIDENCE GAPS")
  if eval "[ \$c $cexp ] && [ \$g $gexp ]"; then
    echo "PASS  $label  (contra=$c, gaps=$g)"; pass=$((pass+1))
  else
    echo "FAIL  $label  (contra=$c, gaps=$g)  expected contra $cexp, gaps $gexp"; fail=$((fail+1))
  fi
}

check "flawed_premium_discount"  flawed_premium_discount.json   "-eq 1" "-eq 1"
check "clean_full_setup"         clean_full_setup.json          "-eq 0" "-eq 0"
check "json_self_contradiction"  json_self_contradiction.json   "-ge 6" "-ge 1"

echo "----"
echo "$pass passed, $fail failed"
[ "$fail" -eq 0 ]