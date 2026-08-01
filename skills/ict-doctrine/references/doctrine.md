# ICT 2022 Doctrine Reference

Định nghĩa canon cho từng term, dùng để phán status. Với mỗi term có bốn phần:
**Định nghĩa** (canon là gì) · **Evidence bar** (được phép gọi tên này khi nào) ·
**Misuse phổ biến** (overcall / drift hay gặp) · **Ví dụ status** (một call mẫu).

Khi phán một claim, so nó với **Evidence bar**, không so với "cảm giác bullish/bearish".

## Mục lục
- [Cây quyết định status](#cây-quyết-định-status)
- [Hard right edge & Hindsight](#hard-right-edge--hindsight) ← nguyên tắc gốc
- [Dealing range · Premium/Discount · Equilibrium](#dealing-range--premiumdiscount--equilibrium)
- [Liquidity (các loại)](#liquidity-các-loại)
- [Sweep / Liquidity run / Judas swing](#sweep--liquidity-run--judas-swing)
- [Displacement](#displacement)
- [FVG & CE (consequent encroachment)](#fvg--ce)
- [Inversion FVG (IFVG)](#inversion-fvg-ifvg)
- [MSS (Market Structure Shift)](#mss-market-structure-shift)
- [BOS (Break of Structure)](#bos-break-of-structure)
- [BOS vs MSS — bảng phân biệt](#bos-vs-mss)
- [CISD (Change in State of Delivery)](#cisd-change-in-state-of-delivery)
- [Order Block (OB)](#order-block-ob)
- [Breaker](#breaker)
- [OTE (Optimal Trade Entry)](#ote-optimal-trade-entry)
- [Killzone / Time](#killzone--time)
- [Target / Draw on liquidity](#target--draw-on-liquidity)

---

## Cây quyết định status

Chạy lần lượt cho mỗi claim:

1. Claim gọi *sai tên* hiện tượng, hoặc mâu thuẫn arithmetic/structure? → **FAIL**.
2. Nếu tên đúng: có đủ evidence bắt buộc của term đó *tại điểm quyết định* không?
   - Không có evidence bắt buộc → **UNSUPPORTED**.
   - Có nhưng mờ / thiếu timeframe / không đọc được → **AMBIGUOUS**.
   - Có, rõ, nhưng chỉ đúng nhờ nến *sau* điểm quyết định → **HINDSIGHT**.
   - Có, rõ, đứng vững tại điểm quyết định → **PASS**.

Lưu ý: FAIL nói về *định nghĩa*. UNSUPPORTED/AMBIGUOUS nói về *bằng chứng*. HINDSIGHT nói về *thời điểm* của bằng chứng. Đừng trộn ba trục này.

---

## Hard right edge & Hindsight

Đây là nguyên tắc gốc, đọc trước mọi thứ khác.

**Hard right edge** = nến/điểm mà quyết định được đưa ra trong thực tế. Trong backtest, đó là cây nến cuối cùng người phân tích "được phép nhìn thấy" trước khi vào lệnh. Mọi thứ bên phải nó là *tương lai chưa biết*.

**Doctrine:** một claim chỉ hợp lệ nếu nó dựng được **chỉ bằng thông tin tính đến hard right edge**. Nếu lý lẽ cần tới một cây nến hình thành *sau* điểm quyết định để đúng, đó là **HINDSIGHT** — kể cả khi kết luận cuối cùng trùng với hướng giá thật sự đi.

**Dấu hiệu hindsight hay gặp:**
- "Đây rõ ràng là sweep vì sau đó giá đảo chiều mạnh." → cái "sau đó" là nến tương lai. Tại điểm quyết định, sweep chưa được *xác nhận* bởi phản ứng chưa xảy ra.
- "FVG này giữ giá nên nó là điểm entry chuẩn." → nếu "giữ giá" là quan sát sau khi giá đã test và bật, đó là hindsight về tính hợp lệ của entry.
- "MSS xác nhận vì trend sau đó tiếp diễn." → MSS phải đọc được tại nến phá structure, không phải xác nhận bằng diễn biến sau.

**Cách sửa (remediation):** yêu cầu người dùng phát biểu lại claim ở dạng "*tại nến X, thông tin có được là...*", tách bạch cái quan sát-được-lúc-đó với cái chỉ biết-sau-này. Nếu claim sụp khi bỏ thông tin tương lai → HINDSIGHT.

Phân biệt với **outcome bias**: thesis đúng hướng ≠ thesis đúng doctrine. Một call có thể PASS doctrine mà giá vẫn đi ngược (setup hợp lệ vẫn thua), và một call HINDSIGHT vẫn có thể "thắng". Validator chấm *tính hợp lệ tại điểm quyết định*, không chấm outcome.

---

## Dealing range · Premium/Discount · Equilibrium

**Định nghĩa.** Dealing range = một leg swing hoàn chỉnh, từ một swing high tới một swing low (hoặc ngược lại) mà thị trường đang giao dịch bên trong. Equilibrium = midpoint 50% của range đó. Trên EQ = **premium**, dưới EQ = **discount**.

**Evidence bar.** (a) Range phải là một leg *xác định được* bằng hai swing point rõ, nhất quán với timeframe của thesis. (b) Trạng thái premium/discount phải tính từ **giá hiện tại so với midpoint**, không phải cảm giác. Midpoint = (high + low) / 2.

**Misuse phổ biến.**
- *Range selection tùy tiện:* chọn high/low cho khớp kết luận mong muốn. Nếu đổi range thì premium/discount lật — đây là red flag.
- *Sai arithmetic:* nói "discount" trong khi giá thực ra trên midpoint. Đây là **FAIL arithmetic**, kiểm được bằng phép tính.
- *Trộn timeframe:* lấy range D1 rồi phán premium/discount cho một entry M5 mà không nói rõ đang chiếu range nào.

**Ví dụ status.** "Giá ở discount của range 1.0850–1.0950, hiện 1.0880." → midpoint 1.0900; 1.0880 < 1.0900 → đúng discount → **PASS**. Nếu người dùng nói discount nhưng giá là 1.0920 → **FAIL** (arithmetic).

---

## Liquidity (các loại)

**Định nghĩa.** Vùng tập trung stop/pending orders mà thị trường có xu hướng tìm đến. Các pool có tên chuẩn:
- **BSL/SSL** — buy-side (trên các high) / sell-side (dưới các low) liquidity.
- **PDH/PDL, PWH/PWL** — previous day/week high/low.
- **EQH/EQL** — equal highs/lows (đôi/cụm đỉnh-đáy bằng nhau).
- **Session highs/lows**, **trendline liquidity** (stops dọc một trendline).

**Evidence bar.** Để nói "có liquidity ở đây", phải chỉ được *loại pool có tên* và *level cụ thể*. "Có liquidity phía trên" chung chung mà không neo vào pool nào → UNSUPPORTED.

**Misuse phổ biến.** Gọi mọi swing high/low là "liquidity" mà không phân biệt pool nào đáng kể (PDH/EQH) với noise. Doctrine drift khi "liquidity" trở thành nhãn dán cho bất kỳ điểm nào.

---

## Sweep / Liquidity run / Judas swing

**Định nghĩa.** Sweep = giá *chạy qua* một pool liquidity có tên để lấy stops, rồi *bị từ chối* (reject) khỏi vùng đó. Judas swing = cú sweep đánh lừa (thường đầu session) đi ngược hướng thật sự trước khi move thật diễn ra.

**Evidence bar.** Ba điều: (a) có *level liquidity có tên* bị quét, (b) giá *xuyên qua* level đó (không chỉ chạm), (c) có *rejection* — sweep được *dùng*, không chỉ touched. Wick thò qua level một mình chưa đủ nếu không có phản ứng từ chối.

**Misuse phổ biến.**
- Gọi "sweep" mà không nêu pool nào bị quét → **UNSUPPORTED**.
- Gọi một cú *break-and-continue* (giá phá qua rồi đi tiếp, không reject) là sweep → **FAIL** (đó không phải sweep, có thể là break/expansion).
- Xác nhận rejection bằng nến *sau* điểm quyết định → **HINDSIGHT**.

**Ví dụ status.** "Sweep EQH tại 1.2050 rồi reject." Nếu chart cho thấy wick xuyên 1.2050 và nến đóng cửa lại dưới → **PASS**. Nếu chỉ nói "quét liquidity phía trên" không level → **UNSUPPORTED**.

---

## Displacement

**Định nghĩa.** Một expansion *một chiều, năng lượng cao* rời khỏi một điểm (thường sau sweep), để lại imbalance phía sau. Đây là "dấu vân tay" của việc smart money đang delivery giá.

**Evidence bar.** Nhìn *body size và tốc độ* tương đối với structure liền trước: nến thân lớn, ít overlap, đi nhanh. Displacement thường *là* thứ tạo ra FVG và *xác nhận* MSS.

**Misuse phổ biến.** Gọi một move *lệt bệt, overlapping, chậm* là displacement chỉ vì nó đúng hướng. Đúng hướng ≠ displacement. Nếu không có displacement thì FVG "kèm theo" và MSS "kèm theo" cũng đáng nghi.

**Ví dụ status.** Chuỗi 3 nến thân lớn cùng chiều, gần như không râu ngược, phá qua swing → displacement hợp lệ → yếu tố PASS cho FVG/MSS đi kèm. Move răng cưa 8 nến nhích dần → **FAIL** nếu bị gọi displacement.

---

## FVG & CE

**Định nghĩa.** FVG (Fair Value Gap) = vùng imbalance 3 nến: khoảng hở giữa râu nến 1 và râu nến 3 mà nến 2 (displacement) để lại. **CE** (consequent encroachment) = midpoint 50% của gap đó.

**Evidence bar.** (a) Phải là sản phẩm *trực tiếp* của một displacement leg (xem Displacement). (b) Là imbalance thật theo cấu trúc 3 nến, không phải một khoảng trống bất kỳ. (c) Kiểm *đã bị fill trước đó chưa* — một FVG đã bị lấp không còn là gap "tươi".

**Misuse phổ biến.**
- Gọi FVG cho một gap không sinh ra từ displacement leg → **FAIL**.
- Kể lại FVG *sau khi* giá đã test và phản ứng, trình bày như thể nó hiển nhiên là điểm entry tại thời điểm quyết định → **HINDSIGHT**.
- Bỏ qua việc gap đã bị fill → claim về "FVG chưa test" thành sai fact.

**Ví dụ status.** "Displacement H1 để lại FVG 1.1000–1.1015, CE 1.10075." Nếu displacement rõ và gap chưa fill → **PASS**. Nếu gap này thực ra là khoảng giữa hai nến overlap không displacement → **FAIL**.

---

## Inversion FVG (IFVG)

**Định nghĩa.** Một FVG *bị close xuyên qua* (bị vi phạm) và sau đó đảo cực, hoạt động như support/resistance chiều ngược lại.

**Evidence bar.** Bắt buộc phải có sự kiện *close xuyên qua FVG cũ* xảy ra rồi. IFVG là một trạng thái *sau vi phạm* — không tồn tại trước khi FVG bị close phá.

**Misuse phổ biến.** Gọi một FVG bình thường (chưa bị vi phạm) là IFVG → **FAIL**. Gán nhãn IFVG dựa trên diễn biến tương lai → **HINDSIGHT**. Đây là term rất dễ overcall.

---

## MSS (Market Structure Shift)

**Định nghĩa.** Tín hiệu *đảo chiều*: giá phá một swing point *ngược* với short-term move liền trước, thường *sau* một sweep và *bằng* displacement. Báo hiệu khả năng đổi hướng delivery.

**Evidence bar.** (a) Có một swing point *tồn tại từ trước* bị phá. (b) Phá bằng **body close** vượt qua, không chỉ wick. (c) Hướng phá *ngược* short-term move trước đó. (d) Lý tưởng: đi kèm displacement (và thường sau sweep). Thiếu displacement → ít nhất là AMBIGUOUS, dễ thành overcall.

**Misuse phổ biến.**
- Gọi một swing nhỏ trong internal noise là MSS → **FAIL** (overcall): không phá structure có ý nghĩa.
- Gọi một *continuation break* (phá thuận trend) là MSS → **FAIL**: đó là BOS, không phải MSS.
- Wick xuyên nhưng không body close → chưa đủ → **UNSUPPORTED**/AMBIGUOUS.

**Ví dụ status.** Sau khi sweep SSL, giá close thân lên phá swing high gần nhất bằng nến displacement → MSS bullish → **PASS**. Một wick chọc qua swing rồi đóng lại dưới → **FAIL** nếu bị gọi MSS.

---

## BOS (Break of Structure)

**Định nghĩa.** *Continuation*: giá phá một swing point *thuận* hướng trend đang chạy, xác nhận trend tiếp diễn.

**Evidence bar.** (a) Có trend/structure *đã tồn tại trước*. (b) Phá swing point bằng **body close** theo hướng trend. Chỉ sweep/stop run mà không có structural break đúng nghĩa → không được gọi BOS.

**Misuse phổ biến.**
- Gọi BOS cho một sweep (giá quét rồi reject, không tiếp diễn) → **FAIL**.
- Dùng BOS và MSS lẫn lộn (xem bảng dưới).
- Wick phá, không body close → **UNSUPPORTED**.

**Ví dụ status.** Trong uptrend, giá close thân trên higher high trước → **PASS** (BOS continuation). Nếu đó là cú phá *ngược* short-term move sau sweep → gọi BOS là **FAIL** (đó là MSS).

---

## BOS vs MSS

Lỗi lẫn lộn phổ biến nhất. Trục phân biệt là **hướng so với move liền trước** và **ý nghĩa**:

| | BOS | MSS |
|---|---|---|
| Bản chất | Continuation | Reversal / shift |
| Hướng phá | *Thuận* trend/short-term move | *Ngược* short-term move |
| Bối cảnh điển hình | Giữa một trend đang chạy | *Sau* sweep liquidity |
| Yêu cầu displacement | Không bắt buộc | Rất nên có (thường bắt buộc trên execution TF) |
| Xác nhận | Body close phá swing thuận hướng | Body close phá swing ngược hướng |
| Ý nghĩa | Trend còn tiếp | Có thể đổi hướng delivery |

Nếu một claim mô tả "phá ngược sau sweep" nhưng gọi là BOS → **FAIL**. Nếu mô tả "phá thuận trend đang chạy" nhưng gọi MSS → **FAIL**.

---

## CISD (Change in State of Delivery)

**Định nghĩa.** Dấu hiệu delivery đổi chiều ở mức granular: giá *close ngược* qua open của chuỗi nến cùng màu liền trước (hoặc qua open của nến/chuỗi displacement) đã đẩy giá theo chiều cũ. Thường dùng ở execution level, mịn hơn MSS.

**Evidence bar.** Chỉ được *reference candle/chuỗi* mà state đang đổi so với nó, và có *close* xuyên qua open reference đó. Không neo được vào chuỗi nào → UNSUPPORTED.

**Misuse phổ biến.** Dùng "CISD" như từ đồng nghĩa tùy tiện của MSS mà không chỉ ra chuỗi nến reference và close point cụ thể → doctrine drift. CISD và MSS *liên quan* nhưng không thay thế nhau vô điều kiện.

---

## Order Block (OB)

**Định nghĩa.** Nến *gốc* của move tạo imbalance và phá structure — thường là nến down-close cuối cùng trước một up-displacement (bullish OB) hoặc up-close cuối trước down-displacement (bearish OB), là origin của cú move đã lấy liquidity / phá structure.

**Evidence bar.** Phải nhất quán với một *rule cụ thể* người dùng đang dùng, và gắn với move có displacement + break/sweep. Một OB "trơ" không sinh ra displacement hay không phá gì thì đáng nghi.

**Misuse phổ biến.** Gọi *mọi nến ngược chiều* là OB → **doctrine drift** kinh điển. Nếu user dán nhãn OB cho hàng loạt nến không phân biệt, flag drift và yêu cầu về đúng một định nghĩa.

**Ví dụ status.** Nến down-close cuối ngay trước chuỗi displacement phá swing + lấy liquidity → bullish OB hợp lệ → **PASS**. Một nến đỏ ngẫu nhiên giữa range gọi OB → **FAIL**.

---

## Breaker

**Định nghĩa.** Một order block *thất bại*: sau khi giá lấy liquidity và phá structure ngược lại, OB cũ đảo cực và trở thành vùng breaker chiều ngược.

**Evidence bar.** Cần *chuỗi sự kiện* đầy đủ: (a) OB hình thành, (b) liquidity bị lấy, (c) structure bị phá ngược, (d) OB cũ giờ đóng vai kháng/hỗ trợ ngược cực. Thiếu một mắt xích → chưa phải breaker.

**Misuse phổ biến.** Gọi breaker chỉ từ một nến đơn hoặc thiếu bước phá structure → **FAIL**. Gán breaker bằng diễn biến tương lai → **HINDSIGHT**.

---

## OTE (Optimal Trade Entry)

**Định nghĩa.** Vùng retrace **0.62–0.79** của một impulse leg (CE ~**0.705**; nhiều người dùng bộ 0.618 / 0.705 / 0.786). Là vùng entry ưa thích khi giá hồi về sau displacement.

**Evidence bar.** (a) Phải có một *impulse leg xác định được* để kéo Fib. (b) Mức phải tính đúng theo hai đầu leg. Đọc trên timeframe thực thi (thường M5 khi có). Không có leg rõ → UNSUPPORTED. Sai số học mức Fib → FAIL arithmetic.

**Misuse phổ biến.** Kéo Fib từ một leg tùy chọn cho khớp entry mong muốn. Gọi vùng 0.5 là OTE (OTE bắt đầu ~0.62). Backfill OTE cho một entry M5 từ chart H1 khi không có M5 → fabrication.

---

## Killzone / Time

**Định nghĩa.** Cửa sổ thời gian ICT: London (02:00–05:00 giờ NY), NY AM (07:00–10:00), Silver Bullet (10:00–11:00), NY PM (13:30–16:00), cùng các macro window.

**Evidence bar.** Chỉ mark killzone từ *trục thời gian nhìn thấy được* trên chart hoặc *giờ người dùng nêu rõ*. Suy ra session từ kiến thức giờ thị trường chung, không có trục thời gian → **UNSUPPORTED**.

**Misuse phổ biến.** "Đây là London killzone" mà chart không hiện giờ nào → UNSUPPORTED. Chuyển đổi múi giờ ngầm rồi kết luận session → dễ sai; yêu cầu nêu timezone của chart.

---

## Target / Draw on liquidity

**Định nghĩa.** Pool liquidity đối diện hoặc PD array đối diện mà giá *có vẻ đang được kéo về* (draw on liquidity). Đây là *mô tả* điều chart hàm ý, không phải khuyến nghị.

**Evidence bar.** Phải chỉ được pool/array đối diện *có tên* làm draw. 

**Misuse phổ biến — và lằn ranh vai trò:** biến "target" thành khuyến nghị trade ("target 1.2100, vào lệnh"). Validator *chỉ* xác nhận draw on liquidity có được nêu đúng không; **không** đưa entry/stop/target như một kèo. Nếu claim của user trượt sang kèo, đó là lúc kéo về đúng vai và (nếu cần) từ chối phần coaching.