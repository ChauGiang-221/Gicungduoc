# Gicungduoc

AI Chatbot đa nền tảng với FPT AI Factory.

## Tech Stack

- **Cloud**: FPT AI Factory (GPU Container)
- **Development**: VSCode Remote SSH
- **Backend**: FastAPI + Python
- **Web**: Next.js 15
- **Mobile**: Expo (React Native)
- **Desktop**: Tauri
- **AI**: FPT AI Inference (SSE Streaming)

## Bắt Đầu

### 1. SSH vào FPT AI Factory

```bash
# VSCode: Cmd+Shift+P → "Remote-SSH: Connect to Host"
ssh fpt-aifactory
```

### 2. Clone repo

```bash
git clone https://github.com/ChauGiang-221/Gicungduoc.git
cd Gicungduoc
```

### 3. Chọn platform

```bash
git checkout web      # Web (Next.js)
git checkout mobile    # Mobile (Expo)
git checkout desktop   # Desktop (Tauri)
```

### 4. Setup

```bash
# Backend
cd backend
python -m venv venv
source venv/bin/activate
pip install -r requirements.txt

# Frontend
cd frontend && npm install
```

### 5. Chạy

```bash
# Backend
uvicorn app.main:app --host 0.0.0.0 --port 8000 --reload

# Web (terminal mới)
cd frontend && npm run dev
```

## Branch Strategy

```
main
├── web      # Next.js app
├── mobile   # Expo React Native
└── desktop  # Tauri desktop app
```

## Tài Liệu

Xem `docs/README.md` để biết thêm chi tiết.

## License

MIT
