# Architecture Overview

## System Architecture

```txt
┌─────────────────┐
│   Next.js UI    │
│  (Vercel)       │
└────────┬────────┘
         │ HTTP/SSE
         │
┌────────▼────────┐
│  FastAPI        │
│  (Railway)      │
└────────┬────────┘
         │
    ┌────┴────┐
    │         │
┌───▼───┐ ┌──▼────┐
│AI APIs│ │Firebase│
│GPT/Cla│ │Firestore│
│ude/Gem│ │       │
└───────┘ └───────┘
```

## Components

### Frontend Layer
- **Next.js App Router**: Pages, layouts, routing.
- **Shadcn UI**: Reusable components.
- **API Client**: Typed calls to backend.
- **State Management**: React hooks + context.

### Backend Layer
- **FastAPI**: REST API server.
- **AI Service**: Unified interface cho OpenAI/Claude/Gemini.
- **Database Service**: Firestore CRUD operations.
- **Pydantic Models**: Request/response validation.

### AI Layer
- **OpenAI GPT-4o**: Fast reasoning, cost-effective.
- **Anthropic Claude**: Long context, analysis.
- **Google Gemini**: Multimodal, low-cost.
- **LangChain**: Optional orchestration.

### Database Layer
- **Firebase Firestore**: Real-time NoSQL.
- **Collections**: users, conversations, messages.

## Data Flow

1. User input trên frontend.
2. Frontend gọi API endpoint.
3. Backend validate request qua Pydantic.
4. AI Service gọi provider tương ứng.
5. Response stream back to frontend.
6. Firestore lưu conversation history.

## Security

- CORS whitelist origins.
- API keys trong environment variables.
- Input validation qua Pydantic.
- Firebase security rules.

## Scalability

- Stateless backend, easy horizontal scale.
- Firebase auto-scaling.
- Vercel edge network.
- CDN caching static assets.
