# Deployment Guide

## Frontend: Vercel

```bash
cd frontend
npm install
npm run build
vercel --prod
```

Environment variables trên Vercel:

```env
NEXT_PUBLIC_API_URL=https://your-backend.up.railway.app
```

## Backend: Railway

```bash
cd backend
railway login
railway init
railway up
```

Railway start command:

```bash
uvicorn app.main:app --host 0.0.0.0 --port $PORT
```

Environment variables trên Railway:

```env
OPENAI_API_KEY=...
ANTHROPIC_API_KEY=...
GOOGLE_API_KEY=...
FIREBASE_PROJECT_ID=...
ALLOWED_ORIGINS=https://your-frontend.vercel.app
```

## Backend: Render alternative

Build command:

```bash
pip install -r requirements.txt
```

Start command:

```bash
uvicorn app.main:app --host 0.0.0.0 --port $PORT
```

## Pre-demo checks

- `GET /health` trả `healthy`.
- Frontend gọi được backend.
- Chat AI trả response trong 2-8 giây.
- Có video demo dự phòng nếu mạng yếu.
- Có `.env.example`, không commit `.env` thật.
