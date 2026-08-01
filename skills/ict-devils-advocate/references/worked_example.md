# Worked example — calibration reference

Calibrates depth, tagging, output length and the shape of the opposite case. Copy its rigour, not its
conclusions.

In Vietnamese with English ICT terms because that is the language the analysis was submitted in. Mirror
whatever you receive.

Three things to watch for: the **inverse case is built from a wick on the user's own D1 screenshot that
their narrative skipped**; a **drawn box is treated as a claim, not evidence**; and the verdict states
what the critique does *not* establish.

---

## Input

> NDX long, 2026-07-28. D1 bias bullish, giá đang làm HH. Dealing range D1 21,100–21,800, giá 21,620 →
> discount, nên long đúng phía range. H1 sweep sellside tại 21,580, displacement lên tạo FVG 21,600–21,640,
> CE 21,620. MSS H1 confirmed tại 21,660. Entry 21,620 (CE), SL 21,570, TP 21,800 (PDH), RR 1:5. Risk 1.5%
> account 10K. Setup trong London killzone.
> Kèm 1 screenshot D1, 1 screenshot H1 (có box và label do tôi vẽ).

---

## Output

```markdown
---
type: devils-advocate
instrument: NDX
date: 2026-07-28
timeframes_provided: [D1, H1]
verdict: BROKEN
opposite_case_strength: stronger
open_objections: 7
tags: [ict, devils-advocate, review]
---

# Devil's Advocate — NDX 2026-07-28

## 0. Evidence base

**Price action (`[CHART]`):** D1 — swing high 21,800, swing low 21,100, giá hiện tại 21,620; **wick 21,832
hai session trước, nến đó close 21,741**; equal lows 21,080–21,100 chưa bị chạm lại. H1 — swing low 21,580
bị xuyên tới 21,566, nến close 21,594; leg 21,566 → 21,668; ba nến tạo gap 21,602–21,638; tại 21,660 wick
lên 21,668, **nến break close 21,635**.

**USER-DRAWN (claim, không phải evidence):** box "H1 FVG 21,600–21,640"; label "MSS" tại 21,660; markers
entry/SL/TP. Box FVG bạn vẽ rộng hơn gap thật 21,602–21,638 — xem O5.

**Không có:** M5. Không có time axis đọc được trên cả hai ảnh.

## 1. Thesis + load-bearing claim

**Steelman:** NDX trong D1 uptrend; giá retrace về nửa rẻ của dealing range, quét sellside 21,580 lấy stop
late longs, displacement lên tạo H1 FVG sạch và shift structure tại 21,660; entry tại CE, target buyside
liquidity 21,800 — mua discount, bán vào liquidity đối diện.

**Premise ngầm bạn không viết:** 21,800 vẫn là liquidity chưa bị lấy. Không có nó thì step 8 không có draw.

**Load-bearing claim:** *"21,620 nằm ở discount của range 21,100–21,800, nên long đúng phía range."* Sai
claim này thì thesis sụp — không phải vì các mục sau sai, mà vì chúng thừa hưởng nó.

## 2. What survives

- **Có một liquidity event thật tại 21,580.** Wick 21,566 xuyên xuống dưới swing low rồi close ngược lên
  21,594 — sweep *được sử dụng*, không phải chỉ touch. `[CHART]`
- **Gap 21,602–21,638 là FVG thật**, ba nến không overlap, byproduct trực tiếp của leg 21,566 → 21,668.
  Đúng yêu cầu step 4. `[CHART]`
- **Entry đặt tại CE chứ không phải proximal edge** — đây là lỗi cũ của bạn, lần này làm đúng.
- **Nến reject tại 21,580 đã close trước entry.** Không phải hindsight.

## 3. Objections

**O1 · `[ARITHMETIC]` · load-bearing · fatal**
Claim: "21,620 là discount của range 21,100–21,800."
Evidence: (21,620 − 21,100)/(21,800 − 21,100) = **0.743**. Premium 74.3%, không gần equilibrium 21,450 đủ
để gọi vùng xám.
Consequence: bạn long từ nửa đắt của chính range bạn vẽ. Trụ chính của thesis không tồn tại. Không phải
diễn giải — số học trên đúng hai con số bạn cấp.
Retracted by: hai boundary swing khác + lý do vì sao *hai swing đó* mới là external range swings, nêu
trước khi biết giá nằm đâu trong range mới.

**O2 · `[CHART]` · load-bearing · fatal**
Claim: premise ngầm rằng 21,800 còn là buyside liquidity chưa bị lấy.
Evidence: trên chính ảnh D1 bạn gửi, 21,800 đã bị xuyên tới 21,832 hai session trước, nến đó close 21,741
— sweep đã xảy ra và đã bị reject.
Consequence: step 8 không có target; RR tính trên một mức không còn là liquidity. Wick 21,832 đứng ở phía
counter-case, không phía bạn.
Retracted by: một buyside pool khác còn nguyên ở trên 21,620, kèm lý do stop nằm ở đó.

**O3 · `[DOCTRINE]` · load-bearing**
Claim: "MSS H1 confirmed tại 21,660."
Fails: step 5 — MSS đòi body close vượt swing có ý nghĩa cấu trúc.
Evidence: `[CHART]` H1 — wick lên 21,668, nến break close **21,635**, quay về trong structure cũ. Thông
tin này đã có *trước* entry, nên đây là information failure chứ không phải hindsight — tin tốt, vì fixable
bằng checklist.
Consequence: không có MSS. Entry mất structural mandate; bạn mua retracement trong một H1 structure chưa
đổi trạng thái. Đúng lỗi tái phạm: counter-HTF entry thiếu H1 structural validation.
Retracted by: một H1 close trên 21,660, hoặc một swing khác được nêu là significant trên cơ sở độc lập với
việc nó đã bị phá.

**O4 · `[ARITHMETIC]`** — RR 1:5 khai cao hơn thực tế. 21,620/21,570/21,800 → risk 50, reward 180 =
**1:3.6**. Bạn đánh giá quyết định dựa trên phần thưởng lớn hơn 39% so với mức level của bạn cho phép.
Retracted by: TP thật hoặc SL thật.

**O5 · `[CHART]`** — Box FVG bạn vẽ là 21,600–21,640; gap thật theo ba nến là **21,602–21,638**. CE thật
21,620.0 (trùng với box, may mắn) nhưng edge lệch 2 điểm mỗi bên. Nhỏ ở đây, không nhỏ ở chỗ khác: mọi
phép tính CE, OTE band và R đều đo trên box chứ không trên nến, nên một box vẽ rộng là một lỗi số học
chạy âm thầm qua cả phân tích.
Retracted by: đo lại box theo high/low của ba nến.

**O6 · `[UNSUPPORTED]`** — "Setup trong London killzone." Không ảnh nào có time axis. Không phải sai — là
*không kiểm chứng được*, và là lỗi bạn lặp lại. Retracted by: screenshot có time axis + timezone của
chart, quy đổi sang giờ NY.

**O7 · `[UNSUPPORTED]`** — Toàn bộ step 6 ở tầng execution. Không có M5. Tôi không suy M5 từ H1 — và điều
này giới hạn *tôi* ngang với giới hạn bạn.

**O8 · `[SELF-CONTRADICTION]`** — Bạn gọi 21,580 là sellside liquidity bị quét *và* nói giá ở discount.
21,580 nằm ở 68.6% của range bạn vẽ — một internal low trong premium. Hai claim không cùng đúng.

Không liệt kê thêm các lỗi thừa hưởng từ O1: khi range sai thì mọi kết luận premium/discount phía dưới sai
theo, đếm ra không thêm thông tin.

## 4. Opposite case

**Inverse thesis:** NDX phân phối trong premium sau khi đã lấy xong buyside liquidity phía trên; draw thật
là sellside equal lows 21,080–21,100; gap 21,602–21,638 là nơi late longs được fill trước delivery xuống.

Cùng bộ fact, đổi vai trò: wick 21,832 là **sweep đỉnh đã hoàn thành**, không phải target phía trước. Leg
xuống từ 21,832 là displacement khởi đầu; leg 21,566 → 21,668 mà bạn gọi displacement là retracement bên
trong nó. Gap 21,602–21,638 nếu bị H1 close xuyên qua thì thành **inversion FVG** — support của bạn và
resistance của tôi là cùng một vùng. Wick-only tại 21,660 là internal grab thất bại, đúng nghĩa failure
swing. Target: equal lows 21,080–21,100, pool duy nhất trong evidence base còn nguyên.

**Strength: stronger** — đủ điều kiện cho nhãn này vì nó giải thích hai fact mà thesis của bạn phải bỏ
qua: wick 21,832 tồn tại, và nến break 21,660 close ngược vào trong.

**Observable phân định hai cách đọc:** một **H1 close dưới 21,602**. Có nó thì gap invert và inverse case
được xác nhận; chưa có thì đây là đọc mạnh hơn chứ không phải đọc đã xác nhận. Đây là mức duy nhất tách
được hai bên — mọi thứ khác trong mục này đều tương thích với cả hai.

## 5. Verdict

**BROKEN.**

Load-bearing claim thất bại độc lập trên `[ARITHMETIC]` (O1) và `[CHART]` (O2); mỗi lỗi tự nó đủ. O3 phá
thêm structural mandate của entry.

**Đã tấn công và không phá được:** tính hợp lệ của gap 21,602–21,638; sweep tại 21,580 thật sự bị reject
chứ không chỉ touch; entry đặt đúng CE thay vì proximal edge. Ba điểm này là process đang hoạt động.

**Điều gì làm tôi đổi ý:** O1 — một cặp boundary swing khác với lý do độc lập với vị trí giá hiện tại. O2 —
một buyside pool còn nguyên trên 21,620. O3 — một H1 close trên 21,660. Cả ba là fact kiểm chứng được;
gửi ảnh và tôi rút objection tương ứng ngay.

**Những gì phản biện này KHÔNG chứng minh:**
- Không chứng minh short là đúng, cũng không chứng minh lệnh long này sẽ thua. BROKEN nghĩa là *lập luận
  không đỡ được kết luận* — một lập luận sai vẫn có thể dẫn tới kết luận đúng.
- Không chứng minh inverse case sẽ xảy ra. Tôi dựng được một counter-case mạnh cho gần như mọi chart; sự
  tồn tại của nó gần như không mang thông tin. Chỉ mức 21,602 ở mục 4 mang thông tin.
- Chỉ dựa trên D1 + H1. Không có M5 và không có time axis, nên O6 và O7 là lỗ hổng bằng chứng của *cả hai*
  bên, không phải bằng chứng chống lại bạn.

## 6. Falsification tests

1. **Boundary sensitivity (O1).** 20 setup NDX gần nhất; mỗi setup vẽ dealing range hai lần — swing bạn
   chọn, và swing kế tiếp ra ngoài. Đếm số lần premium/discount đổi kết luận. **≥8/20 → boundary
   selection là biến số lớn nhất trong process, cần quy tắc viết trước.**
2. **Wick-only MSS (O3).** 30 trường hợp H1 "MSS" mà nến break close ngược vào trong. Đo bao nhiêu vẫn đi
   tiếp và đạt 1R trước khi phá ngược swing đó. **≥20/30 → O3 sai, tôi rút. ≤12/30 → body-close thành hard
   filter.**
3. **DOL đã bị lấy (O2).** 25 setup có pool target đã bị sweep trong 3 session trước, so với 25 setup pool
   còn nguyên. **Chênh lệch <10 điểm phần trăm → O2 yếu hơn tôi nghĩ, hạ xuống secondary.**

## 7. Action items

- [ ] Viết quy tắc chọn boundary dealing range D1 vào `CLAUDE.md` — quyết định trước, không phán đoán tại chỗ
- [ ] Recompute premium/discount cho 10 setup gần nhất trong journal, đối chiếu label đã ghi
- [ ] Thêm "DOL check: pool này đã bị sweep chưa? session nào?" vào pre-trade checklist
- [ ] Thêm hard filter "MSS chỉ tính khi có body close vượt swing" vào checklist H1
- [ ] Đo lại tất cả box FVG theo high/low của nến, không vẽ ước lượng
- [ ] Screenshot journal luôn có time axis + ghi timezone chart
- [ ] Chạy test 1 và 2; log kết quả và trạng thái O1/O3 vào `09 - Goal Tracking/02 - Skill Metrics.md`
```

---

## What to notice

- **Provenance is separated in section 0.** The drawn box goes under `USER-DRAWN`, and the discrepancy
  between box and candles becomes O5. Had the box been accepted as evidence, O5 would not exist.
- **Concession comes before attack** and includes credit for a fixed past error. That is what makes
  BROKEN land instead of reading as posturing.
- **Arithmetic and hindsight are tags, not sections.** O1/O4/O5 are `[ARITHMETIC]`; the hindsight check
  appears as one clause inside O3 and O7, reporting only what it found.
- **Depth is allocated by weight** — three deep objections on the central claim, five compact ones after,
  and an explicit refusal to pile on inherited errors.
- **The opposite case introduces zero new facts** and its strongest evidence is a wick on the user's own
  screenshot. `stronger` is earned by naming two facts the thesis cannot account for; without those it
  would have been `undecidable`.
- **The verdict says what it does not establish**, including that a coherent inverse case is cheap and
  that the missing M5 limits both sides equally.