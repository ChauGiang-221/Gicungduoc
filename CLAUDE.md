# CLAUDE.md — AI Coding Assistant Config

> Cấu hình Claude Code cho project hackathon này.
> Khi Claude Code mở project, đọc file này trước.

---

## 🏗️ Project Overview

- **Tên**: VN AI Innovation Hackathon Starter
- **Mục tiêu**: Nhanh chóng xây dựng MVP AI cho bài toán thực tế Việt Nam
- **Team**: Backend, Frontend, UI/UX Designer
- **Thời gian**: 48-hour hackathon

## 📁 Project Structure

```
Gicungduoc/
├── frontend/           # Next.js 15 + Tailwind + Shadcn UI
│   ├── src/
│   │   ├── app/       # App Router pages
│   │   ├── components/# UI components (ui/, ai-chat.tsx)
│   │   ├── lib/       # API client (api.ts, utils.ts)
│   │   └── hooks/     # React hooks
│   └── package.json
├── backend/            # FastAPI + AI providers
│   ├── app/
│   │   ├── api/       # Routes (ai.py, health.py)
│   │   ├── services/  # AI service, database
│   │   ├── models/    # Pydantic schemas
│   │   └── config.py  # Settings
│   ├── requirements.txt
│   └── main.py
├── docs/               # Tài liệu
│   ├── AI-HELPER.md   # Prompts & skills ⭐
│   ├── PRE-HACKATHON.md
│   ├── pitch-deck.md
│   ├── demo-script.md
│   └── RESOURCES.md
└── docker-compose.yml
```

## 🤖 AI Services

| Provider | Model | Use Case |
|----------|-------|----------|
| OpenAI | GPT-4o | General reasoning |
| Anthropic | Claude 3.5 Sonnet | Long context |
| Google | Gemini 1.5 Pro | Multimodal |

## 🎯 Conventions

### Git Commits
```bash
feat: [mô tả ngắn]      # Tính năng mới
fix: [mô tả]            # Fix bug
docs: [mô tả]           # Documentation
style: [mô tả]          # Formatting
refactor: [mô tả]       # Refactor code
```

### Branch Naming
```
main                 # Production
dev                  # Development integration
feature/ui-xxx       # Frontend features
feature/backend-xxx  # Backend features
```

### Code Style
- **Backend**: Python, FastAPI, Pydantic v2, async/await
- **Frontend**: TypeScript, Next.js 15 App Router, Tailwind CSS
- **Components**: Shadcn UI style (Radix + Tailwind)

## 📋 Common Tasks

### Run Backend
```bash
cd backend
python -m venv venv && venv\Scripts\activate
pip install -r requirements.txt
uvicorn app.main:app --reload --port 8000
```

### Run Frontend
```bash
cd frontend
npm install
npm run dev
```

### Deploy
```bash
# Frontend → Vercel
vercel --prod

# Backend → Railway
cd backend && railway up
```

## 🔧 Tools & Settings

### Claude Code Commands
- `/help` — Help
- `/clear` — Clear conversation
- `/model` — Switch model

### Key Files
- `docs/AI-HELPER.md` — Prompts cho từng task
- `docs/PRE-HACKATHON.md` — Checklist
- `docs/pitch-deck.md` — Slide structure

## ⚠️ Important Notes

1. **API Keys**: Không bao giờ commit `.env` files
2. **Backend port**: 8000
3. **Frontend port**: 3000
4. **CORS**: Backend cho phép `localhost:3000` và `*.vercel.app`
5. **Streaming**: Dùng SSE cho AI responses

## 🚀 Quick Start

```bash
# 1. Clone
git clone https://github.com/ChauGiang-221/Gicungduoc.git
cd Gicungduoc

# 2. Backend
cd backend
python -m venv venv
venv\Scripts\activate
pip install -r requirements.txt
cp .env.example .env  # Điền API keys
uvicorn app.main:app --reload

# 3. Frontend (terminal mới)
cd frontend
npm install
cp .env.example .env.local
npm run dev
```

## 📞 Team Roles

| Role | Focus |
|------|-------|
| Backend | API, AI integration, database |
| Frontend | UI, API client, deploy |
| Designer | User flow, design system |

---

**Last updated: June 2026**