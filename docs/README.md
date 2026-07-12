# Gicungduoc x FPT AI Factory

## Tổng Quan

Dự án AI chatbot đa nền tảng, phát triển trên VSCode với FPT AI Factory làm cloud.

### Yêu Cầu

- **Development**: VSCode Remote SSH
- **Cloud**: FPT AI Factory (GPU Container)
- **UI/UX**: Figma → code
- **3 Nền tảng**: Web + Mobile + Desktop
- **AI Realtime**: SSE streaming, độ trễ thấp nhất
- **Deployment**: Push GitHub → Auto-deploy

---

## Kiến Trúc

```
┌─────────────────────────────────────────────────────────────────┐
│                    FPT AI Factory                                  │
│                    (GPU Container)                                │
│                                                                   │
│   VSCode Remote SSH ──────────────────────────────────────────►   │
│   (Development trên cloud)                                         │
│                                                                   │
│  ┌─────────────────────────────────────────────────────────────┐ │
│  │ Container                                                    │ │
│  │                                                              │ │
│  │   ┌──────────┐  ┌──────────┐  ┌──────────┐                │ │
│  │   │ Backend  │  │   Web    │  │  Mobile  │                │ │
│  │   │ FastAPI  │  │ Next.js  │  │   Expo   │                │ │
│  │   │   :8000  │  │  :3000   │  │  :19000  │                │ │
│  │   └────┬─────┘  └────┬─────┘  └────┬─────┘                │ │
│  │        └─────────────┼──────────────┘                       │ │
│  │                      │                                       │ │
│  │               ┌──────┴──────┐                               │ │
│  │               │  SSE Proxy  │                               │ │
│  │               │  Realtime    │                               │ │
│  │               └──────┬──────┘                               │ │
│  └──────────────────────┼──────────────────────────────────────┘ │
│                         │                                        │
│                         ▼                                        │
│              ┌─────────────────────┐                             │
│              │  FPT AI Inference   │                             │
│              │ mkp-api.fptcloud   │                             │
│              │    (SSE)           │                             │
│              └─────────────────────┘                             │
└─────────────────────────────────────────────────────────────────┘
```

---

## Branch Strategy

```
main
├── web       # Next.js
├── mobile    # Expo
└── desktop   # Tauri
```

Mỗi branch = 1 platform. Push lên GitHub → CI/CD deploy lên FPT AI Factory.

---

## Bắt Đầu

### 1. Tạo GPU Container

1. Login https://console.fptcloud.com
2. **AI Factory** → **GPU Container** → **Create New**
3. Template: **Ubuntu 24.04** hoặc **PyTorch**
4. Enable **SSH Terminal Access**
5. Thêm public key của bạn
6. Create → Copy SSH command

### 2. VSCode Remote SSH

```bash
# Local: Thêm vào ~/.ssh/config
Host fpt-aifactory
    HostName <container-ip>
    User fptai
    Port 22
    IdentityFile ~/.ssh/your-key.pub

# VSCode:
# 1. Install extension "Remote - SSH"
# 2. Cmd+Shift+P → "Remote-SSH: Connect to Host"
# 3. Chọn "fpt-aifactory"
```

### 3. Clone & Setup

```bash
# Trên container (via VSCode Terminal)
git clone https://github.com/ChauGiang-221/Gicungduoc.git
cd Gicungduoc

# Chọn branch theo platform
git checkout web      # hoặc mobile, desktop

# Setup
chmod +x scripts/*.sh 2>/dev/null || true
```

---

## Backend

### FPT AI Inference API

```python
# backend/app/services/ai.py
import requests
import json
import os

class FPTInference:
    BASE_URL = "https://mkp-api.fptcloud.com"
    API_KEY = os.environ["AI_TOKEN"]
    MODEL = os.environ.get("MODEL_NAME", "SaoLa-Llama3.1-planner")

    def chat_stream(self, messages: list[dict]):
        """SSE Streaming - yields content chunks"""
        headers = {
            "Content-Type": "application/json",
            "Authorization": f"Bearer {self.API_KEY}",
        }

        response = requests.post(
            f"{self.BASE_URL}/chat/completions",
            headers=headers,
            json={
                "model": self.MODEL,
                "messages": messages,
                "stream": True,
                "temperature": 0.7,
            },
            stream=True,
        )

        for line in response.iter_lines():
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

### SSE Endpoint

```python
# backend/app/api/routes/chat.py
from fastapi import APIRouter, Request
from fastapi.responses import StreamingResponse
from app.services.ai import FPTInference
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

### Environment Variables

```bash
# backend/.env
AI_TOKEN=your_fpt_api_key
MODEL_NAME=SaoLa-Llama3.1-planner
```

---

## Web (Next.js)

```bash
git checkout web
cd frontend
npm install
npm run dev
```

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
                updated[updated.length - 1].content += content;
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

## Mobile (Expo)

```bash
git checkout mobile
cd mobile
npx expo start
```

```typescript
// mobile/app/(tabs)/chat.tsx
import { useSSE } from '@/hooks/useSSE';

export default function ChatScreen() {
  const { messages, send } = useSSE();
  const [input, setInput] = useState('');

  return (
    <View style={styles.container}>
      <FlatList
        data={messages}
        renderItem={({ item }) => (
          <View style={item.role === 'user' ? styles.user : styles.assistant}>
            <Text>{item.content}</Text>
          </View>
        )}
      />
      <TextInput
        value={input}
        onChangeText={setInput}
        placeholder="Type a message..."
      />
      <Button title="Send" onPress={() => { send(input); setInput(''); }} />
    </View>
  );
}
```

---

## Desktop (Tauri)

```bash
git checkout desktop
cd desktop
npm run tauri dev
```

---

## Figma Workflow

### 1. Thiết Kế

```
Figma Project: Gicungduoc
├── Shared
│   ├── Colors (primary, secondary, accent)
│   ├── Typography (font, sizes, weights)
│   └── Icons (SVG)
├── Web
│   ├── Home
│   ├── Chat Interface
│   └── Settings
├── Mobile
│   ├── Home
│   ├── Chat
│   └── Profile
└── Desktop
    ├── Main Window
    └── Settings
```

### 2. Export

- Export SVG/PNG từ Figma
- Copy vào thư mục tương ứng:
  - `frontend/public/icons/`
  - `mobile/assets/`
  - `desktop/src/icons/`

### 3. Design Tokens

```typescript
// shared/types/design.ts
export const tokens = {
  colors: {
    primary: '#3B82F6',
    secondary: '#64748B',
    background: '#FFFFFF',
    text: '#1F2937',
  },
  typography: {
    font: 'Inter, sans-serif',
    sizes: {
      sm: '14px',
      md: '16px',
      lg: '18px',
      xl: '24px',
    },
  },
};
```

---

## VSCode Extensions

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

---

## Deployment

### GitHub Actions

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
            pm2 restart ${{ github.ref_name }}
```

### GitHub Secrets

```
FPT_HOST=container-ip
FPT_USER=fptai
FPT_SSH_KEY=-----BEGIN OPENSSH PRIVATE KEY-----
```

---

## References

- [FPT AI Factory Docs](https://ai-docs.fptcloud.com/)
- [FPT AI Marketplace API](https://github.com/fpt-corp/ai-marketplace)
- [VSCode Remote SSH](https://code.visualstudio.com/docs/remote/ssh)
- [Expo](https://expo.dev/)
- [Tauri](https://tauri.app/)
