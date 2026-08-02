#!/usr/bin/env bash
# Regression harness for check_arithmetic.py. Run after any change to the script.
#
# Two things are asserted, and the second matters more than the first:
#   1. the script finds the contradictions the fixture was built to contain
#   2. the clean fixture produces ZERO contradictions
#
# (2) is the load-bearing test. A checker that false-positives on a correct analysis
# is worse than no checker, because the skill ships its output as [ARITHMETIC] — the
# one tier the user is told not to argue with.
set -u
cd "$(dirname "$0")/.."
SCRIPT="scripts/check_arithmetic.py"
pass=0; fail=0

run() { python3 "$SCRIPT" "tests/$1" ${2:-}; }

# number of findings at a given level
count() { run "$1" "${3:-}" | grep -cE "^\[$2\] " || true; }

# does the output contain this code at all?
has() { run "$1" "${3:-}" | grep -qE "^\[[A-Z]+\] $2:"; }

check() { # label file "CONTRA_EXPR" [extra_args]
  local label="$1" file="$2" cexp="$3" extra="${4:-}"
  local c; c=$(count "$file" CONTRADICTION "$extra")
  if eval "[ \$c $cexp ]"; then
    echo "PASS  $label  (contradictions=$c)"; pass=$((pass+1))
  else
    echo "FAIL  $label  (contradictions=$c, expected $cexp)"; fail=$((fail+1))
    run "$file" "$extra" | sed 's/^/        /'
  fi
}

check_code() { # label file code [extra_args]
  local label="$1" file="$2" code="$3" extra="${4:-}"
  if has "$file" "$code" "$extra"; then
    echo "PASS  $label  ($code present)"; pass=$((pass+1))
  else
    echo "FAIL  $label  ($code missing)"; fail=$((fail+1))
  fi
}

check_exit() { # label file expected_code [extra_args]
  local label="$1" file="$2" want="$3" extra="${4:-}"
  run "$file" "$extra" >/dev/null 2>&1; local got=$?
  if [ "$got" -eq "$want" ]; then
    echo "PASS  $label  (exit=$got)"; pass=$((pass+1))
  else
    echo "FAIL  $label  (exit=$got, expected $want)"; fail=$((fail+1))
  fi
}

echo "--- the one that matters: no false positives on a correct analysis ---"
check      "clean_setup                 " clean_setup.json           "-eq 0"
check_exit "clean_setup exit code       " clean_setup.json           0

echo
echo "--- each fixture isolates one failure class ---"
check      "premium_mislabelled         " premium_mislabelled.json   "-ge 1"
check_code "  → PD-STATE                " premium_mislabelled.json   "PD-STATE"
check_code "  → SIDE-OF-RANGE flag      " premium_mislabelled.json   "SIDE-OF-RANGE"
check_exit "  → exit 1                  " premium_mislabelled.json   1

check      "rr_overstated               " rr_overstated.json         "-ge 1"
check_code "  → RR-CLAIM                " rr_overstated.json         "RR-CLAIM"

check      "annotation_drift            " annotation_drift.json      "-ge 1"
check_code "  → ANN-DRIFT               " annotation_drift.json      "ANN-DRIFT"

check      "dol_already_swept           " dol_already_swept.json     "-ge 1"
check_code "  → DOL-SWEPT               " dol_already_swept.json     "DOL-SWEPT"

echo
echo "--- sensitivity: a nearby alternative boundary that reverses the conclusion ---"
check_code "boundary_fragile PD-FRAGILE " boundary_fragile.json      "PD-FRAGILE"  --sensitivity
check_code "boundary_fragile PD-ALT     " boundary_fragile.json      "PD-ALT"      --sensitivity
check      "  → still 0 contradictions  " boundary_fragile.json      "-eq 0"       --sensitivity

echo
echo "--- backtest: interval must swallow the claim being made from it ---"
check_code "thin_backtest BT-INTERVAL   " thin_backtest.json         "BT-INTERVAL"
check_code "thin_backtest BT-INDEPENDENCE" thin_backtest.json        "BT-INDEPENDENCE"
check      "thin_backtest counts sane   " thin_backtest.json         "-eq 0"

echo
echo "--- input handling ---"
check_exit "malformed json → exit 2     " malformed.json             2
if python3 "$SCRIPT" --schema | python3 -c 'import json,sys; json.load(sys.stdin)' 2>/dev/null; then
  echo "PASS  --schema emits valid JSON"; pass=$((pass+1))
else
  echo "FAIL  --schema emits valid JSON"; fail=$((fail+1))
fi

echo "----"
echo "$pass passed, $fail failed"
[ "$fail" -eq 0 ]
