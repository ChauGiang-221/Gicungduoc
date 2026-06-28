# Setup Guide

## 1. Yêu cầu máy

- Node.js >= 18
- Python >= 3.10
- Git
- Tài khoản Vercel
- Tài khoản Railway hoặc Render
- Firebase project
- API keys: OpenAI, Anthropic, Google Gemini

## 2. Backend

```bash
cd backend
python -m venv venv
venv\\Scripts\\activate
pip install -r requirements.txt
cp .env.example .env
uvicorn app.main:app --reload --port 8000
```

Kiểm tra:

```bash
curl http://localhost:8000/health
```

## 3. Frontend

```bash
cd frontend
npm install
cp .env.example .env.local
npm run dev
```

Mở: http://localhost:3000

## 4. Firebase

1. Vào Firebase Console.
2. Tạo project mới.
3. Enable Firestore Database.
4. Project Settings → Service accounts → Generate new private key.
5. Lưu file thành `backend/firebase-credentials.json`.
6. Set `FIREBASE_CREDENTIALS_PATH=./firebase-credentials.json` trong backend `.env`.

## 5. AI keys

- OpenAI: tạo key ở OpenAI Platform.
- Anthropic: tạo key ở Anthropic Console.
- Gemini: tạo key trong Google AI Studio.

Khuyến nghị hackathon:

- Dùng GPT-4o cho general reasoning.
- Dùng Claude cho long context / phân tích tài liệu.
- Dùng Gemini cho multimodal và chi phí thấp.
