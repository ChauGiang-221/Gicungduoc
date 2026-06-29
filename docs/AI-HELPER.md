# AI Coding Assistant - Prompts & Skills

> Bộ prompts và skills để dùng AI hỗ trợ code trong hackathon.
> Copy-paste vào Claude Code, Cursor, Copilot, ChatGPT.

---

## 🚀 Cách Dùng

### Claude Code (Recommended)
```bash
# Mở Claude Code trong project
cd Gicungduoc
claude

# Paste prompt từ file này
# AI sẽ đọc code hiện tại và implement
```

### ChatGPT / Claude Web
```bash
# Copy toàn bộ prompt
# Paste vào chat
# AI sẽ generate code cho bạn
```

### Cursor
```bash
# Cmd+K (Mac) hoặc Ctrl+K (Windows)
# Paste prompt
# Tab để accept suggestion
```

---

## 🎯 PROMPTS CHO HACKATHON

### PHẦN 1: BACKEND DEVELOPER

#### Prompt 1: Tạo API Endpoint Mới

```
Tôi đang làm hackathon với FastAPI + Python.

Tạo 1 API endpoint mới tại `backend/app/api/`:
- Path: POST /api/v1/[resource]
- Request body: [mô tả fields]
- Response: JSON với [mô tả]
- Validate với Pydantic
- Handle errors: 400 (bad request), 500 (server error)
- Lưu vào Firebase Firestore nếu cần

Context hiện tại:
- File router: backend/app/api/
- Models: backend/app/models/schemas.py
- Database: backend/app/services/database.py
- AI service: backend/app/services/ai_service.py

Format: Chỉ trả về code Python, không giải thích.
```

#### Prompt 2: Thêm AI Provider Mới

```
Thêm 1 AI provider vào backend/app/services/ai_service.py:

Provider: [tên - ví dụ: Mistral, Groq, Local LLM]

Yêu cầu:
- Method `_chat_[provider]` với streaming support
- Update `_get_model()` để return model name
- Update type hint `AIProvider` literal
- Viết docstring cho method mới

File hiện tại dùng:
- openai.AsyncOpenAI
- anthropic.AsyncAnthropic
- google.generativeai

Format: Chỉ trả về code mới cần thêm, có context.
```

#### Prompt 3: Tạo Database Model

```
Tạo Pydantic model cho Firebase Firestore:

Collection: [tên collection]
Fields:
- id: str (auto-generated UUID)
- user_id: str (required)
- [field1]: [type] (required/optional)
- [field2]: [type] (required/optional)
- created_at: datetime
- updated_at: datetime

Yêu cầu:
- Base model với common fields (id, created_at, updated_at)
- Create/Update schemas riêng
- Validation với @field_validator nếu cần
- Tạo method trong database service để CRUD

File: backend/app/models/schemas.py
File: backend/app/services/database.py

Format: Chỉ trả về code.
```

#### Prompt 4: Fix API Lỗi

```
Debug API endpoint không hoạt động:

Endpoint: POST /api/v1/[resource]
Error: [mô tả lỗi]

Tôi đang dùng:
- FastAPI
- Pydantic v2
- Firebase Firestore
- Async/await pattern

Đã thử:
1. [cách 1]
2. [cách 2]

Hướng dẫn tôi:
1. Nguyên nhân có thể
2. Cách fix
3. Code cụ thể để thêm/sửa
```

---

### PHẦN 2: FRONTEND DEVELOPER

#### Prompt 5: Tạo Component Mới

```
Tạo React component mới cho Next.js 15 (App Router):

Component: [tên component]
Props:
- [prop1]: [type] (required)
- [prop2]: [type] (optional)

UI:
- [mô tả UI]
- Dùng Tailwind CSS classes
- Responsive (mobile-first)

Design System hiện tại:
- Colors: primary (blue), secondary (gray), destructive (red)
- Tailwind config: tailwind.config.js
- Components: src/components/ui/

Yêu cầu:
- TypeScript
- 'use client' directive nếu cần interactivity
- Props interface
- Handle loading/error/empty states
- Export named component

Format: Chỉ trả về JSX code.
```

#### Prompt 6: Tạo API Client

```
Tạo TypeScript API client cho endpoint:

Endpoint: [POST/GET] /api/v1/[resource]
Request: [mô tả]
Response: [mô tả]

File: frontend/src/lib/api.ts

Yêu cầu:
- Function với proper typing
- Handle errors (try/catch)
- Return typed response
- Có loading state helper nếu cần
- Dùng axios hoặc fetch

Format: Chỉ trả về TypeScript code.
```

#### Prompt 7: Tạo Form với Validation

```
Tạo React form với validation cho Next.js:

Form fields:
- [field1]: text, required, min 3 chars
- [field2]: email, required, valid email
- [field3]: number, required, min 0, max 100
- [field4]: select, required, options: [A, B, C]

UI:
- Labels + input fields
- Error messages bên dưới mỗi field
- Submit button (disabled khi invalid)
- Loading state khi submit

Tech stack:
- React Hook Form
- Zod validation
- Tailwind CSS
- Shadcn/ui components

File: src/components/[form-name].tsx

Format: Chỉ trả về complete component code.
```

#### Prompt 8: Thêm Animation

```
Thêm animation vào Next.js component:

Component: [tên]
Animation type: [fade-in / slide-up / scale / bounce]
Trigger: [on mount / on hover / on click]
Duration: [300ms / 500ms]

Dùng:
- Framer Motion
- Tailwind

Format: Chỉ trả về code cần thêm vào component.
```

---

### PHẦN 3: AI INTEGRATION

#### Prompt 9: Tạo Prompt Template

```
Tạo prompt template cho use case:

Use case: [mô tả]
Input: [user input]
Output mong đợi: [mô tả]

Yêu cầu:
- System prompt rõ ràng, dài 50-100 words
- User prompt template với placeholders: {input}, {context}
- Few-shot examples (2-3 examples)
- Output format: [JSON/markdown/plain text]

Context về Vietnamese:
- [nếu cần Vietnamese language support]

Format: Trả về system prompt + user template.
```

#### Prompt 10: Xử Lý AI Response

```
Xử lý AI response cho frontend:

AI returns: [mô tả response format]
Frontend display: [mô tả UI]

Yêu cầu:
- Parse streaming response (SSE)
- Handle markdown rendering (ví dụ: ### headers, **bold**)
- Handle code blocks với syntax highlighting
- Error states: rate limit, API error, timeout
- Loading indicator

Tech:
- Next.js 15
- Tailwind
- markdown-to-jsx hoặc react-markdown

Format: Chỉ trả về handler code.
```

#### Prompt 11: Rate Limiting & Cost Optimization

```
Implement rate limiting cho AI calls:

Requirements:
- [X] requests per minute per user
- [Y] requests per day per user
- Fallback: [mô tả]

Dùng:
- Redis (ioredis) hoặc
- In-memory cache ( Map)

Code nên có:
- Rate limit middleware
- Cost tracking
- Auto-switch provider khi limit hit

File: backend/app/services/rate_limiter.py

Format: Chỉ trả về code.
```

---

### PHẦN 4: UI/UX DESIGNER

#### Prompt 12: Chuyển Figma → Code

```
Chuyển Figma design thành React code:

Screenshot: [mô tả hoặc paste image]

Design specs:
- Spacing: [X]px
- Colors: [hex codes]
- Font: [family, sizes]
- Border radius: [X]px

Dùng:
- Next.js 15
- Tailwind CSS
- Shadcn/ui components

Format: Chỉ trả về JSX component.
```

#### Prompt 13: Tạo Responsive Layout

```
Tạo responsive layout:

Desktop: [mô tả]
Tablet: [mô tả]
Mobile: [mô tả]

Breakpoints:
- Mobile: < 640px
- Tablet: 640px - 1024px
- Desktop: > 1024px

Dùng:
- Tailwind responsive prefixes (md:, lg:)
- Flexbox/Grid

Format: Chỉ trả về layout code.
```

#### Prompt 14: Design System Token

```
Generate design tokens từ Figma specs:

Colors:
- Primary: [hex]
- Secondary: [hex]
- Accent: [hex]
- Background: [hex]
- Text: [hex]

Typography:
- Heading: [font, size, weight]
- Body: [font, size, weight]
- Code: [font, size, weight]

Spacing scale: [4, 8, 12, 16, 24, 32, 48, 64]

Output:
1. tailwind.config.js updates
2. CSS variables

Format: Chỉ trả về config code.
```

---

### PHẦN 5: PITCH & PRESENTATION

#### Prompt 15: Viết Pitch Script

```
Viết script cho slide [số]:

Slide content: [mô tả]
Time: [X] seconds

Audience: Vietnamese judges
Tone: Professional nhưng có cảm xúc
Hook: [có/không]

Format:
```
[Thời gian] [Nội dung nói]
[Pause] [Body language]
```

Yêu cầu:
- Ngắn gọn, đi thẳng vào vấn đề
- Có số liệu cụ thể
- Transition words để nối slide
```

#### Prompt 16: Tạo Q&A Answers

```
Tạo câu trả lời cho câu hỏi BGK:

Câu hỏi: [câu hỏi]
Thời gian trả lời: 15-30 giây

Context:
- Product: [tên, mô tả ngắn]
- Tech: [stack đang dùng]
- Competition: [đối thủ]
- Traction: [metrics]

Yêu cầu:
- Trả lời ngắn gọn (3-5 sentences)
- Có data/supporting evidence
- Tự tin, không phòng thủ
- Chuyển hướng về điểm mạnh nếu câu hỏi khó

Format: Trả lời + điểm cần nhấn mạnh
```

#### Prompt 17: Tạo Demo Script

```
Viết demo script cho feature:

Feature: [mô tả]
Steps:
1. [bước 1]
2. [bước 2]
3. [bước 3]

Timestamps:
- Setup: 10s
- Action: 30s
- Result: 10s

Backup: [nếu fail]

Talking points cho mỗi bước:
- Giải thích user flow
- Highlight "wow moment"
- Transition sentence

Format: Table với timestamp, action, talking point
```

---

### PHẦN 6: DEPLOYMENT & OPS

#### Prompt 18: Fix Deployment Lỗi

```
Fix deployment error:

Platform: [Vercel / Railway / Render]
Error: [log lỗi]

Setup:
- Frontend: Next.js 15
- Backend: FastAPI
- Database: Firebase

Đã thử:
1. [cách 1]

Hướng dẫn:
1. Nguyên nhân
2. Fix
3. Deploy lại
```

#### Prompt 19: Setup Environment Variables

```
Hướng dẫn setup environment variables:

Platform: [Vercel / Railway / Render]

Variables cần thiết:

Frontend (.env.local):
- NEXT_PUBLIC_API_URL: [production backend URL]

Backend (.env):
- OPENAI_API_KEY: [key]
- ANTHROPIC_API_KEY: [key]
- GOOGLE_API_KEY: [key]
- FIREBASE_PROJECT_ID: [id]
- FIREBASE_CREDENTIALS: [json]

Format:
1. Cách lấy từng biến
2. Cách set trên platform
3. Verify
```

#### Prompt 20: Optimize Performance

```
Optimize performance cho:

Target: [frontend/backend/database]
Issue: [mô tả vấn đề]

Current setup:
- [tech stack]
- [metrics hiện tại]

Yêu cầu:
- [target metrics]

Suggestions:
1. [cách 1]
2. [cách 2]
3. [cách 3]

Code examples cho từng suggestion.
```

---

## 📋 QUICK REFERENCE

### Copy-Paste Templates

#### Template: Claude Code Session Start
```
Tôi đang làm hackathon. Project structure:

frontend/  - Next.js 15 + Tailwind + Shadcn UI
backend/   - FastAPI + OpenAI/Claude/Gemini
docs/     - Documentation

Nhiệm vụ: [mô tả]
Priority: [HIGH/MEDIUM]
Deadline: [thời gian]

Giúp tôi [action cụ thể]. Chỉ trả về code cần thêm.
```

#### Template: Fix Bug
```
Bug: [mô tả]
File: [đường dẫn]
Error: [error message]

Context:
- Tech stack: [list]
- Đã thử: [cách]

Fix: [nguyên nhân + solution]
```

#### Template: Code Review
```
Review code từ [file/branch]:

1. Best practices - có follow không?
2. Performance - có bottleneck không?
3. Security - có vulnerabilities không?
4. Error handling - đủ chưa?

Chỉ trả về issues + suggested fixes.
```

---

## 🎯 COMMAND SCRIPTS

### Quick Commands

```bash
# ===== BACKEND =====
# Chạy backend
cd backend && venv\Scripts\activate && uvicorn app.main:app --reload

# Test endpoint
curl -X POST http://localhost:8000/api/v1/ai/chat \
  -H "Content-Type: application/json" \
  -d '{"messages":[{"role":"user","content":"Hello"}],"provider":"openai"}'

# Check API docs
start http://localhost:8000/docs

# ===== FRONTEND =====
# Chạy frontend
cd frontend && npm run dev

# Build production
npm run build

# ===== GIT =====
# Commit và push nhanh
git add -A && git commit -m "feat: [mô tả]" && git push

# Check status
git status --short

# ===== DEPLOY =====
# Deploy frontend
vercel --prod

# Deploy backend
cd backend && railway up

# ===== AI HELPERS =====
# Test OpenAI
python -c "from openai import OpenAI; c=OpenAI(); print('OK')"

# Test Claude
python -c "from anthropic import Anthropic; c=Anthropic(); print('OK')"

# Check API keys
grep -r "API_KEY" backend/.env | sed 's/=.*/=***/'
```

---

## ⚡ PROMPTS CHO TỪNG TEAM ROLE

### Backend Developer

```
[System: Backend Expert]
Tôi là Backend Developer cho VN AI Innovation Hackathon.
Stack: Python, FastAPI, Firebase Firestore, OpenAI/Claude/Gemini APIs
Hỗ trợ tôi với:
1. [Task cụ thể]
2. [Task cụ thể]
3. [Task cụ thể]

Format: Code-first, giải thích ngắn gọn.
```

### Frontend Developer

```
[System: Frontend Expert]
Tôi là Frontend Developer cho VN AI Innovation Hackathon.
Stack: Next.js 15, React, TypeScript, Tailwind CSS, Shadcn UI
Hỗ trợ tôi với:
1. [Task cụ thể]
2. [Task cụ thể]
3. [Task cụ thể]

Format: Code-first, JSX only.
```

### UI/UX Designer

```
[System: Design Expert]
Tôi cần hỗ trợ design cho VN AI Innovation Hackathon.
Cần:
1. [Yêu cầu cụ thể]
2. [Yêu cầu cụ thể]
3. [Yêu cầu cụ thể]

Design system: Tailwind, Shadcn UI, mobile-first
Format: Figma specs hoặc JSX code.
```

---

## 📁 File Này Dùng Như Thế Nào

1. **Mở file**: `docs/AI-HELPER.md`
2. **Copy prompt** bạn cần
3. **Paste** vào Claude Code / ChatGPT / Cursor
4. **Thay thế** placeholders: `[...]`
5. **Run** và copy code vào project
6. **Commit** với git

---

**Chúc code suôn sẻ! 🚀**
