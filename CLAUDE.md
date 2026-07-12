# CLAUDE.md — Gicungduoc x FPT AI Factory

## Project Overview

- **Tên**: Gicungduoc - AI Chatbot đa nền tảng
- **Cloud**: FPT AI Factory (GPU Container)
- **Development**: VSCode Remote SSH
- **UI/UX**: Figma → code
- **Platforms**: Web (Next.js) + Mobile (Expo) + Desktop (Tauri)
- **AI**: FPT AI Inference với SSE streaming

---

## Kiến Trúc

```
FPT AI Factory (GPU Container)
├── Backend (FastAPI) :8000
├── Web (Next.js) :3000
├── Mobile (Expo) :19000
└── Desktop (Tauri) :4000
```

AI Layer: SSE streaming → FPT AI Inference (mkp-api.fptcloud.com)

---

## Branch Strategy

```
main
├── web      # Next.js app
├── mobile   # Expo React Native
└── desktop  # Tauri desktop
```

---

## VSCode Remote SSH Setup

```bash
# ~/.ssh/config
Host fpt-aifactory
    HostName <container-ip>
    User fptai
    IdentityFile ~/.ssh/your-key.pub
```

VSCode: Cmd+Shift+P → "Remote-SSH: Connect to Host" → chọn fpt-aifactory

---

## Common Tasks

### Backend
```bash
cd backend
python -m venv venv && source venv/bin/activate
pip install -r requirements.txt
cp .env.example .env  # Thêm AI_TOKEN
uvicorn app.main:app --host 0.0.0.0 --port 8000 --reload
```

### Web
```bash
cd frontend && npm install && npm run dev
```

### Mobile
```bash
npx expo start
```

### Desktop
```bash
npm run tauri dev
```

---

## FPT AI Inference

```python
# API
BASE_URL = "https://mkp-api.fptcloud.com"
# Streaming: stream=True → SSE data: {"content": "..."}
```

---

## Git

```bash
# Branch
git checkout web       # Web app
git checkout mobile    # Mobile app
git checkout desktop   # Desktop app

# Commit
git add . && git commit -m "feat: mô tả"
git push origin web    # hoặc mobile, desktop
```

---

## Important

1. Không commit `.env` files (chứa API keys)
2. Backend port: 8000
3. Frontend port: 3000
4. SSE streaming cho AI responses
5. Push GitHub → CI/CD auto-deploy lên FPT AI Factory
