# Resources & Research - VN AI Innovation Hackathon

> Compiled from GitHub repos, blog posts, and public learnings.
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

## 📂 GitHub Repositories Tham Khảo (Thật 100%)

### Các đội đã thi VNPT AI Hackathon 2025

#### 🥇 vnpt-ai — RAG Pipeline cho Vietnamese QA
**⭐ 12 stars** | [github.com/duongtruongbinh/vnpt-ai](https://github.com/duongtruongbinh/vnpt-ai)

**Tech Stack:** Python, LangGraph, LangChain, Qdrant, FastAPI, pgvector

**Key Learnings:**
- **Self-correcting code execution** — tự retry đến 5 lần, thường đúng ngay lần 2
- **Router pattern** — phân loại câu hỏi vào Math/Logic/Knowledge/Toxic domain
- **Two-stage retrieval** — top-k docs → LLM reranking để tăng precision
- **Fast-Track Detection** — detect toxic/keywords trước khi gọi LLM → tiết kiệm API cost
- **Real-time checkpointing** — mỗi câu hỏi được lưu vào `inference_log.json`
- **Auto-resume** — tự phát hiện quota limit và chờ reset

#### 🥈 vnptAI-Hackathon-2025 — Multi-Domain QA System
**⭐ 2 stars** | [github.com/baeGil/vnptAI-Hackathon-2025](https://github.com/baeGil/vnptAI-Hackathon-2025)

**Tech Stack:** Python 3.11, LangGraph, Qdrant (HNSW + BM25), VNPT AI API, Docker

**Key Learnings:**
- **Validation Accuracy: 85-91%** on validation set
- **Avg Latency: 3-4s** cho RAG, **9-16s** cho Math, **2-3s** cho Reading
- **Batch processing** với Chain-of-Thought prompting và Majority Voting
- **Auto-resume inference** — chạy overnight không cần monitor

#### 🥉 vnpt_ai_hackathon_meetmate — AI Meeting Co-Host
**⭐ 2 stars** | [github.com/PhuocDang2104/vnpt_ai_hackathon_meetmate](https://github.com/PhuocDang2104/vnpt_ai_hackathon_meetmate)

**Tech Stack:** Electron/React, FastAPI, TypeScript, pgvector, LangGraph agents, WebSocket

**Key Learnings:**
- **S/AAR architecture** — Self-aware Adaptive Agentic RAG
- **Real-time WS pipeline** — audio → ASR → session bus → live transcript
- **Pre/In/Post meeting** staging workflow
- **RAG-first + graded retrieval** — hybrid search, ACL filter, no-source-no-answer
- **Multi-source ingestion** — crawl single pages, full domains, topic-based

### Các đội khác

#### AI4VN-Hackathon2020 — Image Classification
**⭐ 2 stars** | [github.com/huynhtuan17ti/AI4VN-Hackathon2020](https://github.com/huynhtuan17ti/AI4VN-Hackathon2020)

- 7 classes: no event, fallen tree, fire, flooding, bad road, traffic jam, garbage, traffic accident
- **Achieved 6th place** trong final round
- Used EfficientNetB0 với multilabel approach

#### StudyTrack-AI — Naver Vietnam AI Hackathon
**⭐ 0 stars** | [github.com/Vu-Quoc-Tuan/StudyTrack-AI](https://github.com/Vu-Quoc-Tuan/StudyTrack-AI)

- AI task generation, study analytics
- **Tech: React 18, TypeScript, Vite, Google Gemini API**
- Chrome extension cho quick task capture

#### COZYHOME — Naver Vietnam AI Hackathon 2025
**⭐ 0 stars** | [github.com/the-khiem7/COZYHOME_NaverHackathon2025](https://github.com/the-khiem7/COZYHOME_NaverHackathon2025)

- Task (Kanban), Calendar, Journal, Mood Tracker
- AI task generation, smart scheduling, reflection prompts

---

## 🛠️ Tools & Boilerplates (Thật 100%)

### AI Hackathon Starters

| Repo | Stars | Description | URL |
|------|-------|-------------|-----|
| **AI Hackathon Starter** | - | OpenAI, LangChain, LlamaIndex, RAG templates | [AAAsanjay/ai-hackathon-starter](https://github.com/AAAsanjay/ai-hackathon-starter) |
| **GenAI Hackathon Starter** | - | LLM apps, vector DB, deployment configs | [ai-forever/genai-hackathon-starter](https://github.com/ai-forever/genai-hackathon-starter) |
| **Vercel AI SDK** | 8K+ | Streaming LLM, server actions, message history | [vercel/ai](https://github.com/vercel/ai) |
| **Hackathon-Starter** | - | Next.js + TypeScript + Tailwind + AI APIs | [sotetsuk/hackathon-starter](https://github.com/sotetsuk/hackathon-starter) |
| **MLhacker** | - | ML project starter, Jupyter, deployment | [AshiqAbdulkhader/MLhacker](https://github.com/AshiqAbdulkhader/MLhacker) |

### Presentation & Design

| Tool | Description | URL |
|------|-------------|-----|
| **Canva** | AI startup pitch deck templates (free) | [canva.com](https://www.canva.com) |
| **Figma Community** | Hackathon UI kits, startup dashboards | [figma.com/community](https://www.figma.com/community?q=hackathon) |
| **Gamma.app** | AI-powered slide generator | [gamma.app](https://gamma.app) |

---

## 📊 Vietnamese Datasets & Models

| Dataset | Domain | URL |
|---------|--------|-----|
| **VLSP** | Vietnamese NLP benchmark (NER, sentiment, MT, speech) | [vlsp.hltVN.org](https://vlsp.hltVN.org) |
| **UIT-VSFC** | Vietnamese sentiment classification (tourism reviews) | [thanhtts/UIT-VSFC](https://github.com/thanhtts/UIT-VSFC) |
| **VinAI Vietnamese LLM** | State-of-the-art Vietnamese LLMs from Vingroup | [vinai.io](https://vinai.io) |
| **undertheseanlp** | Vietnamese NLP (tokenization, POS, NER) | [undertheseanlp/underthesea](https://github.com/undertheseanlp/underthesea) |
| **vncorenlp** | Full Vietnamese NLP pipeline | [vncorenlp](https://github.com/vncorenlp) |

---

## 🤖 AI Models Comparison

| Model | Context | Speed | Cost | Best For |
|-------|---------|-------|------|----------|
| **GPT-4o** | 128K | Fast | $$$ | General reasoning, code |
| **Claude 3.5 Sonnet** | 200K | Medium | $$$ | Long docs, nuanced |
| **Gemini 1.5 Pro** | 1M | Fast | $$ | Multimodal, cheap |
| **Gemini 1.5 Flash** | 1M | Very Fast | $ | High volume tasks |
| **Groq (Llama)** | 8K | **Fastest** (~500 tok/s) | $ | Real-time apps |
| **VNPT AI** | - | - | - | Vietnamese-optimized |

### ⚡ Groq - Recommended for Hackathon
- Inference: **~500 tokens/second**
- Free tier: Generous
- API: Same as OpenAI
- **Perfect for live demo!**

```python
from groq import Groq
client = Groq(api_key="gsk_...")
chat = client.chat.completions.create(
    model="llama3-8b-8192",
    messages=[{"role": "user", "content": "..."}],
    stream=True
)
```

---

## 💡 Key Learnings Từ Các Đội Đã Thi

### Từ VNPT AI Hackathon 2025

#### 1. Router Pattern — Phân loại trước khi xử lý
```
Câu hỏi → [Fast-Track Detection] 
  → Toxic? → Trả lời cố định (không gọi LLM)
  → Math? → Code Agent
  → Knowledge? → RAG
  → Reading? → Simple lookup
```
→ Tiết kiệm API calls, tăng speed

#### 2. Self-Correcting Loop
```
Code Agent → Run code → Error?
  → Yes → Fix → Retry (max 5 lần)
  → No → Return result
```
→ Thường đúng ngay lần retry đầu tiên

#### 3. Batch Processing + Majority Voting
```
1 câu hỏi → Prompt với CoT → Run 3-5 lần 
→ Đếm kết quả → Majority wins
```
→ Tăng accuracy đáng kể

#### 4. Real-time Checkpointing
```
Mỗi câu hỏi → Lưu vào inference_log.json
→ Nếu crash → Resume từ checkpoint
→ Auto-generate CSV khi quota hit
```

#### 5. Two-Stage Retrieval
```
Query → Top-50 docs (BM25) 
  → LLM rerank → Top-5 docs 
  → Final answer
```
→ Precision cao hơn đáng kể

---

## 🎯 Chiến Thắng - Nguyên Tắc Vàng

### Từ các đội top

1. **Problem-first, not solution-first** — Chọn bài toán cụ thể Việt Nam
2. **Multi-stage pipeline** — Router → RAG → Code Agent → Self-correct
3. **Hybrid retrieval** — BM25 + vector + LLM reranking
4. **Batch + voting** — CoT prompting + majority voting = accuracy cao hơn
5. **Checkpoint everything** — inference_log.json, auto-resume
6. **Auto-detect limits** — quota → graceful shutdown → CSV submission
7. **Deploy early** — Vercel + Railway staging sớm

### Domain Thắng Lợi

| Domain | Bài toán cụ thể |
|--------|-----------------|
| 🏥 **Healthcare** | AI chẩn đoán từ xa, phân tích hình ảnh y tế |
| 📚 **Education** | AI tutoring, Vietnamese QA, exam prep |
| 💼 **Productivity** | Meeting assistant, task management, study tracker |
| 🌾 **Agriculture** | Crop disease detection, smart irrigation |
| 🏙️ **Safety** | Traffic monitoring, disaster detection |

---

## ⚡ Quick Commands

```bash
# Clone thêm repos tham khảo
git clone https://github.com/duongtruongbinh/vnpt-ai
git clone https://github.com/baeGil/vnptAI-Hackathon-2025
git clone https://github.com/PhuocDang2104/vnpt_ai_hackathon_meetmate

# Clone starter của team
git clone https://github.com/ChauGiang-221/Gicungduoc

# Backend
cd backend && python -m venv venv && venv\Scripts\activate && pip install -r requirements.txt

# Frontend  
cd frontend && npm install

# Deploy
vercel --prod          # Frontend
railway up             # Backend
```

---

**Research from real GitHub repos — June 2026 🚀**
