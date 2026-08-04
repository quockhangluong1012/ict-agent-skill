# Rebuttal playbook — where ICT/SMC analyses actually break

## How to read this file

Do not load all of it. It is a checklist against omission, not a menu to fill — an objection is worth
making because you found it on the chart, never because it appears here.

The file is organised by **attack layer**, deepest first, because that is the order the attack should be
run in. Layer 3 findings change what is worth saying about layers 2 and 1; the reverse is not true.

| Layer | Question | Part | Tier it usually produces |
|---|---|---|---|
| 3 — procedure | Would this process have produced a different answer on a different chart? | **Part 0** | `[METHOD]` |
| 2 — inference | Granting the claims, do they support the conclusion? | **Part 2** | `[METHOD]`, `[HINDSIGHT]` |
| 1 — claims | Does each stated fact hold against the chart? | **Part 1** | `[CHART]`, `[DOCTRINE]`, `[ARITHMETIC]` |

- **Always read Part 0 and Part 2** — they are short, they are the deep layers, and they catch what is
  structurally invisible from a step-by-step review. Then **Part 3** (this user's recurring errors).
- **Read the Part 1 sections for the steps actually in play.** If the analysis makes no OTE claim, skip
  step 6.
- **Read Part 0.8 whenever the input is a batch of setups** — in `BACKTEST` mode it is the main event and
  the per-step material is secondary.
- **Read Part 4** before writing the opposite case, **Part 5** if numbers or risk are stated, and
  **Part 6 always, before shipping** — it is the filter that decides what survives into the output.

`[DOCTRINE]` maps to the **Standard** paragraph of each Part 1 section below — cite that paragraph
directly. It is this skill's own citable standard; no external file is needed.

## Contents

- [How to read the Part 1 entries](#how-to-read-the-part-1-entries)
- [Part 0 — Attacks on the procedure](#part-0--attacks-on-the-procedure)
  - [0.1 The counterfactual chart test](#01-the-counterfactual-chart-test)
  - [0.2 Free-parameter audit](#02-free-parameter-audit)
  - [0.3 Order of discovery](#03-order-of-discovery)
  - [0.4 Rule provenance, and the user's own checklist](#04-rule-provenance-and-the-users-own-checklist)
  - [0.5 The symmetry test](#05-the-symmetry-test)
  - [0.6 The unmentioned alternative](#06-the-unmentioned-alternative)
  - [0.7 Confidence–evidence mismatch](#07-confidenceevidence-mismatch)
  - [0.8 Cross-setup battery — BACKTEST mode](#08-cross-setup-battery--backtest-mode)
- [Part 1 — Attack vectors by model step](#part-1--attack-vectors-by-model-step)
  - [Step 1 — HTF PD array / bias](#step-1--htf-pd-array--bias)
  - [Step 2 — Liquidity run](#step-2--liquidity-run)
  - [Step 3 — Displacement](#step-3--displacement)
  - [Step 4 — FVG created](#step-4--fvg-created)
  - [Step 5 — MSS / CISD](#step-5--mss--cisd)
  - [Step 6 — Entry (FVG / CE / OTE)](#step-6--entry-fvg--ce--ote)
  - [Step 7 — Time / killzone](#step-7--time--killzone)
  - [Step 8 — Target / DOL](#step-8--target--dol)
- [Part 2 — Cross-cutting epistemic failures](#part-2--cross-cutting-epistemic-failures)
- [Part 3 — This user's documented recurring errors](#part-3--this-users-documented-recurring-errors)
- [Part 4 — Inversion toolkit](#part-4--inversion-toolkit)
- [Part 5 — Risk and prop-firm rule attacks](#part-5--risk-and-prop-firm-rule-attacks)
- [Part 6 — The objection filter](#part-6--the-objection-filter)
  - [The three tests](#the-three-tests)
  - [Objections that fail the filter by construction](#objections-that-fail-the-filter-by-construction)
  - [The one thing worth over-reporting](#the-one-thing-worth-over-reporting)

---

## How to read the Part 1 entries

Each Part 1 step gives five things: the **standard** the claim has to meet, the **attack vectors**
ranked roughly by how often they land, the **self-deception** that usually produces the error, the
**forcing question**, and **what discharges** the objection. The discharge condition is not optional —
an objection the user cannot possibly answer is a rhetorical move, not an argument.

The standards here are ICT/SMC's own definitions, stated once and citable directly, which makes them
fair `[DOCTRINE]` ammunition. The chart-specific facts are not here and never will be; those you must
read off whatever the user actually gave you — screenshots, prose, or a structured facts file.

These eight steps are the common shape a directional ICT/SMC read takes, not a mandatory checklist.
Read the sections for the steps the user's own analysis actually makes claims about; skip the rest. An
analysis that only argues bias and entry, with no explicit killzone or DOL claim, gets attacked on bias
and entry — inventing a killzone objection because step 7 exists in this file is manufactured
contrarianism, not rigor.

---

## Part 0 — Attacks on the procedure

Part 1 asks whether each claim is true. Part 2 asks whether the claims support the conclusion. Part 0
asks a question neither of them can reach: **would this procedure have produced a different answer on a
different chart?** If not, then every individual claim can be perfectly correct and the analysis still
carries no information — the steps were narration attached to a conclusion that was never at risk.

This is the deepest layer available and the one a step-by-step review structurally cannot see, because
each step examined alone always looks like it is doing work. It is also the layer where overreach is
easiest, so the rule is unusually strict here: **a Part 0 objection ships only with a named,
chart-specific instance.** "Your process is unfalsifiable" asserted in the abstract is contrarianism.
"Your process is unfalsifiable, and here is the specific condition it lacks" is a `fatal` finding.

Every objection in this part is `[METHOD]` unless it can be pinned to something visible, in which case
prefer the harder tier — an unmentioned competing FVG you can point at is `[CHART]`, not `[METHOD]`.

### 0.1 The counterfactual chart test

**The probe.** What is the smallest change to this chart that would have made the analysis say *no
trade*? Name the candle and the price.

**Why it is the first thing to run.** An analysis that survives every possible chart is not an analysis.
The ICT 2022 Model is a *filter* — its whole value is the setups it rejects — so a read with no rejection
condition has used the model's vocabulary while discarding its function. And this failure is invisible
step by step: each of the eight steps can be individually defensible while the conjunction rejects
nothing.

**How to run it concretely.** Take the analysis's own supporting factors one at a time and ask what value
each would have had to take to flip the conclusion. If the sweep had been two ticks shallower — still no
trade? If the displacement bodies had been half the size? If the setup had fallen twenty minutes later,
outside the killzone? Where the honest answer is "the read would have been the same", that factor was not
a criterion, it was decoration, and it should not be counted as support in section 2.

**The three shapes this failure takes.**

1. **No stated invalidation.** The analysis says what it expects but not what would refute it.
2. **Invalidation that cannot be observed before the outcome.** "I'd be wrong if it went to my stop" is
   the outcome, not a condition — it can only be evaluated after the question is already settled.
3. **Elastic criteria.** Every factor is qualitative enough to be satisfied at any value it took.
   Displacement "energetic", MSS "significant", FVG "clean" — with no threshold, none of them can fail.

**Forcing question.** "Name the candle and price that would have made you skip this. If you cannot, tell
me which of your eight steps could have come out no on this chart."

**Discharged by.** A pre-registered condition, decidable at the hard right edge, that the chart could
plausibly have violated — ideally timestamped before the entry.

**Severity.** `fatal` in `LIVE` mode, where it is the single most valuable thing this skill can produce.
`material` in `REVIEW`, where a missing invalidation is diagnosis rather than a live problem — unless the
analysis is being used to justify repeating the process, which it usually is.

---

### 0.2 Free-parameter audit

**The probe.** Count the choices the read made *on* the chart rather than *before* it.

An ICT 2022 read consumes roughly nine degrees of freedom:

| # | Free parameter | Fixed in advance by a written rule? |
|---|---|---|
| 1 | Which timeframe carries the bias | |
| 2 | Which two swings bound the dealing range | |
| 3 | Which pool counts as the liquidity taken | |
| 4 | Which leg counts as displacement | |
| 5 | Which of the arrays at the entry is *the* POI | |
| 6 | Which swing counts as structurally significant for the MSS | |
| 7 | Which leg the OTE is measured from | |
| 8 | Which pool is the DOL | |
| 9 | Which clock, and therefore which killzone | |

**The argument.** A parameter fixed by a written rule before the chart is a *constraint* — it can conflict
with the chart, so it carries information. A parameter chosen while looking at the chart is a *fitted*
parameter — it cannot conflict with anything, because it was selected to fit. A read with eight fitted
parameters and one observation is a curve fit with a sample size of one, and its coherence is guaranteed
rather than evidential.

This reframes several Part 1 attacks as instances of one failure. "The dealing range boundaries were
chosen, not derived" is parameter 2 fitted. "Retrospective swing selection" is parameter 6 fitted. "POI
shopping" is parameter 5 fitted. Naming the pattern is worth more than listing the instances, because the
fix is one rule-writing exercise rather than six corrections.

**How to state it.** Fill the table for the analysis in front of you and report the ratio: *"7 of 9
parameters were selected on the chart. Two were rule-fixed: the HTF→LTF timeframe ordering this analysis
itself declares, and the body-close requirement for MSS — and the second was then not applied (O4)."*
The number is the objection; the table is the evidence.

**Discharged by.** Written rules, predating this chart, that fix the parameters — plus evidence they were
applied here rather than merely owned. A checklist that exists but was not followed is a worse finding
than no checklist, not a better one; see 0.4.

**Watch for the mirror failure.** Not every fitted parameter is illegitimate — discretion is the point of
a discretionary model, and demanding nine mechanical rules would be demanding a different strategy. The
objection is not "you used judgment". It is "you used judgment at nine points and then reported the
result with the confidence of a mechanical system", or "you used judgment at the one point where you *do*
have a written rule". Keep it to that.

---

### 0.3 Order of discovery

**The probe.** In what order were the conclusions actually reached, and does the writeup's order match?

Analyses are written deductively — bias, then range, then sweep, then entry — and generated abductively:
a direction is felt, and the supporting structure is assembled backwards from it. When those two orders
differ, the writeup is a reconstruction, and every "therefore" in it is load-bearing for nothing.

**Tells, all observable in the text.**

- The bias is stated before the range that supposedly produced it, with the range introduced as
  confirmation rather than as premise.
- Boundary swings are unusual, and unusual in exactly the direction that makes the setup work. Run
  `check_arithmetic.py --sensitivity` to show how far the alternative boundary was and what it does to the
  premium/discount conclusion — an alternative that is both nearby and conclusion-flipping is strong
  evidence the choice was doing work.
- Every factor mentioned supports the conclusion. Real chart reading produces mixed evidence; a writeup
  with a 100% support rate has been filtered, and the filter is the finding.
- The target is stated with more precision than the entry logic justifies, which usually means the R
  figure was needed first.

**Forcing question.** "What did you look at first on this chart, and what was your read before you drew
the dealing range?"

**Discharged by.** A pre-trade note, timestamped, showing the same order as the writeup. Absent that, the
honest tier is `[UNSUPPORTED]` rather than `[METHOD]` — you are alleging a process you cannot observe, and
the discipline that makes this skill worth anything requires saying so.

---

### 0.4 Rule provenance, and the user's own checklist

**The probe.** For each rule the analysis invokes, where is it written down?

This yields two attacks that are stronger than anything in Part 1, because they need no doctrinal
argument at all — the standard is the user's own.

1. **Rules invented for this chart.** A standard that appears in this analysis and nowhere in the user's
   written process was probably reverse-engineered from what the chart offered. Ask which document it is
   in.
2. **Written rules that were skipped here.** If the user's checklist requires a body close for MSS and
   this analysis accepts a wick, the objection is not `[DOCTRINE]`, it is `[SELF-CONTRADICTION]` against
   their own process — and it is far harder to argue with, because it does not depend on agreeing about
   what ICT meant. This is the highest-yield attack available whenever a written checklist exists, and it
   is routinely missed because the checklist is not in front of you unless you ask.

**Ask for the checklist once, early, if it is not supplied.** One line: *"Bạn có file checklist/rule đã
viết trước không? Nếu có, phần lớn phản biện mạnh nhất sẽ đến từ chỗ phân tích này lệch khỏi rule của
chính bạn, chứ không phải từ doctrine."*

**Discharged by.** The written rule, plus its application here.

---

### 0.5 The symmetry test

**The probe.** Would the same procedure, applied to the same chart with the bias inverted, have produced
an equally confident opposite read?

Run it mechanically: take each factor the analysis cites as support, and ask whether an equivalent factor
exists in the opposite direction on the same chart. An FVG below and an FVG above. A pool above and a pool
below. A killzone that is equally a killzone for a short. Where the supporting factors are symmetric, they
are not evidence for the direction — they are evidence that PD arrays exist, which was never in dispute.

**This is only shippable as an objection when you can point at the mirror factor.** "There is presumably
an opposing array" is speculation. "You cite the H1 FVG at 21,602–21,638 as support; the same chart shows
an unmitigated H1 FVG at 21,710–21,744 on the other side, which the analysis does not mention" is
`[CHART]` and it is devastating. Without a nameable mirror factor, the symmetry test is a question for the
user, not an objection — put it in `Hypotheses to check`.

**Discharged by.** An asymmetry: a factor that exists on one side and demonstrably not the other.

---

### 0.6 The unmentioned alternative

**The probe.** What is equally visible on the supplied charts and absent from the writeup?

Silence is the most reliable tell of confirmation-driven reading, and unlike most Part 0 material it is
directly evidenced: the fact is on the screenshot the user chose to send. Scan for the competing array,
the untaken pool on the wrong side, the higher-timeframe candle that disagrees, the prior sweep that
already consumed the target.

The worked example's O3 is exactly this shape — a wick on the user's own D1 screenshot that their
narrative walked past — and it is one of the two objections that break the thesis there.

**Distinguish two cases, because they warrant different severity.** The user *considered and rejected* the
alternative but did not write it down (documentation gap, `minor`); or the user did not see it (the read
was not a survey of the chart, it was a search for a setup — `material` at least, and it undermines the
`[CHART]` support elsewhere in the analysis).

**Forcing question.** "Bạn có thấy X trước khi vào lệnh không? Nếu có thì vì sao loại; nếu không thì phần
đọc chart này chưa phải là đọc toàn bộ chart."

**Discharged by.** An account of the alternative and a reason it was rejected.

---

### 0.7 Confidence–evidence mismatch

**The probe.** Compare the certainty of the language to the tier of the evidence underneath it.

"MSS confirmed", "clearly bullish", "chắc chắn", "definitely" attached to a claim that is one reading among
several is a calibration failure, and calibration is the thing a backtesting phase exists to build. This
is a small objection about any single sentence and a `material` one about the analysis as a whole: a
writeup with no hedges anywhere has either found unusually clean evidence or is not tracking its own
uncertainty, and the evidence base usually tells you which.

Report it as a count rather than a complaint: *"Bốn claim dùng ngôn ngữ chắc chắn ('confirmed',
'clearly'); theo evidence base thì hai trong số đó là `[UNSUPPORTED]`."* A count is checkable; "you sound
overconfident" is not.

**Discharged by.** Nothing to discharge — this one is retracted by restating the claims at the confidence
the evidence supports, which is also the fix.

---

### 0.8 Cross-setup battery — BACKTEST mode

When the input is several setups, the strongest objections are almost never inside any one of them. They
live in the relationships between setups, they are invisible from a per-setup review, and nobody finds
them by accident. **Run this battery before attacking any individual setup, and lead the output with what
it finds.**

1. **Rule drift.** Tabulate one row per setup and one column per free parameter from 0.2 — how the dealing
   range was bounded, what the MSS standard was, whether entry was CE or proximal edge, whether killzone
   was required. Any column that is not constant is a rule that changed mid-sample. This is the single
   highest-yield backtest objection: a strategy whose rules varied across the sample was not tested, and
   its aggregate win rate measures nothing, because no fixed procedure produced it.
2. **Selection provenance.** How were these setups found? Scrolling back until something that looks like a
   setup appears is search-then-label, not sampling — the criteria are being applied to a population that
   was already filtered by resemblance to a good setup. The clean method is to fix a date range in advance
   and take every instance.
3. **Survivorship.** How many setups met the criteria and were *not* logged? If the answer is unknown, the
   win rate is `[UNSUPPORTED]` and no amount of per-setup rigour repairs it.
4. **Outcome-conditioned labelling.** Compare the "valid setup" rate among winners against losers. If
   setups are labelled valid more often when they won, the outcome participated in the labelling — which
   is `[HINDSIGHT]` operating at the sample level and it inflates every downstream number.
5. **Regime concentration.** One instrument, one month, one volatility regime, one direction. Twenty
   setups from a single trending month is closer to one observation than twenty.
6. **Non-independence.** Setups from the same session, or off the same HTF leg, are not independent
   draws. Count distinct days and distinct HTF legs alongside the raw count; the smaller number is the
   real sample size.
7. **Variance illiteracy.** Run `check_arithmetic.py` with a `backtest` block for the Wilson interval.
   Twelve wins in twenty is a 95% interval of roughly 39–79% — an observation compatible with a coin and
   with a strong edge simultaneously. Conclusions drawn from a point estimate inside an interval that wide
   are `[METHOD]` failures regardless of how carefully each setup was read.
8. **Criteria mutation between samples.** Entry rules adjusted after seeing the first batch, then applied
   to the second, with results pooled. The pooled number describes no strategy that ever existed.

**Rationing per-setup depth.** After the battery, give full treatment to at most three setups — the two
that carry the most weight in the user's conclusion and the one that most clearly contradicts it — and one
line each for the rest. A twenty-setup review with twenty full objection lists is unreadable, and its
length hides the cross-setup findings that were the point.

**Discharged by.** Per item: the rule table with constant columns (1); a pre-fixed date range (2); a log
including non-taken qualifying setups (3); comparable valid-rates across outcomes (4); a spread of
instruments and regimes (5); a distinct-day count close to the setup count (6); an interval narrow enough
to exclude the null (7); separate reporting of the two samples (8).

---

## Part 1 — Attack vectors by model step

### Step 1 — HTF PD array / bias

**Standard.** A directional bias anchored in a *specified* higher-timeframe dealing range, with named
swing boundaries, and a statement of where price sits inside it (premium / discount / equilibrium)
plus which HTF array price is reaching for.

**Attack vectors.**

1. **The dealing range boundaries are chosen, not derived.** This is the single highest-yield attack in
   the entire model, because every downstream conclusion inherits it. Swap one boundary swing for the
   adjacent one and premium becomes discount, the OTE band relocates, and the "correct side of the
   range" argument reverses. Ask which two swings define the range and why *those* two: are both
   external-range swings, is the high the actual highest point in the range being measured, has price
   already broken one boundary (which would mean the range is expired rather than active)?
2. **The range is expired.** If price has taken out the range high with a body close and continued, the
   old range is no longer the operative dealing range — a "premium" reading inside a superseded range is
   measuring against a structure the market has already left behind.
3. **Bias asserted from candle appearance rather than from the range.** "D1 is clearly bullish" with no
   named range is not step 1, it is a vibe. `[UNSUPPORTED]`.
4. **Timeframe mismatch.** The bias is claimed as the higher timeframe (e.g. D1) but the reasoning cites
   the next timeframe down (e.g. H1) structure. Then it is a lower-timeframe bias and it does not carry
   HTF authority in whatever multi-timeframe ordering the analysis itself declares.
5. **The named HTF array is not actually unmitigated.** If the D1 FVG being "reached for" was already
   traded through, the draw argument weakens considerably.
6. **Arithmetic.** Run the premium/discount computation. A stated `discount` that computes to 0.68 of
   range is `[ARITHMETIC]` and fatal to step 1 as written.

**Self-deception.** Boundaries get selected *after* the direction is decided, so the range always
conveniently puts price on the tradeable side. The tell is a range whose boundaries are unusual swings
that happen to make the setup work.

**Forcing question.** "Name the two swing points defining your dealing range, and give me the premium/
discount fraction that follows from them and current price. Then tell me what the fraction becomes if I
move the high to the next swing up."

**Discharged by.** A D1 chart showing the two boundary swings, with the arithmetic agreeing with the
label, and the boundary choice defended on external-range-swing grounds rather than convenience.

---

### Step 2 — Liquidity run

**Standard.** A resting pool of stops (PDH/PDL, PWH/PWL, relative equal highs/lows, session high/low,
prior swing) was actually taken *and used* — that is, price traded beyond the level and was rejected
from it, not merely touched it.

**Attack vectors.**

1. **Touch, not sweep.** Price reached the level and turned. Nothing was taken. No stops were filled
   above/below, so the liquidity event the model requires did not occur.
2. **Swept but not rejected.** Price traded through and kept going, or consolidated beyond the level.
   That is expansion through liquidity, not a sweep that fuels a reversal — and it usually means the
   level was the *origin* of continuation rather than the turning point.
3. **The pool was not a real pool.** A single swing high in the middle of a range is not a meaningful
   stop pool. Relative equal highs, session extremes and prior-day/week extremes are; an arbitrary
   intraday wick generally is not. Ask what makes this level one where stops would rest.
4. **Wrong-side sweep.** For a long, the model wants sellside liquidity taken. If the analysis points at
   a buyside sweep and then goes long, step 2 is inverted and the whole sequence is misassembled.
5. **The sweep is stale.** The sweep happened many sessions ago and price has since done other things.
   The reversal it was supposed to fuel already played out or already failed.
6. **Sweep identified only in hindsight.** At the hard right edge, the wick had not yet been rejected
   from — the rejection is the *next* candle. If the entry decision was made before the rejection
   existed, the sweep was an assumption at decision time. `[HINDSIGHT]`.

**Self-deception.** Any wick that pokes a line gets promoted to "sweep" because the model needs one and
the rest of the setup looks good.

**Forcing question.** "Which specific pool, at what price, and what is your evidence it was taken *and
used* rather than touched — which candle rejected from it, and had that candle closed when you made the
decision?"

**Discharged by.** A chart showing the level, a trade beyond it, and a rejection candle that had
completed before the entry decision.

---

### Step 3 — Displacement

**Standard.** An energetic, one-sided expansion away from the sweep, fast relative to the surrounding
structure, dominated by large candle bodies, leaving an imbalance behind.

**Attack vectors.**

1. **Grind mislabelled as displacement.** Overlapping candles with long wicks and small bodies that
   happen to travel in the right direction. Directionally correct, energetically absent. Compare the
   candle bodies to the preceding 20–30 candles on the same timeframe — if they are ordinary, this is
   not displacement, and the model's step 3 is unmet.
2. **No imbalance left behind.** Genuine displacement leaves a gap. If you cannot point to the
   inefficiency it created, the "displacement" claim and the step-4 FVG claim collapse together — and
   note that in a valid sequence step 4's FVG must be a *byproduct* of this exact leg.
3. **Displacement in the wrong place.** It occurred before the sweep rather than after it, which breaks
   the causal ordering the model depends on. Order matters: sweep → displacement, not the reverse.
4. **Displacement is the whole move.** Sometimes the "displacement" already travelled to the target. If
   the leg has consumed the distance to the DOL, the trade is being taken at the end of delivery rather
   than at its origin, and the reward side of the setup is largely gone.
5. **Zoom illusion.** On a zoomed-in M5 chart every impulse looks violent. Ask what the same leg looks
   like as a fraction of the day's range, or of the H1 candle it lives inside. An M5 "displacement" that
   is a 2-tick body on H1 is not displacement in any structurally meaningful sense.
6. **Volatility context ignored.** A large-bodied candle at a news release or session open may be noise
   at that hour rather than delivery. If the analysis leans on candle size alone, that is a gap.

**Self-deception.** "Price moved fast in my direction" is emotionally indistinguishable from
displacement in the moment, and the difference is only visible when you compare against context rather
than against expectation.

**Forcing question.** "Give me the body size of your displacement candles against the median body of
the prior 20 candles on that timeframe, and point to the imbalance the leg left behind."

**Discharged by.** A visible leg with bodies clearly outsized relative to local structure, a visible
resulting gap, and correct ordering after the sweep.

---

### Step 4 — FVG created

**Standard.** A three-candle imbalance created *by the displacement leg in step 3*, with a stated high,
low and consequent encroachment (the 50% midpoint).

**Attack vectors.**

1. **Wrong FVG.** The gap being traded is from an earlier leg, not the displacement leg. It is a real FVG
   but it is not *this* setup's FVG, and it carries none of the narrative weight the analysis is giving
   it.
2. **Not actually a gap.** Wicks overlap across the three candles, so there is no imbalance — only a
   large-bodied candle that looks like one. Check whether candle 1's high and candle 3's low genuinely
   fail to overlap.
3. **Stale / already mitigated.** Price has traded into this gap before. The inefficiency it represented
   has been at least partly rebalanced, and the argument for a reaction is much weaker on a second visit
   than a first.
4. **Inverted, and the analysis missed it.** Price traded fully through the FVG with a close beyond it,
   which flips it into an inversion FVG — the same zone now argues the opposite direction. This is one
   of the most powerful `[CHART]` objections available because it converts the user's own support into
   the counter-case's resistance without introducing a single new fact.
5. **CE arithmetic wrong.** Stated consequent encroachment is not the midpoint of the stated high and
   low. `[ARITHMETIC]`.
6. **Too small to be tradeable, or too large to be meaningful.** A gap thinner than typical spread plus
   slippage cannot be entered at CE with any precision; a gap so large that CE sits far from either edge
   makes "entered at the FVG" nearly content-free — say which part of it, and why.
7. **FVG in the wrong location in the narrative.** A bullish FVG sitting in the premium half of the
   dealing range is a much weaker long POI than one in discount, regardless of how clean the gap is.

**Self-deception.** The gap is drawn after the fact, sized to contain the low that price actually made.
Ask whether the box would have been drawn identically at the hard right edge.

**Forcing question.** "Which three candles form this FVG, does its origin leg match your displacement
leg, has price been inside it before, and what is (high+low)/2?"

**Discharged by.** Three identified candles, a genuine non-overlap, an unmitigated first visit, and
CE arithmetic that checks out.

---

### Step 5 — MSS / CISD

**Standard.** A break of a *structurally significant* swing point in the direction of the displacement,
confirmed by a body close beyond it — not a wick, and not a general impression that structure looks
different.

**Attack vectors.**

1. **Wick break, no body close.** The most common and most decisive failure. Cite the breaking candle's
   close relative to the level.
2. **Internal grab promoted to MSS.** The swing broken was a minor internal swing inside a larger intact
   structure. Breaking it changes nothing about the operative structure — and internal MSS is
   particularly unreliable when it points *against* the higher timeframe. This is the user's most
   frequently repeated error; see Part 3.
3. **MSS against HTF with no HTF validation.** Even a clean, body-confirmed M5 MSS carries little weight
   if H1 structure is intact in the opposite direction. Demand the H1 read: is there an H1 MSS/BOS
   supporting this, or is the M5 shift a countertrend retracement inside an intact H1 leg?
4. **Retrospective swing selection.** Which swing counts as "the" swing was decided after seeing which
   one price broke. Ask the user to name the swing they had marked *before* the break.
5. **CISD conflated with MSS.** They are different claims with different evidence requirements. CISD is
   about the state of delivery changing (a run of opposing candles being closed through); MSS is a swing
   break. Using the terms interchangeably usually means neither has been established rigorously.
6. **MSS occurred, then failed, before entry.** Price shifted structure and then reclaimed the level
   before the entry was taken. The shift the analysis relies on had already been invalidated at decision
   time.

**Self-deception.** Once a position is intended, any structural break in the desired direction feels
significant. Significance has to be defined by the structure that existed *before* the break, which
means it can be stated in advance — and if it wasn't, that is the finding.

**Forcing question.** "Which swing, at what price, what was the breaking candle's close, and was that
swing structurally significant on the higher timeframe or internal to it?"

**Discharged by.** A named swing, a body close beyond it, and an argument for its significance that does
not depend on the break having happened.

---

### Step 6 — Entry (FVG / CE / OTE)

**Standard.** A retracement into the FVG (ideally to CE), into the OTE band (0.62–0.79 of the impulse
leg), or into an order block / breaker. This is read on whichever timeframe the user's own analysis uses
for execution — call it the LTF, whatever it actually is (M5, M15, H1, or otherwise). If no chart at
that execution timeframe exists, step 6 cannot be evaluated at all — an execution-shaped conclusion
drawn only from higher-timeframe data is fabrication.

**Attack vectors.**

1. **Proximal edge entry sold as a CE entry.** Entering at the near edge gives a better price and a
   worse confirmation. That is a legitimate choice, but it has to be *stated* as the choice it is, and
   it does not inherit CE's evidential weight. Check whether the stated entry actually sits at CE.
2. **OTE arithmetic wrong, or the impulse leg is the wrong leg.** Recompute 0.62 / 0.705 / 0.79 from the
   stated leg. Then question the leg itself: OTE measured from a different swing pair relocates the whole
   band, and the leg is often chosen so the band contains the price the user already wanted.
3. **Entry outside the band being claimed.** Entry at 0.55 is not OTE. Entry at 0.85 is not OTE. Say the
   number.
4. **Entry not inside the FVG at all.** Compare the stated entry against the stated FVG high/low.
5. **Stop placement doesn't respect the structure the entry relies on.** If the entry thesis depends on
   the sweep low holding, a stop above that low means the thesis and the risk are pointed at different
   levels — the trade can be stopped out with the thesis still intact, which means the stop was not
   derived from the analysis.
6. **Confirmation stacking after the fact.** Listing FVG + OB + OTE + breaker all at the same price is
   often one zone counted four times, not four independent confirmations. Ask which are genuinely
   distinct.
7. **No chart at the execution timeframe provided.** Then every step-6 claim is `[UNSUPPORTED]` and
   should be labelled as such rather than argued about.

**Self-deception.** "I entered at the FVG" is a category that hides enormous variation — edge vs. CE vs.
far edge, fresh vs. stale, with vs. without HTF agreement. The phrase feels like process compliance
while concealing whether any of it was.

**Forcing question.** "Give me your exact entry, the FVG high/low, the CE, the impulse leg swings, and
the 0.62/0.705/0.79 levels. Which of those does your entry actually sit on?"

**Discharged by.** Numbers that agree, on the execution-timeframe chart, with a leg selection defensible
independently of the entry.

---

### Step 7 — Time / killzone

**Standard.** The setup formed inside a killzone or macro window, established from a *visible time axis*
or a time the user explicitly stated — never inferred from general market-hours knowledge.

**Attack vectors.**

1. **No time axis in the screenshot.** Then the killzone claim is `[UNSUPPORTED]`, full stop. Do not
   guess from candle count.
2. **Timezone confusion.** The chart's timezone, the broker's server time, NY time and Vietnam time
   (UTC+7) are four different clocks. A setup "in London killzone" per a UTC+7 chart may be elsewhere in
   NY terms, which is the frame the killzone definitions are written in. Ask which clock.
3. **Setup formed inside the window but entry fell outside it, or vice versa.** These are different
   claims. Which one is being made?
4. **Killzone treated as a confirmation rather than a filter.** Being inside a killzone does not add
   evidence that the read is correct; it only removes one reason to reject it. An analysis that counts
   killzone timing as a supporting pillar has miscounted its own support.
5. **Session boundary gaming.** "Just outside London" and "early NY AM" are frequently the same candle
   described two ways depending on which one helps.

**Self-deception.** Time is the easiest box to tick because it feels objective, which is exactly why an
unstated timezone slips through unexamined.

**Forcing question.** "What timezone is the chart's axis in, what is the setup's time in NY terms, and
which killzone does that fall in?"

**Discharged by.** A visible axis plus a stated timezone, converted to the frame the killzone
definitions use.

---

### Step 8 — Target / DOL

**Standard.** A named opposing liquidity pool or opposing PD array that price is presumably being
delivered toward — a description of the draw, not a trade plan.

**Attack vectors.**

1. **The DOL was already taken.** If the pool the analysis is targeting had already been swept before the
   setup formed, the draw it depends on no longer exists. This is a frequent and fatal oversight.
2. **Target is a round number or a drawn line, not a liquidity pool.** Ask what makes it a pool: whose
   stops rest there, and why.
3. **Nearer opposing liquidity ignored.** If there is an unmitigated opposing array or an untouched pool
   between entry and target, the path assumption is doing unacknowledged work — price plausibly reacts
   there first, which changes the whole risk/reward computation the analysis rests on.
4. **Target chosen to make R work.** The reward figure was needed, so the target was placed where it
   produced it. Tell: the target sits at no identifiable structure.
5. **DOL contradicts the step-1 bias.** A bullish D1 bias with a target below current price, or vice
   versa, means one of the two claims is wrong. `[SELF-CONTRADICTION]`.

**Self-deception.** Targets are the most emotionally motivated number in an analysis, because they are
the number that determines whether the trade sounds worth taking.

**Forcing question.** "Name the pool, show me it is untouched, and tell me what sits between entry and
it."

**Discharged by.** A visible untouched pool consistent with the step-1 bias, with the intervening space
accounted for.

---

## Part 2 — Cross-cutting epistemic failures

Layer 2: granting the claims, do they support the conclusion? Several entries here are the *symptom* of a
Part 0 procedural failure — where that is so, it is noted, and the deeper objection is the one to ship.
Reporting both is double-counting.

**Hindsight contamination.** The dominant failure in `REVIEW` and `BACKTEST` mode. The test is mechanical: cover
everything to the right of the decision candle. Would the boxes be drawn in the same places? Would that
swing have been marked as significant? Would that wick have been called a sweep? Anything that survives
only with the right side visible is `[HINDSIGHT]` and cannot support the analysis. Note the asymmetry —
this cuts against your own objections too. An objection that only works because you can see what
happened next is equally illegitimate; label it or drop it. In `LIVE` mode this section is nearly
inapplicable to the user and applies mainly to you.

**POI shopping.** With enough PD array types available — FVG, OB, breaker, mitigation block, rejection
block, BPR, inversion FVG, opening gaps — some array can be found near almost any price. The existence
of an array at the entry is therefore weak evidence on its own. The question is whether the array was
identifiable and *selected* before price arrived, and whether a competing array pointing the other way
was equally present and simply not mentioned. *This is free parameter 5 in 0.2, and the unmentioned
competing array is 0.6 — if you can name that array, ship the `[CHART]` objection there instead.*

**Timeframe shopping.** If the higher-timeframe read is inconvenient, the analysis quietly becomes a
lower-timeframe read; if that one is inconvenient too, it drops another level. The user's own
higher-timeframe-to-lower-timeframe authority ordering — whatever specific timeframes their analysis
declares — exists to prevent exactly this. Watch for the load-bearing timeframe changing mid-analysis.
*Free parameter 1.*

**The unfalsifiability problem.** Discretionary ICT reads have enough degrees of freedom — which range,
which swing, which array, which timeframe, fresh vs. inverted — that a competent practitioner can
produce a coherent narrative for either direction after the fact. This is not an argument that the model
is worthless; it is an argument that a narrative's coherence is nearly zero evidence of its correctness.
The only thing that distinguishes skill from storytelling is whether the read was **stated in advance
with conditions that could have failed**. When an analysis contains no such condition, the strongest
available objection is often not about any individual step but about this: nothing here could have come
out wrong, so nothing here has been tested. *Run it as 0.1 rather than asserting it here — the
counterfactual test is what converts this from a philosophical complaint into a named missing condition.*

**Curve-fitted backtests.** Boxes drawn to fit a run that is already visible; only winning setups
counted; entry criteria adjusted between samples; the sample drawn from one instrument in one regime.
Ask: how many setups met the criteria and did *not* work, and were they logged with the same diligence?
*Full battery at 0.8.*

**Sample size illiteracy.** Three or four instances support essentially no conclusion about a
discretionary edge. If the analysis generalizes ("this always works when…") from a handful of examples,
that inference is the finding, independent of whether the individual reads were right. Give the interval
rather than the adjective: the `backtest` block of `check_arithmetic.py` computes it.

**Outcome-as-evidence.** "It worked" says nothing about whether the process was sound; the model's own
standards are defined on the setup, not the result. A stale FVG was stale whether or not price respected
it. Hold this line especially firmly when the user cites profit as a rebuttal.

**Vocabulary as substitute for evidence.** A paragraph dense with correct terminology can contain no
verifiable claim at all. Strip the jargon and ask what observable fact each sentence asserts. Sentences
that survive that translation are claims; the rest is atmosphere.

**Annotation drift.** The drawn box and the price action underneath it disagree more often than anyone
expects — a "FVG" box whose edges sit a few ticks off the actual candle extremes, an OB box drawn around
the wrong candle in the cluster, an entry marker at a price the candles never traded. Because every
downstream number (CE, OTE band membership, R multiple) is measured off the box rather than the candles,
a box drawn slightly wide is a silent arithmetic error running through the whole analysis. Always check
the box against the three candles rather than reading the label. This is `[CHART]`, and it is one of the
highest-yield checks available precisely because nobody re-measures their own boxes.

**The inverse case's own base rate.** Worth holding in mind while writing Part 4: with enough PD array
types available, a plausible opposite reading can be constructed for nearly any chart. That means the
*existence* of your counter-case is close to zero evidence that the user is wrong, and treating its
coherence as though it were evidence is the exact error you are criticising them for. Only a named
observable that separates the two readings carries weight.

---

## Part 3 — This user's documented recurring errors

These are established patterns from prior review, so they warrant a deliberate check on every analysis
rather than waiting for them to surface. Their presence still has to be demonstrated from the evidence
in front of you — a documented tendency is a reason to *look*, never a substitute for finding it. This
list is populated by this specific user's own history and is expected to accumulate or change over time
as new case studies are reviewed — it is not a fixed or universal list, and the timeframe letters below
(H1, M5) are the pair this user has most often submitted; substitute whatever HTF/execution-timeframe
pair the current case study actually uses.

1. **Counter-HTF entry without higher-timeframe structural validation.** The signature error. A
   lower-timeframe setup (commonly M5) is taken against an intact higher-timeframe structure (commonly
   H1), with the lower-timeframe MSS treated as sufficient authority. Always run the explicit check:
   does the higher timeframe confirm, contradict, or stay silent? "Silent" is not "confirm".
2. **Weak FVG reaction after MSS.** Entry at an FVG following an apparent MSS and displacement, followed
   by a shallow reaction that reverses into the stop. Root causes to test individually: low-quality
   displacement, stale or previously tested FVG, proximal-edge entry where CE was the plan, DOL already
   swept before the setup formed, setup outside killzone hours.
3. **Displacement quality overestimated.** Grind read as expansion. Force the body-size comparison.
4. **FVG staleness overlooked.** Whether price has been inside the gap before is frequently unchecked.
5. **CE vs. proximal entry conflated.** The distinction collapses under time pressure; check the numbers
   rather than the label.
6. **DOL misidentification.** Especially targeting a pool that was already taken.
7. **Killzone adherence asserted without a visible time axis.**

---

## Part 4 — Inversion toolkit

To build the opposite case without inventing evidence, keep every observed fact and reassign its
narrative role. Each row is a legal reinterpretation of the *same* chart.

| Observed fact | User's role for it | Inverted role |
|---|---|---|
| Wick through a level | Sweep that begins the reversal | Terminus of a move already complete, or first push of continuation through the level |
| Large-bodied leg | Displacement originating new delivery | Final expansion *into* the target; the move is over, not starting |
| Fair value gap | Support to be respected on retest | Gap that will be traded through and inverted, becoming resistance |
| Swing break | MSS establishing a new structure | Internal grab inside a larger structure that remains intact |
| Price in discount of range X | Correct side for a long | Premium of range Y, where Y is the range with the adjacent boundary swing |
| Untouched pool above | DOL, the draw for the long | Stop pool that will be run *against* late longs, then reversed from |
| Order block at entry | Institutional demand | Distribution zone that has already been mitigated |
| Consolidation before the move | Accumulation (Power of Three) | Redistribution before continuation down |

**Highest-yield inversions in practice.** Boundary-swap on the dealing range (flips premium/discount and
therefore the "right side of the range" argument); FVG inversion (converts the user's support into the
counter-case's resistance); demoting an MSS to an internal grab (removes the structural mandate for the
entry entirely); and reading the displacement as terminal rather than initial (leaves the setup
technically intact but strips the reward side).

**The honesty check.** After building the inverse case, ask: did I use any fact not in the evidence
inventory? If yes, remove it and rebuild. If the inverse case cannot stand without it, the correct
label is **not viable** — report that, and say what would make it live.

---

## Part 5 — Risk and prop-firm rule attacks

**Note.** Prop firm rules change, and the specifics below should be verified against the firm's current
rulebook rather than trusted from memory. What does not change is the *class* of error worth attacking.

1. **Claimed R vs. computed R.** Recompute from entry, stop and target. A stated 1:4 that computes to
   1:1.8 changes whether the decision was defensible at all. `[ARITHMETIC]`.
2. **Stop derived from the round number rather than the structure.** If the stop's placement isn't
   justified by the level the thesis depends on, the risk is arbitrary and the R figure is decorative.
3. **Risk-per-trade against a drawdown budget, not against the balance.** On a 10K account the binding
   constraint is the daily-loss and overall-drawdown allowance, not the balance. Two percent per trade
   is three losses from a rule breach, and a strategy whose losses cluster (which discretionary
   sequences do) makes clustered losses the normal case rather than the tail.
4. **FTMO vs. The5ers treated as the same problem.** They differ in ways that change position sizing:
   FTMO's daily loss measures against a fixed starting balance and its programme has a minimum
   trading-day requirement; The5ers resets from the prior day's closing equity and requires a number of
   profitable days above a threshold. A plan built for one can breach the other while looking compliant.
   Verify the current numbers before quoting any.
5. **Equity-curve arithmetic ignored.** "10% target at 1% risk and 50% win rate at 1:2" is a claim about
   a distribution, not a plan. Ask what the expected drawdown along that path is, and whether it fits
   inside the allowance.
6. **Backtest R not achievable live.** Entry at CE to the tick, no spread, no slippage, no partial fill.
   The backtested R is an upper bound; if the plan needs the upper bound, it has no margin.

---

## Part 6 — The objection filter

Read this before shipping, every time. Objections are not free: each one costs the user time to check,
and a list padded with weak entries trains them to skim the strong ones. Cutting is not softening — a
five-objection response where all five land is a harder attack than a fifteen-objection response where
ten are noise, because the user acts on the first and discounts the second.

### The three tests

Apply all three to every drafted objection.

1. **Discharge test.** Name the specific, obtainable evidence that would retract it. If the user cannot
   possibly answer it, it is rhetoric, not an argument. **Delete.**
2. **Consequence test.** State in one clause what changes in the conclusion if you are right. Cannot
   state it → **delete**. States something the conclusion survives unchanged → it is `minor`, and the
   `minor` budget is three for the whole response.
3. **Rebuttal test.** Write the best single-sentence answer the user could give *from evidence already in
   your inventory*. Then judge it honestly:
   - The answer defeats the objection → **delete it and do not ship it.** You have just done their
     checking for them; making them repeat it is a tax on their attention and a hit to your credibility.
   - The answer wounds it → ship it with the answer pre-empted in the `Your best answer:` line. This is
     strictly stronger than making them find the answer themselves and then wondering whether you missed
     it or hid it.
   - No answer exists from the available evidence → this is your strongest material. Lead with it.

Report the outcome in one line at the end of section 3: *"Draft 11 objection, cắt 4 (2 không nêu được
consequence, 2 bị chính evidence base của bạn bác)."* A critique that cuts nothing did not run the filter,
and saying so is itself information about how much the surviving objections are worth.

### Objections that fail the filter by construction

These consume space, dilute the credible objections, and train the user to discount you.

- **"You should have waited for more confirmation."** Unfalsifiable and always available. There is
  always more confirmation. Name the *specific* confirmation the model itself requires and show it was
  absent — otherwise this is not an objection.
- **"The market is random / ICT isn't real."** Not the assignment. The user is testing an ICT read
  against ICT's own standards; a framework-level dismissal answers a question nobody asked.
- **"Risk was too high"** with no numbers. Compute it or drop it.
- **Restating a step as an objection.** "You needed a sweep before entry" is doctrine the user already
  accepts. The objection is that *this* wick did not qualify, with the reason.
- **Attacking the writeup rather than the analysis.** Missing labels in a screenshot are a documentation
  problem worth one line in action items, not an objection to the thesis.
- **Piling on after the load-bearing claim is already broken.** Once step 1's range is shown to be
  wrong, cataloguing downstream errors that all inherit from it adds no information. Say once that they
  inherit, and stop.
- **Reporting a Part 2 symptom and its Part 0 cause as two objections.** "POI shopping" and "free
  parameter 5 was fitted" are one finding. Ship the deeper one.
- **Abstract procedure complaints.** A Part 0 objection with no named chart-specific instance fails the
  discharge test automatically — there is nothing the user could produce to retract it. Either find the
  instance or move it to `Hypotheses to check`.

### The one thing worth over-reporting

Risk-rule and position-sizing breaches, and any arithmetic contradiction. These are cheap for the user to
verify, impossible to argue with, and independently capable of ending an evaluation account. They are
exempt from the severity budget: report every one you find, compressed to a line each if there are
several.