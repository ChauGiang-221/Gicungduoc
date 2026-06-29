# Pre-Hackathon Checklist — VN AI Innovation 2026

## 🎯 Tổng Quan

| Thông tin | Chi tiết |
|-----------|----------|
| Cuộc thi | VN AI Innovation |
| Format | 48-hour Hackathon |
| Tech stack | Next.js + FastAPI + AI (OpenAI/Claude/Gemini) + Firebase |
| Team roles | Backend · Frontend · UI/UX Designer |

---

## ✅ 7 NGÀY TRƯỚC — Chuẩn Bị Chi Tiết

### Kỹ Thuật [Backend]

- [ ] Đã setup backend local và chạy được `uvicorn app.main:app --reload`
- [ ] Đã cấu hình API keys đầy đủ: `OPENAI_API_KEY`, `ANTHROPIC_API_KEY`, `GOOGLE_API_KEY`
- [ ] Đã test cả 3 provider AI: GPT-4, Claude, Gemini đều hoạt động
- [ ] Streaming response (/chat/stream) đã test OK
- [ ] Database Firebase Firestore đã kết nối và hoạt động
- [ ] API docs tại `/docs` đã kiểm tra
- [ ] Đã deploy backend lên Railway/Render (staging URL có sẵn)
- [ ] Health check endpoint `/health` trả về 200
- [ ] Rate limiting đã config (tránh hết credit vì accidental loops)
- [ ] Error handling đã test: khi API key sai → có error message rõ ràng
- [ ] Backup API key sẵn sàng (nếu key chính hết quota)

### Kỹ Thuật [Frontend]

- [ ] Đã setup Next.js local và chạy được `npm run dev`
- [ ] `NEXT_PUBLIC_API_URL` đã trỏ đúng (local hoặc staging)
- [ ] Chat component đã tích hợp với backend streaming endpoint
- [ ] Loading state: khi đang chờ AI reply → spinner/typing indicator
- [ ] Error state: khi API fail → hiển thị thông báo lỗi đẹp
- [ ] Empty state: khi chưa có message nào → placeholder hướng dẫn
- [ ] Provider switcher: user có thể đổi giữa GPT-4 / Claude / Gemini
- [ ] Responsive mobile: test trên điện thoại thật
- [ ] Dark mode (optional): có thể toggle
- [ ] Đã deploy frontend lên Vercel staging
- [ ] URL staging sẵn sàng chia sẻ cho team
- [ ] Đã chụp 5-10 screenshots của UI để dùng trong pitch deck

### UI/UX [Designer]

- [ ] Wireframe low-fidelity đã review với team
- [ ] Design system đã bàn giao (colors, typography, spacing)
- [ ] 3 mockups chính: Landing page, Dashboard, Settings
- [ ] Figma prototype đã tạo (có thể click qua các màn hình)
- [ ] Icon library đã chọn và export (Lucide React)
- [ ] Handoff specs: spacing (px), colors (hex), fonts đã ghi rõ cho developer
- [ ] Backup: nếu dev chưa implement kịp → có screenshot/mockup thay thế cho demo

### Tài Khoản & Access

- [ ] Vercel account đã tạo, project đã setup
- [ ] Railway account đã tạo, project đã setup
- [ ] Firebase console đã access, Firestore đang hoạt động
- [ ] OpenAI account có credit ($20+)
- [ ] Anthropic account có API key
- [ ] Google Cloud account có Gemini API key
- [ ] GitHub repo đã push, CI/CD đã green
- [ ] Tất cả team members đã có quyền write vào repo
- [ ] GH CLI đã login (`gh auth status` → logged in)

### Nội Dung [Pitch & Demo]

- [ ] Pitch deck đã viết xong (6 slides)
- [ ] Đã luyện tập pitch ≥ 5 lần (đo thời gian)
- [ ] Demo script đã viết đầy đủ (3 scenarios)
- [ ] Đã quay video demo dự phòng (60-90s)
- [ ] Slides đã thiết kế đẹp (Canva / Figma / PowerPoint)
- [ ] Đã chuẩn bị backup: nếu live demo fail → dùng video/screenshots
- [ ] 10 câu hỏi Q&A đã trả lời sẵn
- [ ] Đã luyện tập trả lời Q&A với team

### Team Coordination

- [ ] Discord/Telegram group đã tạo, tất cả online
- [ ] Phân chia vai trò rõ ràng: ai pitch, ai demo, ai vận hành laptop
- [ ] Timeline hackathon đã sync: deadline từng milestone
- [ ] Quy ước git: branch nào push vào khi nào
- [ ] Backup laptop đã chuẩn bị (nếu có)
- [ ] Hotspot 4G/5G backup đã test

---

## ✅ 48 GIỜ TRƯỚC — Final Prep

### Ngày Thứ 2

**Sáng:**
- [ ] Clone repo fresh và chạy local toàn bộ (backend + frontend)
- [ ] Test end-to-end: frontend → backend → AI → response hiển thị
- [ ] Deploy lần cuối lên staging
- [ ] Test trên điện thoại: mở URL staging, chat với AI

**Chiều:**
- [ ] Review pitch deck lần cuối, sửa nội dung nếu cần
- [ ] Luyện pitch 2 lần với đồng hồ
- [ ] Chạy demo script thực tế 3 lần (đúng thời gian)
- [ ] Quay video demo mới nếu có thay đổi

**Tối:**
- [ ] Backup tất cả: code (git), video demo (Google Drive), slides (USB)
- [ ] Nghỉ ngơi sớm, ngủ đủ giấc

### Đêm Trước Ngày Thi

- [ ] Laptop sạc > 80%
- [ ] Điện thoại sạc > 80%
- [ ] Hotspot đã test
- [ ] USB drive đã mang theo (backup)
- [ ] Nước uống + đồ ăn nhẹ đã chuẩn bị
- [ ] Vali/ba lô đã đóng đầy đủ

---

## ✅ NGÀY THI — Hackathon Day 1

### Sáng (0-4h)

| Thời gian | Task | Người phụ trách |
|-----------|------|----------------|
| 0-30p | Setup workspace, wifi, login accounts | All |
| 30p-1h | Review problem statement, chọn bài toán | All |
| 1-2h | Architecture design, chia task | Backend + Frontend |
| 2-3h | Backend: init project, setup AI service | Backend |
| 2-3h | Frontend: init Next.js, design layout | Frontend |
| 3-4h | Tích hợp AI đầu tiên, test end-to-end | Backend |

**Checkpoint 1 (4h):** Demo được 1 tính năng AI cơ bản

### Chiều (4-8h)

| Thời gian | Task | Người phụ trách |
|-----------|------|----------------|
| 4-6h | Backend: 2-3 API endpoints chính | Backend |
| 4-6h | Frontend: landing page + chat UI | Frontend |
| 6-7h | Tích hợp frontend ↔ backend | All |
| 7-8h | UI polish, responsive mobile | Frontend + Designer |
| 8h | **Checkpoint 2:** Demo luồng chính end-to-end | All |

### Tối (8-12h)

| Thời gian | Task | Người phụ trách |
|-----------|------|----------------|
| 8-9h | Thêm tính năng phụ (nice-to-have) | Backend |
| 9-10h | Animations, UX micro-interactions | Frontend |
| 10-11h | Deploy production, test URL public | Backend |
| 11-12h | Fix bugs, test edge cases | All |
| 12h | **Checkpoint 3:** Product hoàn chỉnh (MVP) | All |

---

## ✅ NGÀY THI — Hackathon Day 2

### Sáng (12-16h)

| Thời gian | Task | Người phụ trách |
|-----------|------|----------------|
| 12-14h | Full testing (mobile, edge cases, performance) | All |
| 14-15h | Viết README, documentation | Designer |
| 15-16h | Chuẩn bị pitch deck (hoàn thiện slides) | All |

### Chiều (16-20h)

| Thời gian | Task | Người phụ trách |
|-----------|------|----------------|
| 16-17h | Luyện demo script + pitch | All |
| 17-18h | Quay video demo dự phòng | Designer |
| 18-19h | Review toàn bộ, fix last-minute bugs | Backend |
| 19-20h | Chạy demo cuối cùng trên production URL | All |

### Tối (20-24h)

| Thời gian | Task | Người phụ trách |
|-----------|------|----------------|
| 20-21h | Luyện pitch với cả team (có đồng hồ) | All |
| 21-22h | Chuẩn bị Q&A, dự đoán câu hỏi BGK | All |
| 22-23h | Final backup: push git, lưu video, slides | Backend |
| 23-24h | Nghỉ ngơi, chuẩn bị tinh thần | All |

---

## ✅ TRƯỚC KHI PITCH (2h)

- [ ] Laptop đã sạc đầy + sạc dự phòng
- [ ] Demo production URL đã test lần cuối (2 người kiểm tra)
- [ ] Video demo backup đã sẵn sàng play
- [ ] Slides đã upload lên máy tính
- [ ] Presenter mode đã test
- [ ] Microphone/loa đã test (nếu có)
- [ ] Backup internet: hotspot đã bật sẵn
- [ ] Đã đi toilet, uống nước
- [ ] Đã ăn nhẹ
- [ ] Đã mặc trang phục chỉnh tề

---

## ✅ TRONG KHI PITCH

### 5 Phút Pitch

| Slide | Thời gian | Key action |
|-------|----------|------------|
| 1. Hook | 0:00-0:30 | Nói chậm, eye contact với BGK |
| 2. Problem | 0:30-1:10 | Statistics, emotional connection |
| 3. Solution | 1:10-2:10 | Giới thiệu tên sản phẩm + 3 features |
| 4. Demo | 2:10-3:40 | **Live demo** — speak while demonstrating |
| 5. Tech & Impact | 3:40-4:20 | Architecture đơn giản, metrics |
| 6. Team & Ask | 4:20-5:00 | Closing line + ask rõ ràng |

### Q&A (5-10 phút)

- Nghe câu hỏi đến hết rồi mới trả lời
- Thank you + answer ngắn gọn (30s)
- Nếu không biết → "Đây là điều team chưa explore, nhưng..."
- Giữ eye contact, tự tin

---

## ✅ SAU HACKATHON

- [ ] Chụp photo team + sản phẩm
- [ ] Xin contact BGK, mentors
- [ ] Follow up email trong 48h
- [ ] Push code public (nếu muốn)
- [ ] Viết blog post / LinkedIn về project
- [ ] Tiếp tục develop sau hackathon (nếu có traction)
- [ ] Apply vào các chương trình accelerator/incubator

---

## 🚨 XỬ LÝ SỰ CỐ

| Sự cố | Mitigation |
|-------|-----------|
| Backend down | Restart Railway dyno, kiểm tra logs |
| AI API hết quota | Switch sang provider backup (Claude → Gemini) |
| Frontend không kết nối được API | Kiểm tra CORS, NEXT_PUBLIC_API_URL |
| Demo live fail | Play video backup ngay lập tức, không hoảng |
| Quên nội dung pitch | Dùng speaker notes, đồng đội nhắc |
| Wifi venue yếu | Dùng hotspot, pre-load pages |
| Máy tính chết giữa chừng | Backup laptop, code đã push lên git |

---

## 📞 Emergency Contacts

| Người | Vai trò | SĐT |
|-------|---------|-----|
| [Tên Backend] | Backend Dev | [SĐT] |
| [Tên Frontend] | Frontend Dev | [SĐT] |
| [Tên Designer] | UI/UX | [SĐT] |

---

**Chúc team thành công! 🚀**
