# Demo Script

Tổng thời lượng: 5 phút.

## 0:00-0:30 — Mở đầu

"Xin chào ban giám khảo. Team chúng em xây dựng [tên sản phẩm], một giải pháp AI giúp [nhóm người dùng] giải quyết [vấn đề] trong bối cảnh Việt Nam."

## 0:30-1:10 — Problem

"Hiện tại, người dùng phải [cách làm cũ]. Việc này gây ra 3 vấn đề: mất thời gian, dễ sai sót, và khó mở rộng."

## 1:10-2:40 — Live demo

### Scenario 1: Golden path

1. Mở app.
2. Nhập câu hỏi / dữ liệu mẫu.
3. Chọn AI provider.
4. Nhấn gửi.
5. AI trả kết quả streaming.

Talking points:

- "Ở đây user không cần hiểu AI hoạt động thế nào. Họ chỉ nhập vấn đề thực tế."
- "Backend có thể switch giữa GPT-4, Claude và Gemini tùy use case."
- "Kết quả được trả realtime để trải nghiệm nhanh hơn."

### Scenario 2: Provider switch

1. Chọn Claude hoặc Gemini.
2. Gửi cùng câu hỏi.
3. So sánh tốc độ / chất lượng.

Talking points:

- "Điểm mạnh của kiến trúc là không bị khóa vào một provider."
- "Nếu provider A lỗi hoặc đắt, có thể chuyển sang provider B."

## 2:40-3:30 — Tech architecture

"Frontend dùng Next.js và Tailwind để triển khai nhanh, backend dùng FastAPI vì dễ tích hợp AI/ML. Firestore giúp realtime và không cần vận hành database phức tạp."

## 3:30-4:20 — Impact

"Nếu triển khai thật, sản phẩm có thể giúp [nhóm người dùng] giảm [thời gian/chi phí] và tăng khả năng tiếp cận dịch vụ AI tại Việt Nam."

## 4:20-5:00 — Closing

"Điều team muốn ban giám khảo nhớ là: chúng em không chỉ demo một chatbot, mà là một nền tảng có thể áp dụng AI vào bài toán thực tế Việt Nam, triển khai nhanh và mở rộng được."

## Backup nếu live demo fail

- Chạy video demo 60-90 giây.
- Mở screenshots trong slide.
- Dùng API docs `/docs` để chứng minh backend hoạt động.
- Nói rõ: "Do vấn đề mạng tại venue, team xin dùng bản ghi demo đã chuẩn bị trước."

## Q&A nhanh

### Vì sao cần AI?

AI xử lý ngôn ngữ tự nhiên, cá nhân hóa phản hồi và tự động hóa tác vụ mà rule-based khó scale.

### Có rủi ro hallucination không?

Có. Mitigation: giới hạn domain prompt, thêm nguồn dữ liệu kiểm chứng, human-in-the-loop cho quyết định quan trọng.

### Kiếm tiền bằng gì?

Freemium cho cá nhân, subscription cho tổ chức, API licensing cho đối tác.

### Khác chatbot thường ở đâu?

Sản phẩm tập trung vào workflow cụ thể, có database, dashboard, provider abstraction và khả năng tích hợp vào hệ thống thật.
