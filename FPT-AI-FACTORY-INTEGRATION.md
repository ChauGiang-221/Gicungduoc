# Gicungduoc x FPT AI Factory

## Tổng Quan

Fork từ [VN AI Innovation Hackathon Starter](https://github.com/ChauGiang-221/Gicungduoc), định hướng lại cho:

- **Development**: VSCode Remote SSH vào FPT AI Factory GPU Container
- **Cloud**: FPT AI Factory (thay Vercel/Railway)
- **UI/UX**: Figma → code (design trước, nối vào sau)
- **3 Platforms**: Web + Mobile + Desktop
- **AI Realtime**: SSE streaming, độ trễ thấp nhất

---

## Kiến Trúc

```
┌─────────────────────────────────────────────────────────────────────────┐
│                    FPT AI Factory (GPU Container)                         │
│                                                                         │
│   VSCode Remote SSH ──────────────────────────────────────────────────►  │
│   (Development)                                                          │
│                                                                         │
│  ┌──────────────────────────────────────────────────────────────────┐  │
│  │                     Container (Ubuntu + GPU)                        │  │
│  │                                                                   │  │
│  │   ┌─────────────┐  ┌─────────────┐  ┌─────────────┐             │  │
│  │   │  Backend   │  │    Web     │  │   Mobile   │             │  │
│  │   │  FastAPI   │  │  Next.js   │  │    Expo    │             │  │
│  │   │   :8000    │  │   :3000    │  │   :19000   │             │  │
│  │   └──────┬──────┘  └──────┬─────┘  └──────┬─────┘             │  │
│  │          │                 │                │                     │  │
│  │          └────────────────┼────────────────┘                     │  │
│  │                           │                                      │  │
│  │                    ┌──────┴──────┐                               │  │
│  │                    │   AI Layer  │                               │  │
│  │                    │   SSE       │                               │  │
│  │                    └──────┬──────┘                               │  │
│  └───────────────────────────┼──────────────────────────────────────┘  │
│                              │                                         │
│                              ▼                                         │
│                    ┌─────────────────────┐                             │
│                    │  FPT AI Inference   │                             │
│                    │ mkp-api.fptcloud   │                             │
│                    │ (SSE Streaming)     │                             │
│                    └─────────────────────┘                             │
└─────────────────────────────────────────────────────────────────────────┘
```

---

## Branch Strategy

```
main
├── branch/web      # Next.js web app
├── branch/mobile   # Expo React Native
└── branch/desktop  # Tauri desktop app
```

Mỗi platform phát triển trên branch riêng, push lên GitHub → auto-deploy lên FPT AI Factory.

---

## 1. SSH vào FPT AI Factory

### 1.1 Tạo GPU Container

1. Login https://console.fptcloud.com
2. **AI Factory** → **GPU Container** → **Create New**
3. Chọn template (Ubuntu 24.04 / PyTorch / CUDA)
4. Enable **SSH Terminal Access**
5. Thêm public key của bạn
6. Create → Copy SSH command

### 1.2 Kết nối VSCode

```bash
# Local: Thêm vào ~/.ssh/config
Host fpt-aifactory
    HostName <container-ip>
    User fptai
    Port 22
    IdentityFile ~/.ssh/your-key.pub

# VSCode: Cmd+Shift+P → "Remote-SSH: Connect to Host"
# Chọn "fpt-aifactory"
```

### 1.3 Development Workflow

```bash
# 1. SSH vào container (qua VSCode Remote SSH)
ssh fpt-aifactory

# 2. Clone repo
git clone https://github.com/ChauGiang-221/Gicungduoc.git
cd Gicungduoc

# 3. Checkout branch theo platform
git checkout -b web          # cho web app
git checkout -b mobile        # cho mobile app
git checkout -b desktop       # cho desktop app

# 4. Development trực tiếp trên cloud
# Backend
cd backend && pip install -r requirements.txt
uvicorn app.main:app --host 0.0.0.0 --port 8000 --reload

# Web (terminal mới)
cd frontend && npm install && npm run dev
```

---

## 2. FPT AI Inference API

### 2.1 API Endpoints

| Service | Base URL | Streaming |
|---------|----------|-----------|
| AI Marketplace | `https://mkp-api.fptcloud.com` | ✅ |
| AI Studio | `https://api.gptcloud.com/aiam/v1` | ✅ |

### 2.2 Authentication

```bash
# Get API Key: https://ai.fptcloud.com → My Account → My API Keys
Authorization: Bearer <API_KEY>
```

### 2.3 Python Integration

```python
# backend/app/services/ai/fpt_inference.py
import requests
import json
import os

class FPTInference:
    BASE_URL = "https://mkp-api.fptcloud.com"
    API_KEY = os.environ["AI_TOKEN"]
    MODEL = os.environ.get("MODEL_NAME", "SaoLa-Llama3.1-planner")

    def chat(self, messages: list[dict], stream: bool = True):
        headers = {
            "Content-Type": "application/json",
            "Authorization": f"Bearer {self.API_KEY}",
        }

        payload = {
            "model": self.MODEL,
            "messages": messages,
            "stream": stream,
            "temperature": 0.7,
        }

        response = requests.post(
            f"{self.BASE_URL}/chat/completions",
            headers=headers,
            json=payload,
            stream=stream,
        )

        return response.iter_lines() if stream else response.json()

    def chat_stream(self, messages: list[dict]):
        """SSE Streaming - yields content chunks"""
        for line in self.chat(messages, stream=True):
            if line:
                text = line.decode('utf-8')
                if text.startswith('data: '):
                    text = text[6:]
                if text == "[DONE]":
                    break
                try:
                    data = json.loads(text)
                    if content := data.get("content"):
                        yield content
                except json.JSONDecodeError:
                    pass
```

### 2.4 OpenAI SDK (Compatible!)

```python
from openai import OpenAI

client = OpenAI(
    api_key=os.environ["AI_TOKEN"],
    base_url="https://mkp-api.fptcloud.com"
)

# Streaming
for chunk in client.chat.completions.create(
    model="SaoLa-Llama3.1-planner",
    messages=[{"role": "user", "content": "Hello"}],
    stream=True
):
    print(chunk.choices[0].delta.content, end='', flush=True)
```

### 2.5 Environment Variables

```bash
# backend/.env
AI_TOKEN=your_fpt_api_key
MODEL_NAME=SaoLa-Llama3.1-planner
ALLOWED_ORIGINS=http://localhost:3000
```

---

## 3. Realtime AI (SSE Streaming)

### 3.1 Backend Endpoint

```python
# backend/app/api/routes/chat.py
from fastapi import APIRouter, Request
from fastapi.responses import StreamingResponse
from app.services.ai.fpt_inference import FPTInference
import json

router = APIRouter(prefix="/chat", tags=["chat"])

@router.post("")
async def chat(request: Request):
    body = await request.json()
    messages = body.get("messages", [])

    ai = FPTInference()

    def generate():
        for chunk in ai.chat_stream(messages):
            yield f"data: {json.dumps({'content': chunk})}\n\n"
        yield "data: [DONE]\n\n"

    return StreamingResponse(
        generate(),
        media_type="text/event-stream",
        headers={
            "Cache-Control": "no-cache",
            "X-Accel-Buffering": "no",
        },
    )
```

### 3.2 Frontend SSE Client

```typescript
// frontend/src/hooks/useSSE.ts
export function useSSE() {
  const [messages, setMessages] = useState<Message[]>([]);
  const [streaming, setStreaming] = useState(false);

  const send = async (content: string) => {
    const userMsg = { role: 'user', content };
    setMessages(prev => [...prev, userMsg]);
    setMessages(prev => [...prev, { role: 'assistant', content: '' }]);
    setStreaming(true);

    const response = await fetch('/api/chat', {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify({ messages: [...messages, userMsg] }),
    });

    const reader = response.body?.getReader();
    const decoder = new TextDecoder();

    while (reader) {
      const { done, value } = await reader.read();
      if (done) break;

      const chunk = decoder.decode(value);
      for (const line of chunk.split('\n')) {
        if (line.startsWith('data: ')) {
          const data = line.slice(6);
          if (data === '[DONE]') break;
          try {
            const { content } = JSON.parse(data);
            if (content) {
              setMessages(prev => {
                const updated = [...prev];
                const last = updated.length - 1;
                if (last >= 0 && updated[last].role === 'assistant') {
                  updated[last].content += content;
                }
                return updated;
              });
            }
          } catch {}
        }
      }
    }
    setStreaming(false);
  };

  return { messages, streaming, send };
}
```

---

## 4. VSCode Setup

### 4.1 Extensions

```json
// .vscode/extensions.json
{
  "recommendations": [
    "ms-python.python",
    "ms-toolsai.jupyter",
    "bradlc.vscode-tailwindcss",
    "dbaeumer.vscode-eslint",
    "esbenp.prettier-vscode",
    "expo.expo-tools",
    "tauri-apps.tauri-vscode",
    "rust-lang.rust-analyzer"
  ]
}
```

### 4.2 Debug Config

```json
// .vscode/launch.json
{
  "version": "0.2.0",
  "configurations": [
    {
      "name": "Backend (FastAPI)",
      "type": "python",
      "module": "uvicorn",
      "args": ["app.main:app", "--reload", "--host", "0.0.0.0", "--port", "8000"],
      "cwd": "${workspaceFolder}/backend"
    },
    {
      "name": "Frontend (Next.js)",
      "type": "node",
      "runtimeExecutable": "npm",
      "runtimeArgs": ["run", "dev"],
      "cwd": "${workspaceFolder}/frontend"
    }
  ]
}
```

---

## 5. Figma → Code Workflow

### 5.1 Design System

```
Figma Project
├── Shared
│   ├── Colors (primary, secondary, accent)
│   ├── Typography (font, sizes)
│   └── Icons
├── Web
│   ├── Home, Chat, Settings
├── Mobile
│   ├── Home, Chat, Profile
└── Desktop
    ├── Main Window, Settings
```

### 5.2 Export & Integrate

```bash
# 1. Design trên Figma
# 2. Export assets (SVG, PNG)
# 3. Copy vào project

# Web
cp figma/web/*.svg frontend/public/icons/

# Mobile
cp figma/mobile/*.png mobile/assets/

# Desktop
cp figma/desktop/*.svg desktop/public/icons/
```

### 5.3 Shared Design Tokens

```typescript
// shared/types/design.ts
export const tokens = {
  colors: {
    primary: '#3B82F6',
    secondary: '#64748B',
  },
  typography: {
    font: 'Inter, sans-serif',
    sizes: { sm: '14px', md: '16px', lg: '18px' },
  },
};
```

---

## 6. 3 Platform Implementation

### 6.1 Web (Next.js)

```bash
# Branch: web
git checkout -b web
cd frontend && npm install && npm run dev
```

```typescript
// frontend/src/app/api/chat/route.ts
export async function POST(req: Request) {
  const { messages } = await req.json();
  const response = await fetch('http://localhost:8000/chat', {
    method: 'POST',
    headers: { 'Content-Type': 'application/json' },
    body: JSON.stringify({ messages }),
  });
  return new Response(response.body, {
    headers: { 'Content-Type': 'text/event-stream' },
  });
}
```

### 6.2 Mobile (Expo)

```bash
# Branch: mobile
git checkout -b mobile
cd mobile && npx expo start
```

```typescript
// mobile/app/(tabs)/chat.tsx
import { useSSE } from '@/hooks/useSSE';

export default function ChatScreen() {
  const { messages, send } = useSSE();
  // ... UI components
}
```

### 6.3 Desktop (Tauri)

```bash
# Branch: desktop
git checkout -b desktop
cd desktop && npm run tauri dev
```

---

## 7. CI/CD Deployment

### 7.1 GitHub Actions

```yaml
# .github/workflows/deploy.yml
name: Deploy to FPT AI Factory

on:
  push:
    branches: [web, mobile, desktop]

jobs:
  deploy:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4

      - name: Deploy via SSH
        uses: appleboy/ssh-action@master
        with:
          host: ${{ secrets.FPT_HOST }}
          username: ${{ secrets.FPT_USER }}
          key: ${{ secrets.FPT_SSH_KEY }}
          script: |
            cd /opt/gicungduoc
            git pull origin ${{ github.ref_name }}
            # Restart appropriate service based on branch
            pm2 restart ${{ github.ref_name }}
```

### 7.2 GitHub Secrets

```
FPT_HOST=your-container-ip
FPT_USER=fptai
FPT_SSH_KEY=-----BEGIN OPENSSH PRIVATE KEY-----
```

---

## 8. Quick Start

```bash
# 1. Tạo GPU Container trên FPT AI Factory
# 2. SSH vào via VSCode Remote SSH

# 3. Clone repo
git clone https://github.com/ChauGiang-221/Gicungduoc.git
cd Gicungduoc

# 4. Chọn branch theo platform
git checkout web     # hoặc mobile, desktop

# 5. Setup backend
cd backend
python -m venv venv
source venv/bin/activate
pip install -r requirements.txt
cp .env.example .env  # Thêm AI_TOKEN

# 6. Chạy backend
uvicorn app.main:app --host 0.0.0.0 --port 8000

# 7. Frontend (terminal mới)
cd frontend && npm install && npm run dev

# 8. Push khi done
git add . && git commit -m "feat: ..."
git push origin web  # hoặc mobile, desktop
```

---

## 9. Todo List

- [ ] Tạo GPU Container (SSH enabled)
- [ ] VSCode Remote SSH connect
- [ ] Clone repo + checkout branch
- [ ] Setup FPT AI Inference API
- [ ] Implement SSE streaming
- [ ] Build Web/Mobile/Desktop
- [ ] Figma design → code
- [ ] Setup GitHub Actions
- [ ] Test deployment

---

## References

- [FPT AI Factory Docs](https://ai-docs.fptcloud.com/)
- [FPT AI Marketplace API](https://github.com/fpt-corp/ai-marketplace)
- [VSCode Remote SSH](https://code.visualstudio.com/docs/remote/ssh)
- [Expo](https://expo.dev/)
- [Tauri](https://tauri.app/)
