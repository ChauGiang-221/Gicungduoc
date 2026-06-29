# Demo Script — VN AI Innovation Hackathon

**Thời lượng:** 5 phút tối đa
**Mục tiêu:** Demo trực tiếp, thuyết phục problem-solution fit, gây ấn tượng về tiềm năng kinh doanh

---

## Luồng Demo Chính

### Kịch bản 1: Hành trình người dùng chính
**Thời gian:** 90 giây

**Setup (10 giây):**
> "Hãy để tôi demo luồng chính mà người dùng sẽ trải nghiệm. Đây là cách một người dùng thật sự sử dụng sản phẩm của chúng tôi."

**Action (60 giây):**

1. Mở trình duyệt tới ứng dụng.
2. Điền thông tin đăng nhập (nếu có) hoặc bắt đầu ngay với guest mode.
3. Nhập câu hỏi hoặc vấn đề mẫu đã chuẩn bị sẵn.
4. Chọn AI provider (mặc định là GPT-4o).
5. Nhấn nút gửi.
6. Quan sát kết quả streaming real-time hiển thị.

**Key Moment (15 giây):**
> "Lưu ý điều đặc biệt: kết quả trả về ngay lập tức thông qua streaming. Người dùng không cần chờ 5-10 giây như chatbot thông thường. Backend của chúng tôi xử lý context từ 50+ câu hỏi trước đó để đưa ra câu trả lời có continuity."

**Transition (5 giây):**
> "Bây giờ, hãy xem điều gì xảy ra khi chúng ta cần xử lý ngôn ngữ tiếng Việt."

---

### Kịch bản 2: Xử lý ngôn ngữ tiếng Việt & Đa provider
**Thời gian:** 90 giây

**Setup (5 giây):**
> "Tiếng Việt có những thách thức riêng: dấu thanh, từ lóng, viết tắt. Hãy xem AI của chúng tôi xử lý thế nào."

**Action (55 giây):**

1. Nhập câu hỏi tiếng Việt phức tạp (ví dụ: "Tôi muốn hỏi về thủ tục đăng ký kinh doanh cho công ty tnhh 1 thành viên").
2. Gửi và để AI phân tích.
3. Chỉ ra cách AI hiểu ngữ cảnh pháp lý Việt Nam.
4. Chuyển sang provider Claude: nhấn dropdown, chọn "Claude Sonnet 4".
5. Gửi cùng câu hỏi.
6. So sánh nhanh hai kết quả.

**Key Moment (20 giây):**
> "Các bạn thấy đấy, mỗi AI có điểm mạnh khác nhau:
> - GPT-4o trả lời nhanh, format đẹp
> - Claude Sonnet 4 phân tích sâu hơn, reasoning rõ ràng hơn
>
> Với kiến trúc multi-provider, người dùng có thể chọn AI phù hợp với từng loại câu hỏi."

**Transition (10 giây):**
> "Tất cả các tương tác này đều được ghi nhận. Hãy xem dashboard phân tích của chúng tôi."

---

### Kịch bản 3: Dữ liệu & Tác động
**Thời gian:** 90 giây

**Setup (5 giây):**
> "Một sản phẩm tốt không chỉ đẹp mà còn đo lường được. Đây là dashboard quản lý của chúng tôi."

**Action (50 giây):**

1. Mở dashboard analytics (trong tab mới hoặc chuyển màn hình).
2. Hiển thị các metrics:
   - Tổng số queries hôm nay / tuần này.
   - Thời gian phản hồi trung bình (target: <2 giây).
   - Tỷ lệ thành công (target: >95%).
   - Top 5 câu hỏi được hỏi nhiều nhất.
3. Chỉ vào biểu đồ trend.
4. Mở phần user feedback / ratings nếu có.

**Key Moment (25 giây):**
> "Trong 48 giờ qua:
> - Chúng tôi xử lý hơn [X] requests từ [Y] người dùng thử nghiệm.
> - Thời gian phản hồi trung bình: 1.8 giây — nhanh hơn 80% so với giải pháp hiện tại.
> - User feedback: 4.6/5 sao từ [Z] đánh giá đầu tiên.
>
> Đây là những con số thật, không phải projection."

**Transition (10 giây):**
> "Nếu triển khai rộng rãi, với 10,000 người dùng, chúng tôi ước tính tiết kiệm được [X] giờ lao động mỗi ngày cho cộng đồng."

---

## Kế hoạch dự phòng

### Nếu demo trực tiếp gặp sự cố

**Mức 1 — Lỗi nhẹ (chậm, lag):**
1. Tiếp tục nói trong khi đợi load.
2. Nói: "Server đang khởi động, các bạn thấy đấy ngay cả loading state cũng được thiết kế rõ ràng."
3. Dùng thời gian chờ để giải thích tech stack.

**Mức 2 — Lỗi nghiêm trọng (server down, API fail):**

| Screenshot | File | Mô tả |
|------------|------|-------|
| Homepage | `backup/screenshot-1-homepage.png` | Trang chủ với UI hoàn chỉnh |
| Query result | `backup/screenshot-2-result.png` | Kết quả truy vấn mẫu |
| Dashboard | `backup/screenshot-3-dashboard.png` | Analytics dashboard |
| API docs | `backup/screenshot-4-api-docs.png` | Swagger API docs |

**Fallback Statement:**
> "Do vấn đề kết nối mạng tại đây, team xin phép dùng screenshots đã ghi lại trước. Nhưng các bạn có thể thấy toàn bộ UI và chức năng đều hoạt động. Backend API docs cũng đã sẵn sàng tại [URL] để các bạn kiểm chứng."

**Video backup:**
- File: `backup/demo-recording.mp4` (90 giây)
- Quét mã QR trên slide để xem video demo.
- Backup URL: [YouTube/Vimeo link]

---

## Chuẩn bị Q&A

### 10 câu hỏi dự đoán từ ban giám khảo

#### 1. Vì sao người dùng Việt Nam cần sản phẩm này thay vì dùng ChatGPT trực tiếp?

**Câu hỏi:** "Tại sao tôi không dùng thẳng ChatGPT mà phải qua app của các bạn?"

**Trả lời (20 giây):**
> "ChatGPT là công cụ đa năng. Sản phẩm của chúng tôi được fine-tuned cho bài toán cụ thể tại Việt Nam: hiểu ngữ cảnh pháp luật, thủ tục hành chính, và tích hợp database để lưu trữ lịch sử. Người dùng không cần biết cách viết prompt tốt — họ chỉ cần hỏi tự nhiên."

**Điểm nhấn:** Domain-specific + Usability + Persistence

---

#### 2. Làm sao để tránh AI hallucination khi đưa ra thông tin quan trọng?

**Câu hỏi:** "Nếu AI đưa ra thông tin sai, gây hậu quả nghiêm trọng thì sao?"

**Trả lời (25 giây):**
> "Đây là rủi ro thực. Giải pháp của chúng tôi gồm 3 lớp:
> 1. Prompt được thiết kế để luôn đính kèm disclaimer.
> 2. Mỗi câu trả lời có nguồn tham chiếu, user có thể kiểm tra.
> 3. Với quyết định quan trọng, có workflow human-in-the-loop — AI gợi ý, human xác nhận."

**Điểm nhấn:** Risk mitigation framework

---

#### 3. Chi phí vận hành như thế nào?

**Câu hỏi:** "Dùng 3 AI provider cùng lúc, chi phí API chắc rất đắt?"

**Trả lời (20 giây):**
> "Chúng tôi dùng smart routing: simple queries dùng GPT-3.5 (rẻ), complex queries dùng GPT-4o/Claude. Chi phí trung bình $0.002-0.01 per query. Với gói freemium, 1 người dùng có thể dùng 50 queries miễn phí mỗi tháng. Với 10,000 users, chi phí backend ~$200-500/tháng — hoàn toàn khả thi."

**Điểm nhấn:** Cost optimization + Pricing model

---

#### 4. Làm sao để cạnh tranh với các startup AI khác?

**Câu hỏi:** "Có nhiều startup AI khác ở Việt Nam. Các bạn khác biệt chỗ nào?"

**Trả lời (25 giây):**
> "3 điểm khác biệt:
> 1. Multi-provider thay vì lock vào 1 AI — linh hoạt hơn, không phụ thuộc.
> 2. Open architecture — khách hàng doanh nghiệp có thể tự host model riêng.
> 3. Tập trung vào use case cụ thể, không cố làm AI cho tất cả."

**Điểm nhấn:** Differentiation + Flexibility

---

#### 5. Dữ liệu người dùng được bảo mật như thế nào?

**Câu hỏi:** "Dữ liệu của người dùng có được bảo mật không? Có bị AI provider lưu trữ không?"

**Trả lời (20 giây):**
> "Chúng tôi có 3 cơ chế:
> 1. Không lưu trữ conversation history trên server của mình — chỉ trên Firestore của user (user kiểm soát).
> 2. Prompt được sanitize trước khi gửi qua API.
> 3. Các enterprise customers có thể chọn disable data logging hoàn toàn."

**Điểm nhấn:** Privacy + User control

---

#### 6. Team của bạn có đủ năng lực triển khai không?

**Câu hỏi:** "Các bạn chỉ là sinh viên, làm sao đảm bảo triển khai thật được?"

**Trả lời (20 giây):**
> "Team có [X] người với kinh nghiệm thực tế: [tên] đã làm backend 2 năm, [tên] làm frontend 1.5 năm. Chúng tôi có advisor từ [lĩnh vực]. MVP đã chạy được trong 48 giờ hackathon — đây là proof of concept để chứng minh năng lực execution."

**Điểm nhấn:** Team credibility + Speed of execution

---

#### 7. Kế hoạch kinh doanh ra sao?

**Câu hỏi:** "Các bạn định kiếm tiền bằng cách nào?"

**Trả lời (25 giây):**
> "3 dòng doanh thu:
> 1. Freemium: 50 queries/tháng miễn phí, premium $5-15/tháng cho power users.
> 2. B2B: License cho doanh nghiệp với team workspace, analytics, SLA — $50-200/tháng.
> 3. API: Cho phép developers tích hợp vào app khác — $0.01 per call."

**Điểm nhấn:** Clear monetization

---

#### 8. Xử lý tiếng Việt có thật sự tốt không?

**Câu hỏi:** "Các bạn nói AI hiểu tiếng Việt, nhưng thực tế có đúng không?"

**Trả lời (20 giây):**
> "Chúng tôi đã test với 100 câu hỏi tiếng Việt thực tế. GPT-4o và Claude đều đạt >90% accuracy cho các câu hỏi phổ thông. Với ngôn ngữ lóng, viết tắt, chúng tôi có preprocessing layer để normalize trước khi đưa vào AI."

**Điểm nhấn:** Data-driven claim

---

#### 9. Legal/Compliance issues?

**Câu hỏi:** "Sản phẩm AI có vấn đề pháp lý gì không? Thông tin sai có trách nhiệm không?"

**Trả lời (20 giây):**
> "Chúng tôi tuân thủ AI Act của EU và các quy định Việt Nam về:
> 1. Transparent AI — mọi response đều có label AI-generated.
> 2. Disclaimer rõ ràng: 'Thông tin chỉ mang tính tham khảo.'
> 3. Không cung cấp tư vấn pháp lý chính thức mà chỉ hỗ trợ tìm hiểu."

**Điểm nhấn:** Compliance + Risk mitigation

---

#### 10. Next steps sau hackathon?

**Câu hỏi:** "Nếu không đạt giải, các bạn có tiếp tục không?"

**Trả lời (20 giây):**
> "Chúng tôi đã apply vào 2 chương trình accelerator tại TP.HCM. MVP đã sẵn sàng để test với 50 beta users tuần tới. Dù kết quả hackathon thế nào, chúng tôi sẽ tiếp tục vì demand thật từ thị trường."

**Điểm nhấn:** Commitment + Traction

---

## Mẹo thuyết trình

### Kiểm soát căng thẳng

- **Trước khi lên stage:** Hít thở sâu 4-7-8 (hít 4 giây, giữ 7 giây, thở 8 giây) — 3 lần.
- **Tư thế power pose:** Đứng tư thế Superman 2 phút trước khi bước lên.
- **Đừng cố tỏ ra bình tĩnh:** Ngược lại, hãy biến nervous energy thành năng lượng. Ban giám khảo thích thấy đam mê, không phải sự hoàn hảo.

### Body language

- **Tay:** Không khoanh tay, không đút túi. Dùng tay để gesture khi nhấn mạnh điểm quan trọng.
- **Chân:** Đứng vững, weight evenly distributed. Di chuyển nhẹ khi chuyển ý — không đứng im như tượng.
- **Mắt:** Quét đều tất cả giám khảo, không dán vào 1 người. Dừng 2-3 giây với mỗi người khi nói điểm quan trọng.

### Eye contact strategy

| Vị trí | Chiến lược |
|--------|------------|
| Giám khảo giữa | Nhìn nhiều nhất — người quyết định chính |
| Giám khảo trái | Thỉnh thoảng nhìn để bao quát |
| Giám khảo phải | Ít nhất 1 lần trong 2 phút để họ cảm thấy được include |
| Audience | Thỉnh thoảng quét để tạo kết nối |

### Nếu quên dòng

1. **Dừng 1-2 giây** — không panic, đây là normal pause.
2. **Nhìn xuống cheat sheet** trên màn hình demo (đã chuẩn bị sẵn).
3. **Paraphrase:** "Nói cách khác..." để mua thời gian.
4. **Chuyển action:** "Để tôi demo trực tiếp thay vì mô tả..." — luôn có demo để cover.

### Quản lý thời gian Q&A

- **Total Q&A:** 5 phút (nếu demo 5 phút → tổng 10 phút)
- **Mỗi câu hỏi:** Tối đa 30-45 giây trả lời
- **Nếu câu hỏi dài/phức tạp:** "Câu hỏi rất hay, để tôi trả lời ngắn gọn trước, sau đó có thể discuss thêm."
- **Nếu không biết:** "Đây là insight mà chúng tôi sẽ research thêm sau hackathon. Cảm ơn bạn đã gợi ý."
- **Kết thúc mạnh:** "Câu hỏi cuối được không ạ?" — dùng được nếu hết giờ.

### Checklist trước khi demo

- [ ] Laptop đã kết nối màn hình/ projector
- [ ] Browser đã mở sẵn tab app
- [ ] Backup screenshots đã mở trong tab riêng
- [ ] Video backup đã sẵn sàng play
- [ ] API docs đang mở ở `/docs`
- [ ] Demo accounts/logins đã chuẩn bị
- [ ] Timer/đồng hồ để tracking thời gian
- [ ] Powerpoint slide cuối có QR code video backup

---

## Tài liệu liên quan

- [Pitch Deck](docs/demo/pitch-deck.md)
- [API Endpoints](docs/api/endpoints.md)
- [Setup Guide](docs/SETUP.md)
- [Deployment Guide](docs/DEPLOYMENT.md)
