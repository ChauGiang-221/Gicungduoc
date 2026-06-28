# VN AI Innovation Hackathon Starter

Khung sườn plug-and-play cho team hackathon AI tại Việt Nam: frontend Next.js, backend FastAPI, Firebase Firestore, multi-provider AI (OpenAI, Claude, Gemini), deployment config và kịch bản pitch/demo.

## Mục tiêu

- Xây dựng nhanh MVP AI cho bài toán thực tế Việt Nam.
- Chia việc rõ ràng cho Backend Developer, Frontend Developer, UI/UX Designer.
- Deploy nhanh lên Vercel + Railway/Render.
- Có sẵn tài liệu pitch, demo, API và setup.

## Tech stack

### Frontend
- Next.js 15 App Router
- React 19
- TypeScript
- Tailwind CSS
- Shadcn UI style components
- Framer Motion
- Lucide Icons

### Backend
- Python FastAPI
- Pydantic validation
- OpenAI API
- Anthropic Claude API
- Google Gemini API
- Firebase Firestore

### Deployment
- Frontend: Vercel
- Backend: Railway hoặc Render
- Database: Firebase Firestore

## Cấu trúc project

```txt
project/
├── frontend/          # Next.js app
│   ├── src/app/       # App Router pages
│   ├── src/components/# UI components
│   └── src/lib/       # API client, utils
├── backend/           # FastAPI app
│   ├── app/api/       # API routes
│   ├── app/services/  # AI + database services
│   ├── app/models/    # Pydantic schemas
│   └── tests/         # Tests
├── docs/              # Pitch, demo, setup, API docs
├── shared/            # Shared contracts/types
└── .github/workflows/ # CI/CD
```

## Chạy local trong 5 phút

### Backend

```bash
cd backend
python -m venv venv
# Windows
venv\\Scripts\\activate
# macOS/Linux
source venv/bin/activate
pip install -r requirements.txt
cp .env.example .env
uvicorn app.main:app --reload --port 8000
```

API docs: http://localhost:8000/docs

### Frontend

```bash
cd frontend
npm install
cp .env.example .env.local
npm run dev
```

App: http://localhost:3000

## Environment variables

### Backend

Copy [backend/.env.example](backend/.env.example) thành `backend/.env` rồi điền:

```env
OPENAI_API_KEY=...
ANTHROPIC_API_KEY=...
GOOGLE_API_KEY=...
FIREBASE_PROJECT_ID=...
FIREBASE_CREDENTIALS_PATH=./firebase-credentials.json
```

### Frontend

Copy [frontend/.env.example](frontend/.env.example) thành `frontend/.env.local`:

```env
NEXT_PUBLIC_API_URL=http://localhost:8000
```

## API chính

- `GET /health` — kiểm tra backend sống.
- `GET /api/v1/ai/providers` — xem provider AI khả dụng.
- `POST /api/v1/ai/chat` — chat AI non-streaming.
- `POST /api/v1/ai/chat/stream` — chat AI streaming qua SSE.

## Team workflow gợi ý

### Backend Developer
- Hoàn thiện database schema.
- Tùy biến prompt AI cho bài toán cụ thể.
- Thêm endpoints business logic.
- Deploy backend.
- Stress test API.

### Frontend Developer
- Implement UI từ Figma.
- Tích hợp API.
- Thêm loading/error states.
- Optimize UX/mobile.
- Deploy frontend.

### UI/UX Designer
- Research user flow.
- Wireframe, mockup.
- Design system.
- Prototype tương tác.
- Support frontend handoff.

## Tài liệu quan trọng

- [docs/SETUP.md](docs/SETUP.md)
- [docs/DEPLOYMENT.md](docs/DEPLOYMENT.md)
- [docs/api/endpoints.md](docs/api/endpoints.md)
- [docs/demo/pitch-deck.md](docs/demo/pitch-deck.md)
- [docs/demo/demo-script.md](docs/demo/demo-script.md)
- [docs/TROUBLESHOOTING.md](docs/TROUBLESHOOTING.md)

## License

MIT
