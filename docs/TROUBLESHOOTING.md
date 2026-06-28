# Troubleshooting

## Backend không chạy

### Lỗi thiếu module

```bash
pip install -r requirements.txt
```

### Lỗi import `app`

Chạy từ thư mục `backend`:

```bash
uvicorn app.main:app --reload --port 8000
```

### Lỗi API key

Kiểm tra `backend/.env`:

```env
OPENAI_API_KEY=...
ANTHROPIC_API_KEY=...
GOOGLE_API_KEY=...
```

## Frontend không chạy

### Node version quá cũ

```bash
node --version
```

Cần >= 18.

### Dependency lỗi

```bash
cd frontend
rm -rf node_modules package-lock.json
npm install
```

Windows PowerShell:

```powershell
Remove-Item -Recurse -Force node_modules
Remove-Item package-lock.json
npm install
```

## CORS error

Backend `.env` cần có origin frontend:

```env
ALLOWED_ORIGINS=http://localhost:3000,https://your-app.vercel.app
```

## AI response chậm

- Dùng streaming endpoint.
- Giảm `max_tokens`.
- Chuyển provider sang Gemini Flash hoặc GPT-4o mini nếu cần tối ưu chi phí/tốc độ.

## Deploy fail

### Vercel

- Kiểm tra `frontend/package.json` build script.
- Set `NEXT_PUBLIC_API_URL`.
- Root directory trên Vercel phải là `frontend`.

### Railway

- Root directory là `backend`.
- Start command: `uvicorn app.main:app --host 0.0.0.0 --port $PORT`.
- Set đầy đủ environment variables.
