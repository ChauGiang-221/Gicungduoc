# Resources & Research - VN AI Innovation Hackathon

> Compiled from GitHub, blog posts, and public learnings.
> Last updated: June 2026

---

## 🏆 Judge Criteria - Điều BGK Muốn Thấy

| Tiêu chí | Trọng số | Điều cần show |
|-----------|----------|----------------|
| Technical Implementation | 30% | Multi-provider AI, streaming, error handling, working demo |
| Innovation & Problem Solving | 25% | Bài toán Việt Nam cụ thể, không phải chatbot generic |
| Business Potential & Impact | 20% | Metrics cụ thể: "giảm X% thời gian, Y người dùng" |
| Presentation & Demo | 15% | Live demo smooth, backup video sẵn sàng, Q&A tốt |
| UI/UX & Polish | 10% | Responsive, professional, micro-interactions |

---

## 🎯 Chiến Thắng - Nguyên Tắc Vàng

### Từ Các Đội Thắng Giải

1. **Problem-first** — Chọn bài toán cụ thể Việt Nam, không phải "AI chatbot"
2. **Live demo là vua** — Judges muốn thấy AI thực sự hoạt động
3. **Multi-provider AI** — Dùng GPT-4 + Claude + Gemini, không lock 1 provider
4. **Vietnamese context** — Dữ liệu tiếng Việt, context Việt Nam
5. **Backup always** — Video demo + screenshots dự phòng
6. **Practice 5+ times** — Đúng 5 phút, timing chuẩn
7. **Deploy early** — Vercel + Railway staging sớm, judges có thể test URL
8. **Honesty about limits** — Judges tôn trọng self-awareness

---

## 💼 Domain Bài Toán Việt Nam Tiềm Năng

### 🏥 Healthcare
- AI chẩn đoán từ xa cho vùng nông thôn (1 bác sĩ/800 người)
- Phân tích hình ảnh y tế (ung thư phổi, gan, vú)
- Mental health screening với limited psychiatrist access
- Medical record fragmentation across hospitals

### 📚 Education
- AI tutoring cá nhân hóa, giảm khoảng cách thành thị-nông thôn
- Teacher workload reduction (45-60 students/class)
- University entrance exam prep inequality
- Vocational training mismatch với job market

### 🌾 Agriculture
- Phát hiện bệnh cây trồng không cần agronomist
- Smart irrigation cho climate change adaptation
- Precision farming cho smallholder farmers (70% < 1 hectare)
- Post-harvest loss reduction (25-30% loss rate)
- Aquaculture disease monitoring cho cá tra/basa

### 💰 Finance
- Credit scoring cho informal sector workers (không có lịch sử tín dụng)
- Microfinance accessibility cho rural population
- Fraud detection cho digital payments (e-wallets, QR)
- Financial literacy cho young adults
- Insurance penetration in rural areas

### 🌿 Environment
- Air quality monitoring và prediction cho Hanoi/HCMC smog
- Water pollution detection cho rivers/canals
- Flood prediction cho Mekong Delta
- Wildlife trafficking detection

---

## 📂 GitHub Repositories Tham Khảo

> Search thêm: `site:github.com "vn ai innovation" OR "ai hackathon vietnam"`

### Tìm kiếm Recommended

```bash
# Trên GitHub search
"vn ai innovation" hackathon
"ai hackathon" vietnam winner
"vietnam" "ai" "hackathon" starter
"ai innovation" "vietnam" repository
```

### Vietnamese AI Repos

- **undertheseanlp/underthesea**: Vietnamese NLP library
  - github.com/undertheseanlp/underthesea
  - Tokenization, POS tagging, NER cho tiếng Việt

- **vncorenlp**: Full Vietnamese NLP pipeline
  - github.com/vncorenlp
  - Ressed, word segmentation, POS tagging, NER

- **fastText Vietnamese**: Word embeddings
  - fasttext.cc/docs/get_trained.html
  - Pre-trained vectors cho 157 languages including Vietnamese

### Starter Templates

| Repo | Stars | Description |
|------|-------|-------------|
| vercel/ai | 8K+ | Official Vercel AI templates |
| langchain-ai/langchain | 90K+ | AI orchestration framework |
| ChauGiang-221/Gicungduoc | - | Our hackathon starter |

---

## 📝 Blog Posts & Learnings

### Tìm kiếm Recommended

```
site:medium.com "hackathon" "ai" "vietnam" "experience"
site:viblo.asia "hackathon" "ai" "việt nam"
site:kipalog.com "hackathon" "ai"
```

### Vietnamese Tech Blogs

- **Viblo**: https://viblo.asia - Vietnamese tech community, nhiều bài về AI
- **Kipalog**: https://kipalog.com - Vietnamese developer blog
- **TopDev**: https://topdev.vn - Vietnamese tech jobs & blogs
- **ICTNews**: https://ictnews.vn - Tech news Vietnam

---

## 🎨 Presentation Templates

| Tool | Use Case | Free | URL |
|------|----------|------|-----|
| **Canva** | Pitch deck templates | ✅ (watermark) | https://www.canva.com |
| **Gamma.app** | AI-powered slides generator | ✅ (limited) | https://gamma.app |
| **Figma** | UI mockups + prototypes | ✅ | https://figma.com |
| **Pitch.com** | Interactive decks | ✅ tier | https://pitch.com |
| **Slidesgo** | Free Google Slides | ✅ | https://slidesgo.com |

### Canva Templates Search
Search: `pitch deck ai` | `hackathon presentation` | `startup pitch`

---

## 🛠️ Vietnamese AI Ecosystem

### Vietnamese AI Companies & APIs

| Company | APIs | Free Tier | URL |
|---------|------|-----------|-----|
| **Viettel AI** | Vietnamese LLMs, OCR, speech | ✅ | viettelai.vn |
| **FPT AI** | Vietnamese NLP, speech, OCR | ✅ | fpt.ai |
| **VNG AI** | Conversational AI, Vietnamese | ✅ | vng.com.vn |
| **Zalo AI** | Vietnamese language AI | ✅ | zaloai.zalo.me |

### Vietnamese NLP Libraries

```python
# Install underthesea
pip install underthesea

# Usage
from underthesea import word_tokenize, pos_tag, ner

text = "Trường đại học Bách Khoa TP.HCM"
tokens = word_tokenize(text, format="text")
# Output: "Trường đại_học Bách_Khoa TP.HCM"

# Named Entity Recognition
from underthesea import ner
ner(text)
# Output: [('Trường', 'N', 'O'), ...]
```

---

## 📊 Vietnamese Datasets

| Dataset | Domain | URL |
|---------|--------|-----|
| **UIT-VSFC** | Vietnamese sentiment | github.com/undertheseanlp/uit-vsfc |
| **Vietnamese Fake News** | NLP classification | kaggle.com/datasets |
| **Viettel Speech** | Speech recognition | viettelai.vn |
| **VietCorpus** | Large text corpus | Various sources |
| **Open Data VN** | Government data | data.gov.vn |
| **GSO Vietnam** | Official statistics | gso.gov.vn |

### Environment Datasets

- **World Air Quality**: waqi.info
- **Mekong Delta Flood**: NASA, NOAA data
- **Vietnam Census**: gso.gov.vn

---

## 🤖 AI Models Comparison

| Model | Context | Speed | Cost | Best For |
|-------|---------|-------|------|----------|
| **GPT-4o** | 128K | Fast | $$$ | General reasoning, code |
| **Claude 3.5 Sonnet** | 200K | Medium | $$$ | Long docs, nuanced |
| **Gemini 1.5 Pro** | 1M | Fast | $$ | Multimodal, cheap |
| **Gemini 1.5 Flash** | 1M | Very Fast | $ | High volume tasks |
| **Groq (Llama)** | 8K | **Fastest** | $ | Real-time apps |
| **Mistral** | 32K | Fast | $ | Open source |

### Groq - Recommended for Hackathon
- Inference speed: ~500 tokens/second
- Free tier: Generous
- API: Same as OpenAI
- **Perfect for live demo - no waiting!**

```python
# Groq setup
from groq import Groq
client = Groq(api_key="gsk_...")

chat_completion = client.chat.completions.create(
    model="llama3-8b-8192",
    messages=[{"role": "user", "content": "Hello"}],
    stream=True
)
```

---

## 💡 Tips Từ Hackathon Winners

### 1. Chọn Bài Toán
- ❌ "AI chatbot trả lời câu hỏi"
- ✅ "AI phát hiện bệnh cây trồng từ ảnh chụp lá"

### 2. Demo Live
- ❌ "Đây là screenshot của sản phẩm"
- ✅ "Để tôi demo với ảnh thật từ nông trại" → upload → AI phát hiện bệnh

### 3. Backup Plan
- ❌ Hy vọng live demo không fail
- ✅ Video 60s sẵn sàng, nói "Do network tại venue..." rồi play video

### 4. Timing
- ❌ 7 phút → bị cắt giữa chừng
- ✅ Đúng 5 phút, có đồng hồ, có người nhắc

### 5. Metrics
- ❌ "Sản phẩm tốt"
- ✅ "Giảm 60% thời gian chẩn đoán, chính xác 92%"

---

## 🔗 Search Tips

Muốn tìm thêm resources?

```
# GitHub
site:github.com "vn ai" OR "vietnam ai" hackathon
site:github.com "hackathon" "ai" "vietnam" "starter"

# Blogs
site:medium.com "hackathon" "ai" "vietnam"
site:viblo.asia "hackathon" "ai" "việt nam"
site:kipalog.com "hackathon" "ai"

# Templates
canva.com "pitch deck" "ai" "startup"
gamma.app "presentation" "hackathon"
```

---

**Research continues - check back for updates! 🚀**
