# ict-audit — rubric, taxonomy, and output contract

Load this before writing an audit. It defines (a) the three states every claim
lands in, (b) the error taxonomy and its short tags, (c) a condensed ICT-2022
recap so you judge against the model rather than a vibe, (d) the exact output
template, and (e) a worked example. The SKILL.md body tells you *when* and *how*
to run the audit; this file tells you *what a finding is* and *how it reads*.

---

## The three states (the spine of the whole audit)

Every substantive claim in the user's analysis resolves to exactly one:

- **Supported** — the JSON facts back it. It needs no finding unless the user's
  overall read hinges on it and you want to name it in the verdict line.
- **Contradicted** — the JSON facts say otherwise (or the `check_facts.py`
  output printed a CONTRADICTION for it). This is a hard error. HIGH severity by
  default.
- **Unsupported** — the JSON has no evidence either way: the relevant field is
  `null` / `unknown`, the timeframe was never provided, or the claim is about
  something the extraction simply doesn't cover. **This is the category the user
  cares about most: "asserted but not proven."** It is *not* the same as wrong —
  say "unproven," not "incorrect."

Keeping Contradicted and Unsupported separate is the single most important
discipline in this skill. Collapsing them ("that's wrong") when the truth is
"you have no evidence for that yet" destroys the audit's value for backtesting.

---

## Error taxonomy (tags used in findings)

Use the short tag in the output. Severity is HIGH / MED / LOW.

- **`EVIDENCE`** — claim contradicted by a JSON fact (price zone, level, MSS
  direction, sweep, etc.). Ground it in the specific field/value.
- **`UNSUPPORTED`** — claim with no backing in the JSON (`null`, `unknown`,
  timeframe absent). Asserted, unproven.
- **`PD/RANGE`** — misidentified PD array, dealing range bounds, or
  premium/discount/equilibrium classification. Check against the computed zone
  from `check_facts.py`, not against the chart's "feel."
- **`STRUCTURE`** — MSS / CISD / BOS claimed without the thing that defines it:
  an actual swing-point break with a **body close** beyond it, in the
  displacement direction. A wick through a level is not an MSS. "Structure looks
  different now" is not an MSS.
- **`ENTRY`** — an entry / OTE / CE read that is missing where the analysis
  needs one, OR asserted where the JSON can't support it (e.g. entry described
  on M5 when no M5 was provided, or OTE claimed with `ote` null).
- **`LOGIC`** — the ICT-2022 reasoning itself is broken: steps invoked out of
  order (e.g. "entry off the FVG" before any displacement/FVG exists), a
  non-sequitur ("swept liquidity, therefore premium"), or a conclusion that
  doesn't follow from its stated premises.
- **`HINDSIGHT`** — outcome-driven reasoning: the setup is justified only
  because the resolution is already visible. Tells: an entry with no trigger
  stated at entry time, "it then ran to target" used as *evidence* the read was
  right, levels drawn to fit where price went. Critical for honest backtests —
  flag it wherever the argument leans on knowing the outcome.
- **`CONSISTENCY`** — the analysis contradicts *itself* (calls the zone discount
  in one line and premium in another; bias long but target below current price
  with no reversal logic).

A single claim can carry two tags (e.g. `PD/RANGE`+`EVIDENCE`). Pick the most
specific one as primary; mention the second only if it adds information.

---

## Severity

- **HIGH** — a load-bearing claim is Contradicted, or a core step (bias, MSS,
  entry) rests on broken logic / hindsight. If this claim falls, the analysis's
  conclusion falls.
- **MED** — a real gap that weakens the case but isn't fatal: a key claim
  Unsupported, a secondary structure call unjustified.
- **LOW** — imprecision, a minor unproven aside, terminology slippage that
  doesn't change the conclusion.

Rank findings by severity, HIGH first. Within a severity, order by how central
the claim is to the user's conclusion.

---

## Condensed ICT-2022 recap (judge against this, not a vibe)

1. **HTF bias / PD array** — where price sits in the HTF dealing range
   (premium/discount/equilibrium) and which HTF array it reaches for. Read on D1.
2. **Liquidity run** — a *resting pool actually taken* (PDH/PDL, PWH/PWL, equal
   H/L, session H/L) and *used* (rejected from), not merely wicked.
3. **Displacement** — energetic one-sided expansion leaving imbalance. Judged by
   body size/speed vs prior structure. Grinding/overlapping ≠ displacement.
4. **FVG** — the gap left *by that displacement leg*. CE = its 50% midpoint. A
   gap unrelated to step 3 doesn't count.
5. **MSS / CISD** — swing-point break with a **body close** beyond, in the
   displacement direction. Not a wick; not "looks different."
6. **Entry** — retrace into FVG (ideally CE) or OTE band **0.62–0.79** of the
   impulse leg, or OB/breaker. Normally an **M5** read; if no M5 was provided,
   this step is unevaluable — say so.
7. **Time** — inside a killzone (London 02:00–05:00 NY, NY AM 07:00–10:00,
   Silver Bullet 10:00–11:00, NY PM 13:30–16:00) or macro. Only from a visible
   time axis or a time the user stated — never inferred from market hours.
8. **Target** — opposing liquidity pool / opposing PD array as the draw. A
   *description of the implied draw*, never a trade recommendation.

---

## Hard guardrails (non-negotiable)

- **The JSON is the evidence base.** Adjudicate the prose against it. Do **not**
  invent chart facts to settle a claim. If the JSON can't settle it, the claim
  is Unsupported — full stop.
- **No trade advice, ever.** No entry/SL/TP of your own, no directional call, no
  "I would take this." You assess the *analysis*, not the *trade*.
- **No coaching.** Name the specific flaw and why it fails. Do not add
  "next time try…", pep talk, or generic study tips. Explanation ≠ coaching: "MSS
  claimed on a wick, not a body close" is explanation; "you should practice
  spotting MSS" is coaching — omit the latter.
- **If an image is attached and it plainly conflicts with the JSON**, do not
  silently swap in your own chart read. Note once, as a WARNING, that the
  extraction itself may be off — then continue adjudicating against the JSON.
- **No praise padding, no hedging fluff.** Supported claims get at most the
  verdict line. Every finding must carry information.
- **No speculative objections.** A finding must resolve against the JSON as
  Contradicted or Unsupported. If the strongest form is "maybe / probably / có
  thể / smart money likely intended…," it is not a finding — make it
  `UNSUPPORTED` or drop it. Concretely forbidden: "có thể ở H1 có OB chưa
  mitigate," "HTF chắc đang bearish," "smart money probably wanted…," or any
  invented sweep / structure / session the JSON doesn't contain. You may only
  attack with evidence that exists.
- **Flag single-point verdicts.** When a HIGH verdict rests entirely on **one**
  extracted number that isn't cross-checked elsewhere in the JSON (e.g. a lone
  `current_price` with no corroborating level), append `— dựa trên 1 số extract
  chưa đối chiếu` to that finding. The JSON is authoritative for adjudication,
  but it is itself an extraction that can be wrong; don't launder a single fragile
  field into false certainty.
- **JSON self-inconsistency is a data warning, not a user finding.** When
  `check_facts.py` reports checklist↔data contradictions (a checklist flag true
  while its block is empty), the fault is the *extraction's*, not the user's
  analysis. Open with one line — `WARNING: JSON tự mâu thuẫn (N mục checklist)` —
  and treat any prose that cites those flags as `UNSUPPORTED`. Do not tag the
  user with `EVIDENCE` for trusting a checklist the extractor filled in wrong;
  the honest verdict there is usually `THESIS UNPROVEN` on unreliable evidence.

---

## Output template (use exactly this shape)

Keep it tight. Drop any section that would be empty. Findings are the substance;
everything else is one line.

```
**Verdict:** <ONE of: THESIS BROKEN | THESIS UNPROVEN | THESIS SURVIVES, WEAKENED | THESIS SURVIVES INTACT> — <≤1 clause why>
**Load-bearing claim:** "<the one claim the thesis rests on>" → <its state>
**Evidence base:** present <tf list> · gaps <what's missing → which step unevaluable>

**Findings (ranked):**
1. `[HIGH·EVIDENCE]` "<short quote>" → contradicted: <field=value>. <one clause why it matters>. gỡ khi: <evidence that would discharge it>.
2. `[HIGH·STRUCTURE]` "<claim>" → MSS asserted on a wick; JSON shows no body close beyond <level>. Step 5 not met. gỡ khi: <M5 body close beyond level>.
3. `[MED·UNSUPPORTED]` "<claim>" → no evidence (<field>=null / M5 absent). Unproven, not wrong.
...

**Opposite read:** <one-line inverse read from the SAME facts> — <stronger | equally viable | weaker but non-trivial | not viable>
**Missing / unevaluable:** <steps not addressed, or not checkable, comma-separated one-liners>
```

The verdict enum keys off the **load-bearing claim's** state, not the finding
count: load-bearing Contradicted → `THESIS BROKEN`; load-bearing Unsupported /
unevaluable → `THESIS UNPROVEN`; load-bearing Supported but real secondary gaps →
`THESIS SURVIVES, WEAKENED`; everything Supported → `THESIS SURVIVES INTACT`.
Only **HIGH** findings carry the `gỡ khi:` (discharge) clause — the evidence that
would overturn them; MED/LOW stay a single clause so length tracks stakes. The
`Opposite read` line is dropped only when the inverse is trivially `not viable`
*and* the thesis already broke on its own terms; otherwise always include it,
since an `equally viable` inverse is itself a strong audit result.

**Fully-supported analysis (zero findings).** When nothing is contradicted or
unsupported, do not pad with invented findings. Write `**Findings (ranked):**
none.` and add one certifying line so the user sees the read was actually
checked, not skimmed:

```
**Verdict:** Internally consistent and fully supported across the steps present; nothing contradicted or unproven.
**Evidence base:** present <tf list> · <gaps or "no gaps"> (confidence <overall>)

**Findings (ranked):** none.
**Supported backbone:** <compact ✓ list of the claims that checked out — bias, sweep→displacement→MSS, OTE/entry, killzone, target — each with the field that backs it>.
**Missing / unevaluable:** <none, or the steps that couldn't be checked>
```

The `Supported backbone` line appears **only** on a zero-finding audit — it is a
certification, not praise, so keep it to one line of field-grounded ✓ items, not
adjectives. When there is even one finding, drop this line; supported claims then
live in the verdict only.

Notes on style:
- Quote the user in ≤10 words; paraphrase past that.
- One line per finding. If a finding needs two clauses, use one sentence, not a
  paragraph.
- No preamble ("Here is your audit…"), no closing ("Let me know if…").
- Vietnamese prose is fine; keep ICT terms in English. Match the user's language.

---

## Worked example (abbreviated)

**User analysis (excerpt):** "D1 đang ở discount nên tôi bias long. Giá sweep
PDL rồi tạo MSS trên H1, tôi vào lệnh ở FVG M5 vùng OTE, target là PDH. Sau đó
giá chạy đúng lên PDH nên setup này chuẩn."

**check_facts.py prints (abbrev):**
- present: [D1, H1]  (no M5)
- current_price=1.0820 -> computed zone = **premium** (stated: discount)  → CONTRADICTION
- gaps: step 6 needs M5, absent → UNEVALUABLE

**Audit:**
```
**Verdict:** THESIS BROKEN — the long bias sits on a zone the JSON contradicts.
**Load-bearing claim:** "D1 ở discount → bias long" → Contradicted
**Evidence base:** present D1, H1 · gaps M5 absent → Entry/OTE unevaluable

**Findings (ranked):**
1. `[HIGH·PD/RANGE]` "D1 ở discount" → contradicted: current_price=1.0820 in dealing_range computes to premium. The long bias is built on a false zone. gỡ khi: dealing_range high/low được sửa lại sao cho 1.0820 rơi vào nửa dưới. — dựa trên 1 số extract chưa đối chiếu.
2. `[HIGH·HINDSIGHT]` "giá chạy đúng lên PDH nên setup chuẩn" → outcome used as proof of the read; no entry-time trigger cited. gỡ khi: nêu được trigger tại decision candle, không dùng diễn biến sau đó.
3. `[MED·ENTRY]` "vào lệnh ở FVG M5 / OTE" → unsupported: no M5 provided, ote=null. Unproven, not wrong.
4. `[MED·STRUCTURE]` "MSS trên H1" → JSON shows a swing high wicked, no body close beyond it. Step 5 not met.

**Opposite read:** cùng dữ kiện (premium + PDH swept) đọc thành bearish draw về sellside — equally viable.
**Missing / unevaluable:** displacement (step 3) not addressed; killzone/time not stated.
```

Notice: the discount claim is the **load-bearing** one, so its Contradicted state
drives `THESIS BROKEN` on its own — the other findings pile on but don't decide the
verdict. Only the two HIGH findings carry `gỡ khi:`; the MED ones stay one clause.
The `PD/RANGE` finding rests on a single `current_price`, so it's flagged as such.
The opposite read is built strictly from facts already in the JSON (premium zone +
swept PDH), adding nothing new. No trade advice, no coaching.