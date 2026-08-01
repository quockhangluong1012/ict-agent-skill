# Rebuttal playbook — where ICT 2022 analyses actually break

## How to read this file

Do not load all of it. It is a checklist against omission, not a menu to fill — an objection is worth
making because you found it on the chart, never because it appears here.

- **Always read** Part 2 (cross-cutting failures) and Part 3 (the user's recurring errors). Both are
  short and both catch things that are invisible from a single step's perspective.
- **Read the Part 1 sections for the steps actually in play.** If the analysis makes no OTE claim, skip
  step 6.
- **Read Part 4** before writing the opposite case, **Part 5** if numbers or risk are stated, and
  **Part 6** if your objection list has grown past about six items.

The `[METHOD]` tier maps almost entirely to Part 2; `[DOCTRINE]` maps to the **Standard** paragraph of
each Part 1 section.

## Contents

- [How to use this file](#how-to-use-this-file)
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
- [Part 6 — Objections not worth making](#part-6--objections-not-worth-making)

---

## How to use this file

Each step below gives five things: the **standard** the claim has to meet, the **attack vectors**
ranked roughly by how often they land, the **self-deception** that usually produces the error, the
**forcing question**, and **what discharges** the objection. The discharge condition is not optional —
an objection the user cannot possibly answer is a rhetorical move, not an argument.

The standards here are the ICT 2022 Model's own definitions, which makes them fair `[DOCTRINE]`
ammunition. The chart-specific facts are not here and never will be; those you must read off the
screenshots the user actually gave you.

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
4. **Timeframe mismatch.** The bias is claimed as D1 but the reasoning cites H1 structure. Then it is an
   H1 bias and it does not carry HTF authority in a D1 → H1 → M5 workflow.
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
leg), or into an order block / breaker. In a D1 → H1 → M5 workflow this is read on M5. If no M5 chart
exists, step 6 cannot be evaluated at all — an M5-shaped conclusion drawn from H1 data is fabrication.

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
7. **No M5 chart provided.** Then every step-6 claim is `[UNSUPPORTED]` and should be labelled as such
   rather than argued about.

**Self-deception.** "I entered at the FVG" is a category that hides enormous variation — edge vs. CE vs.
far edge, fresh vs. stale, with vs. without HTF agreement. The phrase feels like process compliance
while concealing whether any of it was.

**Forcing question.** "Give me your exact entry, the FVG high/low, the CE, the impulse leg swings, and
the 0.62/0.705/0.79 levels. Which of those does your entry actually sit on?"

**Discharged by.** Numbers that agree, on an M5 chart, with a leg selection defensible independently of
the entry.

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

**Hindsight contamination.** The dominant failure in chart review. The test is mechanical: cover
everything to the right of the decision candle. Would the boxes be drawn in the same places? Would that
swing have been marked as significant? Would that wick have been called a sweep? Anything that survives
only with the right side visible is `[HINDSIGHT]` and cannot support the analysis. Note the asymmetry —
this cuts against your own objections too. An objection that only works because you can see what
happened next is equally illegitimate; label it or drop it.

**POI shopping.** With enough PD array types available — FVG, OB, breaker, mitigation block, rejection
block, BPR, inversion FVG, opening gaps — some array can be found near almost any price. The existence
of an array at the entry is therefore weak evidence on its own. The question is whether the array was
identifiable and *selected* before price arrived, and whether a competing array pointing the other way
was equally present and simply not mentioned.

**Timeframe shopping.** If the D1 read is inconvenient, the analysis quietly becomes an H1 read; if H1
is inconvenient, an M5 read. The workflow's authority ordering (D1 → H1 → M5) exists to prevent exactly
this. Watch for the load-bearing timeframe changing mid-analysis.

**The unfalsifiability problem.** Discretionary ICT reads have enough degrees of freedom — which range,
which swing, which array, which timeframe, fresh vs. inverted — that a competent practitioner can
produce a coherent narrative for either direction after the fact. This is not an argument that the model
is worthless; it is an argument that a narrative's coherence is nearly zero evidence of its correctness.
The only thing that distinguishes skill from storytelling is whether the read was **stated in advance
with conditions that could have failed**. When an analysis contains no such condition, the strongest
available objection is often not about any individual step but about this: nothing here could have come
out wrong, so nothing here has been tested.

**Curve-fitted backtests.** Boxes drawn to fit a run that is already visible; only winning setups
counted; entry criteria adjusted between samples; the sample drawn from one instrument in one regime.
Ask: how many setups met the criteria and did *not* work, and were they logged with the same diligence?

**Sample size illiteracy.** Three or four instances support essentially no conclusion about a
discretionary edge. If the analysis generalizes ("this always works when…") from a handful of examples,
that inference is the finding, independent of whether the individual reads were right.

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
in front of you — a documented tendency is a reason to *look*, never a substitute for finding it.

1. **Counter-HTF entry without H1 structural validation.** The signature error. An M5 setup is taken
   against an intact H1 structure, with the M5 MSS treated as sufficient authority. Always run the
   explicit check: does H1 confirm, contradict, or stay silent? "Silent" is not "confirm".
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

## Part 6 — Objections not worth making

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