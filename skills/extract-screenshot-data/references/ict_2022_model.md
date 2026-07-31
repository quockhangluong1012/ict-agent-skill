# The ICT 2022 Model — 8-step reference
 
This is the sequence `schema.json` is structured around. When deciding whether evidence is strong
enough to flip a boolean or fill a field, check it against the step definition here, not against a
general sense of "this looks bullish/bearish."
 
1. **HTF PD array / bias** — Where does price sit inside the higher-timeframe dealing range
   (premium vs. discount vs. equilibrium), and which HTF array (order block, FVG, breaker) is price
   reaching for? This is read on D1 (or the highest timeframe image provided).
2. **Liquidity run** — Has a resting pool of stops actually been taken? PDH/PDL, PWH/PWL, equal
   highs/lows, session highs/lows. This is the "Judas swing" / stop run that precedes the real move.
   A wick poking through a level is not enough on its own — look for the sweep being *used*
   (rejected from) rather than just touched.
3. **Displacement** — An energetic, one-sided expansion away from that sweep, leaving an imbalance
   behind. The tell is candle body size and speed relative to the preceding structure, not just
   "price went up." A grinding, overlapping move is not displacement even if it's directionally
   correct.
4. **FVG created** — The displacement leg must leave a Fair Value Gap / liquidity void. Record its
   high, low, and consequent encroachment (the 50% midpoint of the gap). A gap that isn't a direct
   byproduct of the displacement leg in step 3 doesn't belong here.
5. **MSS / CISD** — Market Structure Shift or Change in the State of Delivery, in the direction of
   the displacement. This requires an actual break of a swing point with a body close beyond it —
   not just a wick, and not just "structure looks different now."
6. **Entry** — Retracement into the FVG (ideally to the CE) or into the OTE band (0.62–0.79 of the
   impulse leg), or into an order block / breaker. This step is normally read on the lowest timeframe
   provided (M5, when available) — it's the execution-level confirmation, not the HTF bias.
7. **Time** — Is the setup inside a killzone (London 02:00–05:00 NY, NY AM 07:00–10:00 NY, Silver
   Bullet 10:00–11:00 NY, NY PM 13:30–16:00 NY) or a macro window? Only mark this from an actual
   visible time axis or a time explicitly stated by the user — never assume a session from general
   market-hours knowledge.
8. **Target** — The opposing liquidity pool or opposing PD array that price is presumably being
   delivered toward. This is a *description of what the chart implies as a draw on liquidity*, not a
   trade recommendation — this skill stops at identifying the target, it does not build a trade plan
   around it.
## Timeframe-to-step mapping (for the `timeframe` tag on each item)
 
Most setups spread across D1 → H1 → M5 like this:
 
| Step | Usual timeframe |
|---|---|
| 1. HTF bias / dealing range | D1 |
| 2. Liquidity run | D1 or H1 |
| 3. Displacement | H1 or M5 |
| 4. FVG created | H1 or M5 |
| 5. MSS / CISD | H1 or M5 |
| 6. Entry (OTE / CE) | M5 |
| 7. Time / killzone | Whatever timeframe shows a time axis |
| 8. Target | Read against whichever timeframe shows the liquidity pool |
 
This is a *default expectation*, not a rule to force data into. If a chart clearly shows an MSS on
H1 in the image provided, tag it `"timeframe": "H1"` — don't relabel it "M5" just because entries are
usually M5-timeframe. And if no M5 image was provided at all, step 6 (Entry / OTE) simply cannot be
evaluated — leave `ote` fields null/false rather than inferring an M5-style entry from the H1 chart.