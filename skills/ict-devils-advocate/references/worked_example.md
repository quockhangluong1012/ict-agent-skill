# Worked example — calibration reference

Calibrates depth, tagging, output length and the shape of the opposite case. Copy its rigour, not its
conclusions.

In Vietnamese with English ICT terms because that is the language the analysis was submitted in. Mirror
whatever you receive.

Five things to watch for, in rough order of how easy they are to get wrong:

- The response **leads with a procedure-level objection**, and that objection is pinned to named
  specifics rather than asserted in the abstract.
- **Severity and tier are independent.** O7 is `[CHART]` and `minor`; O1 is `[METHOD]` and `fatal`.
- The **inverse case is built from a wick on the user's own D1 screenshot** that their narrative skipped.
- A **drawn box is treated as a claim, not evidence.**
- The `--sensitivity` run **strengthens** an objection rather than weakening it, and the response says so.
  A tool that only ever confirms the attack is not being run honestly.

---

## Input

> NDX long, 2026-07-28. Lệnh đã đóng. D1 bias bullish, giá đang làm HH. Dealing range D1 21,100–21,800,
> giá 21,620 → discount, nên long đúng phía range. H1 sweep sellside tại 21,580, displacement lên tạo FVG
> 21,600–21,640, CE 21,620. MSS H1 confirmed tại 21,660. Entry 21,620 (CE), SL 21,570, TP 21,800 (PDH),
> RR 1:5. Risk 1.5% account 10K. Setup trong London killzone.
> Kèm 1 screenshot D1, 1 screenshot H1 (có box và label do tôi vẽ).

Mode is `REVIEW`: past tense, the trade is closed, and both charts extend past the decision candle.

---

## Output

```markdown
---
type: devils-advocate
mode: REVIEW
instrument: NDX
date: 2026-07-28
timeframes_provided: [D1, H1]
verdict: BROKEN
evidence_sufficiency: partial
opposite_case_strength: stronger
objections: {fatal: 3, material: 3, minor: 3}
open_objections: 9
tags: [ict, devils-advocate, review]
---

# Devil's Advocate — NDX 2026-07-28

## 0. Evidence base

**Mode:** REVIEW — lệnh đã đóng, cả hai ảnh kéo dài quá nến quyết định. Hindsight là lỗi chính tôi đi
tìm, và nó ràng buộc tôi ngang với bạn: mọi objection dưới đây phải đứng được nếu che phần bên phải.

**Price action (`[CHART]`):** D1 — swing high 21,800, swing low 21,100, giá hiện tại 21,620; **wick
21,832 hai session trước, nến đó close 21,741**; equal lows 21,080–21,100 chưa bị chạm lại. H1 — swing
low 21,580 bị xuyên tới 21,566, nến close 21,594; leg 21,566 → 21,668; ba nến tạo gap 21,602–21,638; tại
21,660 wick lên 21,668, **nến break close 21,635**.

**USER-DRAWN (claim, không phải evidence):** box "H1 FVG 21,600–21,640"; label "MSS" tại 21,660; markers
entry/SL/TP. Box FVG bạn vẽ rộng hơn gap thật 21,602–21,638 — xem O7.

**Không có:** M5. Không có time axis đọc được trên cả hai ảnh. Không có checklist/rule viết trước — tôi
đã hỏi; nếu có thì phần lớn phản biện mạnh nhất sẽ đến từ chỗ phân tích lệch khỏi rule của chính bạn chứ
không phải từ doctrine.

**Evidence sufficiency: `partial`.** Hai lỗ hổng — thiếu M5 và thiếu time axis — nhưng load-bearing claim
là một khẳng định premium/discount trên D1, đánh giá được đầy đủ từ range và giá có sẵn. Grade bám theo
claim trụ chứ không theo số lỗ hổng: hai gap mà vẫn để claim trung tâm kiểm được thì vẫn là `partial`,
không phải `thin`. Hệ quả: verdict được phép ở face value, nhưng O8 và O9 nằm trong đúng hai gap này nên
là `[UNSUPPORTED]` của cả hai phía — verdict sẽ nói lại.

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
- **Boundary của dealing range không phải chỗ yếu.** Xem O2 — sensitivity check đứng về phía bạn ở điểm
  này, kể cả khi kết luận rút ra từ nó thì không.

## 3. Objections

**O1 · `[METHOD]` · fatal · procedure**
Claim: toàn bộ quy trình — tám step được nêu như một chuỗi suy luận.
Fails: 0.1 và 0.2 — phân tích này không có điều kiện nào có thể ra "không vào lệnh", và 7/9 tham số của
model được chọn *trên* chart chứ không cố định *trước* chart.
Evidence: đọc lại chính đoạn bạn viết. "Displacement lên" — không có ngưỡng body size, nên không có giá
trị nào của nó có thể fail. "MSS confirmed" — chấp nhận trên một wick (O4), nghĩa là tiêu chí MSS cũng
không có ngưỡng vận hành. Range boundary, pool được quét, leg displacement, FVG nào, swing nào là
significant, pool nào là DOL, killzone nào: chín lựa chọn, không cái nào được bảo vệ bằng một rule có
trước. Hai thứ *có* ràng buộc là thứ tự D1→H1→M5 và yêu cầu body close cho MSS — và cái thứ hai đã không
được áp dụng.
Consequence: đây là lỗi sâu nhất trong danh sách vì nó sống sót qua mọi lần sửa các objection còn lại.
Sửa xong O2, O3, O4 thì bạn vẫn có một quy trình mà chart nào cũng cho ra một setup. Một model là một bộ
lọc; giá trị của nó nằm ở những setup nó *từ chối*. Phân tích này dùng từ vựng của model và bỏ chức năng.
Your best answer: "Tôi có loại setup, chỉ là không viết ra." Không cứu được — nhưng nó chuyển O1 từ
`fatal` xuống `material` ngay khi bạn đưa được một ghi chú pre-trade có timestamp cho thấy điều đó.
Retracted by: một rule viết trước chart này, nêu điều kiện quan sát được tại hard right edge mà chart
21,620 hôm đó có thể đã vi phạm. Một dòng là đủ, miễn là nó có trước.

**O2 · `[ARITHMETIC]` · fatal · load-bearing**
Claim: "21,620 là discount của range 21,100–21,800."
Evidence: (21,620 − 21,100)/(21,800 − 21,100) = **0.743**. Premium 74.3%, không gần equilibrium 21,450 đủ
để gọi vùng xám.
Consequence: bạn long từ nửa đắt của chính range bạn vẽ. Trụ chính của thesis không tồn tại. Không phải
diễn giải — số học trên đúng hai con số bạn cấp.
Your best answer: "Boundary tôi chọn sai, range thật khác." Đây là câu trả lời đúng hướng nhưng nó không
cứu được ở đây, và tôi đã kiểm tra trước khi viết: chạy `--sensitivity`, để 21,620 rơi khỏi premium phải
kéo D1 high lên 22,045 (+245, 35% span) hoặc kéo low lên 21,400 (+300, 43%). Trên ảnh D1 bạn gửi không có
swing nào ở hai chỗ đó. Kết luận premium bền vững với mọi boundary hợp lý trong evidence base — nên O2
không phải chuyện chọn boundary, và lần này sensitivity check đứng về phía tính chắc chắn của objection
chứ không phải chống lại nó.
Retracted by: một cặp boundary swing nhìn thấy được trên ảnh D1 đặt 21,620 xuống dưới 55%.

**O3 · `[CHART]` · fatal · load-bearing**
Claim: premise ngầm rằng 21,800 còn là buyside liquidity chưa bị lấy.
Evidence: trên chính ảnh D1 bạn gửi, 21,800 đã bị xuyên tới 21,832 hai session trước, nến đó close 21,741
— sweep đã xảy ra và đã bị reject. Phân tích không nhắc tới wick này một lần nào.
Consequence: step 8 không có target; RR tính trên một mức không còn là liquidity. Và phần im lặng quan
trọng ngang phần sai: wick 21,832 là fact dễ thấy nhất trên ảnh D1, nên việc nó vắng mặt trong writeup
nói rằng lần đọc chart này là một cuộc tìm setup, không phải một lần khảo sát chart. Điều đó hạ giá trị
của toàn bộ `[CHART]` support ở các mục khác.
Your best answer: "Tôi thấy nhưng cho rằng nó chưa đủ sâu để coi là sweep." Nếu đúng vậy thì đây là
documentation gap chứ không phải blind spot — nhưng nó vẫn không trả lại target cho step 8, vì một mức đã
bị xuyên 32 điểm và reject không còn là pool nguyên vẹn theo bất kỳ cách đọc nào.
Retracted by: một buyside pool khác còn nguyên ở trên 21,620, kèm lý do stop nằm ở đó.

**O4 · `[DOCTRINE]` · material**
Claim: "MSS H1 confirmed tại 21,660."
Fails: step 5 — MSS đòi body close vượt swing có ý nghĩa cấu trúc (xem Standard của Step 5 trong
`rebuttal_playbook.md`).
Evidence: `[CHART]` H1 — wick lên 21,668, nến break close **21,635**, quay về trong structure cũ. Thông
tin này đã có *trước* entry, nên đây là information failure chứ không phải hindsight — tin tốt, vì fixable
bằng checklist.
Consequence: không có MSS. Entry mất structural mandate; bạn mua retracement trong một H1 structure chưa
đổi trạng thái. Đúng lỗi tái phạm: counter-HTF entry thiếu H1 structural validation. Là `material` chứ
không `fatal` chỉ vì O2 và O3 đã giết thesis trước; nếu hai cái đó được rút thì O4 lên `fatal`.
Retracted by: một H1 close trên 21,660, hoặc một swing khác được nêu là significant trên cơ sở độc lập với
việc nó đã bị phá.

**O5 · `[SELF-CONTRADICTION]` · material**
Claim: "sweep sellside tại 21,580" *và* "giá ở discount", cùng một đoạn.
Evidence: 21,580 nằm ở 68.6% của range bạn vẽ. Một internal low trong nửa premium không phải sellside
liquidity của range đó.
Consequence: hai claim không cùng đúng, và bạn đang đếm cả hai là support. Dù giải quyết theo hướng nào
thì step 2 hoặc step 1 cũng mất một trụ.
Retracted by: chỉ ra pool 21,580 thuộc về range nào, nếu không phải range bạn đã nêu.

**O6 · `[ARITHMETIC]` · material**
Claim: RR 1:5.
Evidence: 21,620/21,570/21,800 → risk 50, reward 180 = **1:3.6**. Thêm spread+slippage 2.5 điểm thì còn
1:3.4.
Consequence: quyết định được đánh giá trên phần thưởng lớn hơn 39% so với mức level của bạn cho phép.
Ngoài scope severity budget vì risk arithmetic luôn được báo.
Retracted by: TP thật hoặc SL thật.

**O7 · `[CHART]` · minor** — Box FVG bạn vẽ là 21,600–21,640; gap thật theo ba nến là 21,602–21,638. CE
thật 21,620.0 trùng box (may mắn), edge lệch 2 điểm mỗi bên. Kết luận không đổi ở đây — nên `minor` —
nhưng mọi phép tính CE, OTE band và R đều đo trên box chứ không trên nến, nên một box vẽ rộng là lỗi số
học chạy âm thầm. Retracted by: đo lại theo high/low ba nến.

**O8 · `[UNSUPPORTED]` · minor** — "Setup trong London killzone." Không ảnh nào có time axis. Không phải
sai — là *không kiểm chứng được*, và là lỗi bạn lặp lại. Retracted by: screenshot có time axis + timezone
chart, quy đổi sang giờ NY.

**O9 · `[UNSUPPORTED]` · minor** — Toàn bộ step 6 ở tầng execution. Không có M5. Tôi không suy M5 từ H1 —
và điều này giới hạn *tôi* ngang với giới hạn bạn. Retracted by: ảnh M5 quanh thời điểm entry.

Không liệt kê thêm các lỗi thừa hưởng từ O2: khi range sai thì mọi kết luận premium/discount phía dưới sai
theo, đếm ra không thêm thông tin.

*Filter: draft 13 objection, ship 9, cắt 4. Hai cái không nêu được consequence (kích thước gap, cách đặt
tên leg). Một cái bị chính evidence base của bạn bác trước khi tôi gửi — tôi định tấn công chất lượng
displacement, nhưng leg 21,566 → 21,668 là 102 điểm trên một H1 mà 20 nến trước có body trung vị ~28
điểm, nên nó qua. Một cái là Part 0 không pin được vào instance cụ thể nào, đã chuyển xuống khối
`Hypotheses to check` cuối bài.*

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

**BROKEN.** Evidence sufficiency `partial`, và ở đây grade không cap verdict: BROKEN xoay trên O2 và O3,
cả hai đứng trên bằng chứng D1 có sẵn, nên hai gap (M5, axis) không chạm tới nó. Nếu verdict là
`SURVIVES THIS ATTACK` thì `partial` vẫn cho phép — chỉ `thin` mới hạ nó xuống `UNPROVEN`, và ở đây không
`thin` vì claim trụ kiểm được đầy đủ.

Load-bearing claim thất bại độc lập trên `[ARITHMETIC]` (O2) và `[CHART]` (O3); mỗi lỗi tự nó đủ. O1 là
lỗi nghiêm trọng nhất về dài hạn nhưng nó không tự mình phá thesis — nó nói rằng thesis chưa từng được đặt
vào thế có thể sai.

**Đã tấn công và không phá được:** tính hợp lệ của gap 21,602–21,638; sweep tại 21,580 thật sự bị reject
chứ không chỉ touch; entry đặt đúng CE thay vì proximal edge; chất lượng displacement (đo body, nó qua);
và boundary selection của dealing range, mà sensitivity check cho thấy là bền. Năm điểm này là process
đang hoạt động.

**Điều gì làm tôi đổi ý:** O2 — một cặp boundary swing nhìn thấy được đặt 21,620 dưới 55%. O3 — một buyside
pool còn nguyên trên 21,620. O4 — một H1 close trên 21,660. O1 — một ghi chú pre-trade có timestamp. Cả
bốn là fact kiểm chứng được; gửi ảnh và tôi rút objection tương ứng ngay.

**Những gì phản biện này KHÔNG chứng minh:**
- Không chứng minh short là đúng, cũng không chứng minh lệnh long này sẽ thua. BROKEN nghĩa là *lập luận
  không đỡ được kết luận* — một lập luận sai vẫn có thể dẫn tới kết luận đúng. Lệnh đã đóng, và kết quả
  của nó không nói gì về việc O1–O9 đúng hay sai theo cả hai chiều.
- Không chứng minh inverse case sẽ xảy ra. Tôi dựng được một counter-case mạnh cho gần như mọi chart; sự
  tồn tại của nó gần như không mang thông tin. Chỉ mức 21,602 ở mục 4 mang thông tin.
- Chỉ dựa trên D1 + H1. Không có M5 và không có time axis, nên O8 và O9 là lỗ hổng bằng chứng của *cả hai*
  bên, không phải bằng chứng chống lại bạn.

## 6. Falsification tests

1. **Điều kiện loại setup (đóng O1).** Viết rule pre-trade trước, rồi áp cho 20 setup NDX kế tiếp *trước
   khi* biết kết quả. Đếm bao nhiêu setup bị rule loại. **≥4/20 bị loại → rule có ràng buộc thật, O1 rút.
   0/20 → rule chỉ mô tả lại thứ bạn định làm, O1 giữ nguyên và đây là việc cần sửa trước mọi thứ khác.**
2. **Wick-only MSS (đóng O4).** 30 trường hợp H1 "MSS" mà nến break close ngược vào trong. Đo bao nhiêu
   vẫn đi tiếp và đạt 1R trước khi phá ngược swing đó. **≥20/30 → O4 sai, tôi rút. ≤12/30 → body-close
   thành hard filter.**
3. **DOL đã bị lấy (đóng O3).** 25 setup có pool target đã bị sweep trong 3 session trước, so với 25 setup
   pool còn nguyên. **Chênh lệch <10 điểm phần trăm → O3 yếu hơn tôi nghĩ, hạ xuống secondary.**

## 7. Action items

- [ ] Viết **một** điều kiện loại setup, dạng quan sát được tại hard right edge, vào `CLAUDE.md` trước
      phiên tiếp theo — đây là action item duy nhất mà mọi cái dưới đây phụ thuộc vào
- [ ] Viết quy tắc chọn boundary dealing range D1 — quyết định trước, không phán đoán tại chỗ
- [ ] Recompute premium/discount cho 10 setup gần nhất trong journal, đối chiếu label đã ghi
- [ ] Thêm "DOL check: pool này đã bị sweep chưa? session nào?" vào pre-trade checklist
- [ ] Thêm hard filter "MSS chỉ tính khi có body close vượt swing" vào checklist H1
- [ ] Đo lại tất cả box FVG theo high/low của nến, không vẽ ước lượng
- [ ] Screenshot journal luôn có time axis + ghi timezone chart
- [ ] Chạy test 1 và 2; log kết quả và trạng thái O1/O4 vào `09 - Goal Tracking/02 - Skill Metrics.md`

Hypotheses to check (not objections)

- Ba trong bốn setup gần nhất bạn gửi đều long từ nửa premium của range tự vẽ. Nếu đúng là một pattern
  thì nó lớn hơn O2 — nhưng tôi chỉ có một setup ở đây nên không tier được. Gửi journal thì kiểm tra được.
```

---

## What to notice

- **The procedure objection leads and is pinned.** O1 is not "your process is unfalsifiable" asserted in
  the abstract — that would fail the discharge test. It counts the fitted parameters, quotes two criteria
  that have no operative threshold, names the one rule that existed and was not applied, and states the
  single artefact that retracts it. Note also that it is `fatal` but explicitly *not* what broke the
  thesis; the verdict says which objection did which job.
- **Severity is allocated by consequence, not by tier.** O7 is `[CHART]` — the hardest evidence class
  available — and `minor`, because the conclusion is identical whether the box is right or wrong. O4 is
  demoted to `material` only because O2 and O3 got there first, and the response says so, which tells the
  user what happens to it if they successfully answer the other two.
- **The `minor` budget is exactly full at three**, and all three compress to one line with an inline
  `Retracted by:` and no labelled fields — the carve-out the format allows. Nothing else was let in. The
  risk arithmetic (O6) is exempt from the budget by rule and says so inline.
- **The pressure valve is used and quarantined.** The one hunch that could not be tiered sits below
  section 7, unnumbered, and is explicitly excluded from the verdict. The filter line says where it went,
  so the count still reconciles: 13 drafted = 9 shipped + 3 deleted + 1 relocated.
- **`Your best answer:` pre-empts rather than waits.** O2's best answer is the right instinct — challenge
  the boundaries — and the response has already run `--sensitivity` and found the instinct doesn't rescue
  it here. That is the difference between an attack and an argument.
- **Provenance is separated in section 0.** The drawn box goes under `USER-DRAWN`, and the discrepancy
  between box and candles becomes O7. Had the box been accepted as evidence, O7 would not exist.
- **Concession comes before attack** and includes credit for a fixed past error, plus two things the
  attack tried and failed on. That is what makes BROKEN land instead of reading as posturing.
- **The filter reports its own work.** Thirteen drafted, nine shipped, with the reason for each cut —
  including one objection abandoned because the evidence base defeated it. A response that cuts nothing
  did not run the filter, and the user has no way to tell unless it is stated.
- **The opposite case introduces zero new facts** and its strongest evidence is a wick on the user's own
  screenshot. `stronger` is earned by naming two facts the thesis cannot account for; without those it
  would have been `undecidable`.
- **The verdict says what it does not establish**, including that the closed trade's outcome is evidence
  about nothing here, that a coherent inverse case is cheap, and that the missing M5 limits both sides.
- **Evidence sufficiency is graded off the load-bearing claim, not a gap count.** Two gaps (no M5, no
  axis) would look like more than `partial` allows if you counted gaps — but the load-bearing claim is a
  D1 premium/discount assertion that O2 breaks on fully-present data, so the grade is `partial` and the
  verdict stands at face value. Had the load-bearing claim been the killzone or the M5 entry, the same two
  gaps would have forced `thin`, and a `SURVIVES THIS ATTACK` would have become `UNPROVEN`. The grade
  tracks whether the central claim is checkable, which is the only thing that decides how much a survival
  is worth.
- **Action items are ordered by dependency, not by objection number.** The single procedural fix comes
  first because the other seven are worth less until it exists.
