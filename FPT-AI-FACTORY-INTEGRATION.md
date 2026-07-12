# Gicungduoc x FPT AI Factory - Kiến Trúc Mới

## Tổng Quan

Fork từ [VN AI Innovation Hackathon Starter](https://github.com/ChauGiang-221/Gicungduoc), định hướng lại để:
- **Cloud**: FPT AI Factory (thay Railway/Vercel)
- **Development**: VSCode Remote SSH
- **UI/UX**: Figma → code
- **3 Platforms**: Web + Mobile + Desktop
- **AI**: Realtime responses (SSE/WebSocket)
- **Deployment**: Push GitHub → Auto-deploy lên FPT AI Factory

---

## 1. Kiến Trúc Hệ Thống

```
┌──────────────────────────────────────────────────────────────────────┐
│                        FPT AI Factory Platform                          │
│                                                                      │
│  ┌────────────────────────────────────────────────────────────────┐ │
│  │                    GPU Container (SSH Ready)                     │ │
│  │  ┌──────────────┐  ┌──────────────┐  ┌──────────────┐         │ │
│  │  │   Web        │  │   Mobile     │  │   Desktop    │         │ │
│  │  │  (Next.js)   │  │  (Expo)      │  │  (Tauri)    │         │ │
│  │  │  :3000       │  │  :19000      │  │  :4000       │         │ │
│  │  └──────┬───────┘  └──────┬───────┘  └──────┬───────┘         │ │
│  │         │                  │                  │                  │ │
│  │         └──────────────────┼──────────────────┘                │ │
│  │                            ▼                                     │ │
│  │                   ┌────────────────┐                              │ │
│  │                   │  FastAPI       │                              │ │
│  │                   │  Backend       │                              │ │
│  │                   │  :8000         │                              │ │
│  │                   └────────┬───────┘                              │ │
│  └────────────────────────────│────────────────────────────────────┘ │
│                               │                                        │
│         ┌─────────────────────┼─────────────────────┐                │
│         ▼                     ▼                     ▼                │
│  ┌─────────────┐       ┌─────────────┐       ┌─────────────┐        │
│  │ FPT AI      │       │ Firebase   │       │  Redis      │        │
│  │ Inference   │       │ Firestore  │       │  Cache      │        │
│  │ API         │       │            │       │             │        │
│  │ api.gptcloud│       │            │       │             │        │
│  └─────────────┘       └─────────────┘       └─────────────┘        │
└──────────────────────────────────────────────────────────────────────┘
```

**FPT AI Factory Components:**
| Service | Purpose | Access |
|---------|---------|--------|
| GPU Container | Hosting Web/Mobile/Desktop apps + Backend | SSH ready (Ubuntu 24.04, CUDA, PyTorch templates) |
| AI Inference | LLM API (OpenAI-compatible) | `https://api.gptcloud.com/aiam/v1/chat/completions` |
| AI Studio | Fine-tune models, Model Hub | Web UI → Deploy as API Endpoint |
| Firestore | Database (users, conversations, messages) | Firebase SDK |
| Redis | Session cache, rate limiting | Optional |

---

## 2. Cấu Trúc Repository Mới

```
gicungduoc/
├── .claude/
│   └── commands/
├── .github/
│   └── workflows/
│       ├── deploy-web.yml      # Deploy Next.js
│       ├── deploy-mobile.yml   # Deploy Expo
│       └── deploy-desktop.yml  # Build Tauri
│
├── apps/
│   ├── web/                   # Next.js 15
│   │   ├── src/
│   │   │   ├── app/
│   │   │   ├── components/
│   │   │   └── lib/
│   │   ├── public/
│   │   ├── Dockerfile
│   │   └── vercel.json
│   │
│   ├── mobile/               # Expo (React Native)
│   │   ├── app/
│   │   ├── components/
│   │   ├── eas.json
│   │   └── app.json
│   │
│   └── desktop/              # Tauri (Rust + Web)
│       ├── src/
│       ├── src-tauri/
│       └── tauri.conf.json
│
├── services/
│   └── backend/              # FastAPI - AI Backend
│       ├── app/
│       │   ├── api/
│       │   │   ├── routes/
│       │   │   └── deps.py
│       │   ├── core/
│       │   │   ├── config.py
│       │   │   └── security.py
│       │   ├── models/
│       │   ├── schemas/
│       │   └── services/
│       │       └── ai/
│       │           ├── __init__.py
│       │           ├── fpt_factory.py    # FPT AI Factory integration
│       │           ├── openai.py
│       │           └── anthropic.py
│       └── main.py
│
├── shared/
│   └── types/                # Shared TypeScript types
│
├── figma/                    # Figma exports
│   ├── web/
│   ├── mobile/
│   └── desktop/
│
├── docker-compose.yml
├── CLAUDE.md
└── README.md
```

**Thay đổi quan trọng:**
- `frontend/` → `apps/web/`
- Thêm `apps/mobile/` (Expo)
- Thêm `apps/desktop/` (Tauri)
- Backend tách riêng `services/backend/`

---

## 3. FPT AI Factory Integration

### 3.1 Kết nối GPU Container qua SSH

```bash
# 1. Tạo GPU Container trên FPT AI Factory Console
#    - Enable "SSH Terminal Access"
#    - Thêm public key của bạn (max 10 keys)

# 2. Copy SSH command từ container details page
ssh username@container-ip.fptcloud.com

# 3. VSCode: Cmd+Shift+P → "Remote-SSH: Connect to Host"
# 4. Thêm vào ~/.ssh/config:
Host fpt-aifactory
    HostName <container-ip>
    User fptai
    Port 22
    IdentityFile ~/.ssh/fpt-aifactory-key.pub

# 5. Pre-configured templates: Ubuntu 24.04, CUDA, TensorFlow, PyTorch, Code Server
```

**Templates có sẵn:**
| Template | Use Case |
|----------|----------|
| Ubuntu 24.04 | General purpose |
| CUDA | GPU workloads |
| TensorFlow | TF models |
| PyTorch | PyTorch models |
| Code Server | VS Code in browser |

### 3.2 Backend Service (services/backend/)

**services/backend/app/services/ai/fpt_inference.py:**
```python
"""FPT AI Factory - AI Inference Integration
API: https://mkp-api.fptcloud.com/chat/completions
Supports streaming SSE!
"""

import json
import requests
from typing import AsyncGenerator
from app.core.config import settings


class FPTInferenceAI:
    """FPT AI Inference - OpenAI-compatible with streaming support"""

    BASE_URL = "https://mkp-api.fptcloud.com"

    def __init__(self):
        self.api_key = settings.AI_TOKEN   # From My Account → My API Keys
        self.model = settings.MODEL_NAME  # Model name (e.g., "SaoLa-Llama3.1-planner")

    def chat_complete(
        self,
        messages: list[dict],
        temperature: float = 0.7,
        max_tokens: int = 2048,
        stream: bool = False,
    ) -> dict | AsyncGenerator[str, None]:
        """Non-streaming or streaming chat completion"""

        headers = {
            "Content-Type": "application/json",
            "Authorization": f"Bearer {self.api_key}",
        }

        payload = {
            "model": self.model,
            "messages": messages,
            "temperature": temperature,
            "max_tokens": max_tokens,
            "stream": stream,
        }

        response = requests.post(
            f"{self.BASE_URL}/chat/completions",
            headers=headers,
            json=payload,
            stream=stream,
            timeout=60.0,
        )

        if stream:
            # SSE Streaming
            def event_generator():
                for line in response.iter_lines():
                    if line:
                        line_text = line.decode('utf-8')
                        if line_text.startswith('data: '):
                            line_text = line_text[6:]
                        if line_text == "[DONE]":
                            break
                        try:
                            chunk = json.loads(line_text)
                            if content := chunk.get("content"):
                                yield content
                            elif error := chunk.get("error"):
                                yield f"[ERROR: {error}]"
                        except json.JSONDecodeError:
                            pass

            return event_generator()
        else:
            response.raise_for_status()
            return response.json()

    # Alternative: Use OpenAI SDK directly (compatible!)
    # from openai import OpenAI
    # client = OpenAI(api_key=API_KEY, base_url="https://mkp-api.fptcloud.com")
    # response = client.chat.completions.create(model=MODEL, messages=[...], stream=True)
```

**services/backend/app/services/ai/fpt_studio.py:**
```python
"""FPT AI Studio - Model Fine-tuning & Deployment"""

class FPTAIStudio:
    """AI Studio workflow for custom model deployment"""

    @staticmethod
    def get_deployment_info(
        endpoint_url: str,
        model_id: str,
        token: str,
    ) -> dict:
        """Get deployment info from AI Studio → Model Hub

        Workflow:
        1. Fine-tune model in AI Studio → Data Hub + Fine-tuning Jobs
        2. Deploy via Model Hub (API Endpoint mode)
        3. Copy Endpoint URL, Model ID, Token
        """
        return {
            "endpoint": endpoint_url,  # e.g., https://api.gptcloud.com/aiam/v1
            "model": model_id,          # UUID from Model Hub
            "token": token,            # From My Account → My API Keys
        }
```

### 3.3 Environment Variables (services/backend/.env.example)

```bash
# FPT AI Inference (AI Marketplace) - PRIMARY
# Get from: https://ai.fptcloud.com → My Account → My API Keys
AI_TOKEN=your_fpt_api_key_here
MODEL_NAME=SaoLa-Llama3.1-planner  # Or other available models
AI_ENDPOINT=https://mkp-api.fptcloud.com

# Alternative FPT AI Inference (AI Studio - Model Hub)
# Get from: AI Studio → Model Hub → Deploy → Copy Endpoint/Model/Token
# AI_TOKEN_2=your_ai_studio_token_here
# MODEL_ID_2=your-model-uuid
# AI_STUDIO_ENDPOINT=https://api.gptcloud.com/aiam/v1

# Alternative AI Providers (fallback)
OPENAI_API_KEY=sk-...
ANTHROPIC_API_KEY=sk-ant-...
GOOGLE_API_KEY=...

# Database
FIREBASE_PROJECT_ID=your-project-id
FIREBASE_CREDENTIALS_PATH=./firebase-credentials.json

# Redis Cache (optional - session management)
REDIS_URL=redis://localhost:6379

# CORS Origins (your FPT GPU Container IPs/domains)
ALLOWED_ORIGINS=http://localhost:3000,http://localhost:19000,http://localhost:4000
```

---

## 4. VSCode Development Workflow

### 4.1 Remote SSH Setup

```bash
# Clone repo trên local
git clone https://github.com/YOUR_USERNAME/Gicungduoc.git

# SSH vào FPT AI Factory
ssh fpt-aifactory

# Clone repo trên cloud instance
git clone https://github.com/YOUR_USERNAME/Gicungduoc.git
cd Gicungduoc

# Development trực tiếp trên cloud
cd services/backend
uvicorn app.main:app --host 0.0.0.0 --port 8000 --reload
```

### 4.2 VSCode Extensions cho Development

```json
// .vscode/extensions.json
{
  "recommendations": [
    "ms-python.python",
    "ms-toolsai.jupyter",
    "bradlc.vscode-tailwindcss",
    "dbaeumer.vscode-eslint",
    "esbenp.prettier-vscode",
    "rust-lang.rust-analyzer",
    "tauri-apps.tauri-vscode",
    "expo.expo-tools",
    "firebase.firebase-loader"
  ]
}
```

### 4.3 Debugging Configuration

```json
// .vscode/launch.json
{
  "version": "0.2.0",
  "configurations": [
    {
      "name": "Python: FastAPI Backend",
      "type": "python",
      "request": "launch",
      "module": "uvicorn",
      "args": ["app.main:app", "--reload", "--host", "0.0.0.0", "--port", "8000"],
      "cwd": "${workspaceFolder}/services/backend",
      "env": {
        "PYTHONPATH": "${workspaceFolder}/services/backend"
      }
    },
    {
      "name": "Next.js Web",
      "type": "node",
      "request": "launch",
      "runtimeExecutable": "npm",
      "runtimeArgs": ["run", "dev"],
      "cwd": "${workspaceFolder}/apps/web"
    },
    {
      "name": "Tauri Desktop",
      "type": "tauri"
    }
  ]
}
```

---

## 5. Figma → Code Workflow

### 5.1 Thiết kế trên Figma

**Cấu trúc Figma:**
```
Gicungduoc Design System
├── Shared
│   ├── Colors
│   ├── Typography
│   └── Icons
├── Web App
│   ├── Home
│   ├── Chat Interface
│   └── Settings
├── Mobile App
│   ├── Home
│   ├── Chat
│   └── Profile
└── Desktop App
    ├── Main Window
    └── Settings
```

### 5.2 Figma → Code (3 nền tảng)

**Web (Tailwind + shadcn/ui):**
```bash
# Sử dụng Figma API hoặc plugin
# 1. Export từ Figma: File → Export → PNG/SVG
# 2. Hoặc dùng Figma REST API
npx @figma-export/cli export --file <file-key> --output-dir ./figma/web
```

**Mobile (React Native + Expo):**
```bash
# Export assets từ Figma
npx @figma-export/cli export --file <file-key> --output-dir ./figma/mobile/assets
```

**Desktop (Tauri):**
```bash
# Desktop dùng chung assets với web
# hoặc export riêng cho native components
```

### 5.3 Shared Design Tokens

```typescript
// shared/types/design.ts
export const designTokens = {
  colors: {
    primary: {
      50: '#f0f9ff',
      100: '#e0f2fe',
      // ... từ Figma
    },
    secondary: {
      // ...
    },
  },
  typography: {
    fontFamily: {
      sans: 'Inter, sans-serif',
    },
    fontSize: {
      xs: '0.75rem',
      sm: '0.875rem',
      base: '1rem',
      lg: '1.125rem',
      xl: '1.25rem',
    },
  },
  spacing: {
    1: '0.25rem',
    2: '0.5rem',
    4: '1rem',
    8: '2rem',
  },
} as const;
```

---

## 6. 3-Platform Architecture

### 6.1 Web (Next.js 15)

```typescript
// apps/web/src/app/api/chat/route.ts
import { NextRequest, NextResponse } from 'next/server';

export async function POST(req: NextRequest) {
  const { messages, stream } = await req.json();

  const response = await fetch(`${process.env.API_URL}/chat`, {
    method: 'POST',
    headers: { 'Content-Type': 'application/json' },
    body: JSON.stringify({ messages, stream: true }),
  });

  // SSE streaming
  return new Response(response.body, {
    headers: {
      'Content-Type': 'text/event-stream',
      'Cache-Control': 'no-cache',
      'Connection': 'keep-alive',
    },
  });
}
```

### 6.2 Mobile (Expo)

```typescript
// apps/mobile/app/(tabs)/chat.tsx
import { useState, useCallback } from 'react';
import { View, Text, FlatList, TextInput, Button } from 'react-native';
import { useSSE } from '@/hooks/useSSE';

export default function ChatScreen() {
  const [messages, setMessages] = useState<Message[]>([]);
  const [input, setInput] = useState('');
  const { send, isConnected } = useSSE('/api/chat');

  const handleSend = useCallback(async () => {
    const userMessage: Message = { role: 'user', content: input };
    setMessages(prev => [...prev, userMessage]);
    setInput('');

    await send({ messages: [...messages, userMessage] });
  }, [input, messages, send]);

  return (
    <View style={styles.container}>
      <FlatList
        data={messages}
        renderItem={({ item }) => (
          <View style={item.role === 'user' ? styles.userMsg : styles.aiMsg}>
            <Text>{item.content}</Text>
          </View>
        )}
      />
      <View style={styles.inputRow}>
        <TextInput value={input} onChangeText={setInput} style={styles.input} />
        <Button title="Send" onPress={handleSend} disabled={!isConnected} />
      </View>
    </View>
  );
}
```

### 6.3 Desktop (Tauri)

```rust
// apps/desktop/src-tauri/src/main.rs
use tauri::Manager;

fn main() {
    tauri::Builder::default()
        .setup(|app| {
            let window = app.get_window("main").unwrap();
            window.set_title("Gicungduoc - AI Chat");
            Ok(())
        })
        .run(tauri::generate_context!())
        .expect("error while running tauri application");
}
```

```typescript
// apps/desktop/src/components/Chat.tsx
import { useState, useEffect } from 'react';
import { fetchSSE } from '@/lib/api';

export function ChatWindow() {
  const [messages, setMessages] = useState<Message[]>([]);

  useEffect(() => {
    // SSE connection for real-time AI responses
    const eventSource = new EventSource('/api/chat');

    eventSource.onmessage = (event) => {
      const data = JSON.parse(event.data);
      setMessages(prev => [...prev, { role: 'assistant', content: data.content }]);
    };

    return () => eventSource.close();
  }, []);

  return <div className="chat-container">{/* ... */}</div>;
}
```

---

## 7. Realtime AI Response (SSE Streaming)

### 7.1 FPT AI Inference - Streaming Support ✅

**FPT AI Inference có hỗ trợ SSE streaming!**

- Endpoint: `POST https://mkp-api.fptcloud.com/chat/completions`
- Parameter: `stream: true`
- Response format:
  ```
  data: {"content": "partial-text"}
  data: {"content": "more-text"}
  ...
  data: [DONE]
  ```
- Error format: `data: {"error": "error-message"}`

### 7.2 Backend - FastAPI SSE Endpoint

```python
# services/backend/app/api/routes/chat.py
from fastapi import APIRouter, Request
from fastapi.responses import StreamingResponse
from app.services.ai.fpt_inference import FPTInferenceAI
import json

router = APIRouter(prefix="/chat", tags=["chat"])

@router.post("")
async def chat(request: Request):
    """SSE streaming chat endpoint"""
    body = await request.json()
    messages = body.get("messages", [])
    stream = body.get("stream", True)
    temperature = body.get("temperature", 0.7)

    ai = FPTInferenceAI()

    async def event_generator():
        # Non-blocking generator for FastAPI StreamingResponse
        for chunk in ai.chat_complete(
            messages=messages,
            stream=True,
            temperature=temperature,
        ):
            yield f"data: {json.dumps({'content': chunk})}\n\n"
        yield "data: [DONE]\n\n"

    return StreamingResponse(
        event_generator(),
        media_type="text/event-stream",
        headers={
            "Cache-Control": "no-cache",
            "Connection": "keep-alive",
            "X-Accel-Buffering": "no",
        },
    )
```

### 7.3 Frontend - SSE Client

```typescript
// apps/web/src/hooks/useSSE.ts
import { useState, useCallback, useRef } from 'react';

interface Message {
  role: 'user' | 'assistant';
  content: string;
}

export function useSSEChat() {
  const [messages, setMessages] = useState<Message[]>([]);
  const [isStreaming, setIsStreaming] = useState(false);
  const eventSourceRef = useRef<EventSource | null>(null);

  const sendMessage = useCallback(async (content: string) => {
    const userMessage: Message = { role: 'user', content };
    setMessages(prev => [...prev, userMessage]);

    // Add placeholder for assistant
    setMessages(prev => [...prev, { role: 'assistant', content: '' }]);
    setIsStreaming(true);

    try {
      const response = await fetch('/api/chat', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({
          messages: [...messages, userMessage],
          stream: true,
        }),
      });

      const reader = response.body?.getReader();
      const decoder = new TextDecoder();

      if (!reader) return;

      while (true) {
        const { done, value } = await reader.read();
        if (done) break;

        const chunk = decoder.decode(value);
        const lines = chunk.split('\n');

        for (const line of lines) {
          if (line.startsWith('data: ')) {
            const data = line.slice(6);
            if (data === '[DONE]') break;

            try {
              const parsed = JSON.parse(data);
              if (parsed.content) {
                // Append to last assistant message
                setMessages(prev => {
                  const updated = [...prev];
                  const lastIndex = updated.length - 1;
                  if (lastIndex >= 0 && updated[lastIndex].role === 'assistant') {
                    updated[lastIndex].content += parsed.content;
                  }
                  return updated;
                });
              }
            } catch (e) {
              // Skip non-JSON lines
            }
          }
        }
      }
    } finally {
      setIsStreaming(false);
    }
  }, [messages]);

  return { messages, isStreaming, sendMessage };
}
```

### 7.4 Alternative - OpenAI SDK (Compatible!)

```python
# Direct OpenAI SDK works with FPT AI!
from openai import OpenAI

client = OpenAI(
    api_key=os.environ["AI_TOKEN"],
    base_url="https://mkp-api.fptcloud.com"
)

# Non-streaming
response = client.chat.completions.create(
    model="SaoLa-Llama3.1-planner",
    messages=[{"role": "user", "content": "Hello"}]
)
print(response.choices[0].message.content)

# Streaming
for chunk in client.chat.completions.create(
    model="SaoLa-Llama3.1-planner",
    messages=[{"role": "user", "content": "Hello"}],
    stream=True
):
    if chunk.choices[0].delta.content:
        print(chunk.choices[0].delta.content, end='', flush=True)
```

---

## 8. GitHub Actions Deployment → FPT GPU Container

### 8.1 Backend Deploy (FastAPI)

```yaml
# .github/workflows/deploy-backend.yml
name: Deploy Backend to FPT GPU Container

on:
  push:
    branches: [main]
    paths: ['services/backend/**']

jobs:
  deploy:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4

      - name: Deploy to FPT GPU Container
        uses: appleboy/ssh-action@master
        with:
          host: ${{ secrets.FPT_GPU_HOST }}
          username: ${{ secrets.FPT_GPU_USER }}
          key: ${{ secrets.FPT_GPU_SSH_KEY }}
          script: |
            cd /opt/gicungduoc/services/backend
            git pull origin main
            source venv/bin/activate
            pip install -r requirements.txt
            pm2 restart backend || pm2 start uvicorn --name backend -- app.main:app --host 0.0.0.0 --port 8000
            pm2 save
```

### 8.2 Web Deploy (Next.js)

```yaml
# .github/workflows/deploy-web.yml
name: Deploy Web App to FPT GPU Container

on:
  push:
    branches: [main]
    paths: ['apps/web/**']

jobs:
  deploy:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4

      - name: Deploy to FPT GPU Container
        uses: appleboy/scp-action@master
        with:
          host: ${{ secrets.FPT_GPU_HOST }}
          username: ${{ secrets.FPT_GPU_USER }}
          key: ${{ secrets.FPT_GPU_SSH_KEY }}
          script: |
            cd /opt/gicungduoc/apps/web
            git pull origin main
            npm ci
            npm run build
            pm2 restart web || pm2 start npm --name web -- run start
            pm2 save
```

### 8.3 GitHub Secrets Configuration

```
FPT_GPU_HOST=<your-gpu-container-ip>
FPT_GPU_USER=fptai
FPT_GPU_SSH_KEY=-----BEGIN OPENSSH PRIVATE KEY-----\n...
```

### 8.4 Alternative: Docker Deploy (Dockerfile)

```dockerfile
# services/backend/Dockerfile
FROM python:3.11-slim

WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]
```

```yaml
# .github/workflows/deploy-docker.yml
name: Deploy Docker to FPT GPU Container

on:
  push:
    branches: [main]

jobs:
  deploy:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4

      - name: Build and Push Docker
        run: |
          docker build -t gicungduoc/backend:latest ./services/backend
          docker save gicungduoc/backend:latest | ssh ${{ secrets.FPT_GPU_HOST }} "docker load"

      - name: Deploy Container
        uses: appleboy/ssh-action@master
        with:
          host: ${{ secrets.FPT_GPU_HOST }}
          username: ${{ secrets.FPT_GPU_USER }}
          key: ${{ secrets.FPT_GPU_SSH_KEY }}
          script: |
            docker rm -f backend || true
            docker run -d --name backend --restart unless-stopped \
              -p 8000:8000 \
              -e AI_TOKEN=${{ secrets.FPT_AI_TOKEN }} \
              -e MODEL_ID=${{ secrets.FPT_MODEL_ID }} \
              gicungduoc/backend:latest
```

---

## 9. Branch Strategy (3 Platforms)

```
main
├── web/          # Web-specific features
├── mobile/       # Mobile-specific features
├── desktop/      # Desktop-specific features
└── services/     # Backend/shared features
```

### 9.1 Branch Naming

```bash
# Platform branches
git checkout -b web/chat-interface
git checkout -b mobile/offline-mode
git checkout -b desktop/system-tray

# Backend/shared
git checkout -b services/fpt-factory-integration
git checkout -b services/realtime-sse

# Hotfixes
git checkout -b hotfix/web-login-bug
```

### 9.2 Merge Strategy

| Branch | Target | Review |
|--------|--------|--------|
| `web/*` | `main` | 1 approval |
| `mobile/*` | `main` | 1 approval |
| `desktop/*` | `main` | 1 approval |
| `services/*` | `main` | 2 approvals |

---

## 10. Quick Start Guide

### 10.1 Local Development (VSCode Remote SSH)

```bash
# 1. SSH vào FPT AI Factory
ssh fpt-aifactory

# 2. Clone và setup
git clone https://github.com/YOUR_USERNAME/Gicungduoc.git
cd Gicungduoc

# 3. Backend
cd services/backend
python -m venv venv
source venv/bin/activate
pip install -r requirements.txt
uvicorn app.main:app --reload

# 4. Web (terminal mới)
cd apps/web
npm install
npm run dev

# 5. Mobile (terminal mới)
cd apps/mobile
npx expo start

# 6. Desktop (terminal mới)
cd apps/desktop
npm run tauri dev
```

### 10.2 Figma Design → Code

```bash
# 1. Export từ Figma plugin "Figma to Code"
# 2. Copy assets vào figma/ folders

# 3. Web components
cp figma/web/*.svg apps/web/public/icons/

# 4. Mobile assets
cp figma/mobile/*.png apps/mobile/assets/
```

---

## 11. Todo List

### Phase 1: Setup (1-2 ngày)
- [ ] Fork repo Gicungduoc gốc
- [ ] Tạo GPU Container trên FPT AI Factory (SSH enabled)
- [ ] Setup VSCode Remote SSH
- [ ] Clone repo vào GPU Container

### Phase 2: Backend (2-3 ngày)
- [ ] Setup Python venv + FastAPI
- [ ] Tích hợp FPT AI Inference API (`POST /v1/chat/completions`)
- [ ] WebSocket proxy cho realtime responses
- [ ] Test với model từ AI Studio

### Phase 3: Design (song song)
- [ ] Tạo Figma design system
- [ ] Export assets cho 3 platforms
- [ ] Setup shared design tokens

### Phase 4: Frontend (3-5 ngày)
- [ ] Web app (Next.js 15) - ưu tiên
- [ ] Mobile app (Expo)
- [ ] Desktop app (Tauri)

### Phase 5: CI/CD (1-2 ngày)
- [ ] Setup GitHub Actions deploy
- [ ] Docker build cho backend
- [ ] Test auto-deploy lên GPU Container

### Phase 6: Testing & Launch (2-3 ngày)
- [ ] End-to-end testing
- [ ] Performance optimization
- [ ] Demo & pitch materials

---

## 12. References

### FPT AI Factory Documentation
| Resource | URL |
|----------|-----|
| AI Docs (Main) | https://ai-docs.fptcloud.com/ |
| GPU Container | https://ai-docs.fptcloud.com/gpu-container/ |
| AI Inference | https://ai-docs.fptcloud.com/fpt-ai-inference/ |
| AI Studio | https://ai-docs.fptcloud.com/fpt-ai-studio/ |
| Sitemap | https://ai-docs.fptcloud.com/sitemap.md |

### FPT AI Inference API
| API | Base URL | Models |
|-----|----------|--------|
| **AI Marketplace** | `https://mkp-api.fptcloud.com` | DeepSeek-R1, Llama, Qwen, SaoLa, Gemma, Mistral |
| **AI Studio** | `https://api.gptcloud.com/aiam/v1` | Custom fine-tuned models |

**Streaming**: `stream: true` → SSE format `data: {"content": "..."}`

### GitHub Repositories
- [FPT AI Marketplace API Examples](https://github.com/fpt-corp/ai-marketplace) - Official API integration examples
- [VN AI Innovation Hackathon Starter](https://github.com/ChauGiang-221/Gicungduoc)

### Other Resources
- [VSCode Remote SSH](https://code.visualstudio.com/docs/remote/ssh)
- [Tauri Framework](https://tauri.app/)
- [Expo React Native](https://expo.dev/)
- [Next.js 15](https://nextjs.org/)
- [LiteLLM](https://docs.litellm.ai/) - Unified LLM interface
