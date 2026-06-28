# API Endpoints

Base URL local: `http://localhost:8000`

## Health

```http
GET /health
```

Response:

```json
{
  "status": "healthy",
  "version": "1.0.0",
  "ai_providers": {
    "openai": true,
    "anthropic": true,
    "google": true
  }
}
```

## Providers

```http
GET /api/v1/ai/providers
```

Response:

```json
{
  "providers": {
    "openai": { "available": true, "model": "gpt-4o" },
    "anthropic": { "available": true, "model": "claude-3-5-sonnet-20241022" },
    "google": { "available": true, "model": "gemini-1.5-pro" }
  },
  "default": "openai"
}
```

## Chat

```http
POST /api/v1/ai/chat
Content-Type: application/json
```

Request:

```json
{
  "messages": [
    { "role": "system", "content": "Bạn là trợ lý AI hữu ích cho người Việt." },
    { "role": "user", "content": "Gợi ý ý tưởng AI cho nông nghiệp Việt Nam." }
  ],
  "provider": "openai",
  "temperature": 0.7,
  "max_tokens": 2000
}
```

Response:

```json
{
  "content": "...",
  "provider": "openai",
  "model": "gpt-4o",
  "tokens_used": null
}
```

## Streaming Chat

```http
POST /api/v1/ai/chat/stream
Content-Type: application/json
```

Response type: `text/event-stream`

Example chunks:

```txt
data: Xin chào

data: , tôi có thể giúp bạn...

data: [DONE]
```

## Error handling

- `400` — request sai format hoặc provider không hợp lệ.
- `500` — lỗi AI provider, thiếu API key, hoặc backend exception.

## JavaScript example

```ts
const res = await fetch(`${API_URL}/api/v1/ai/chat`, {
  method: 'POST',
  headers: { 'Content-Type': 'application/json' },
  body: JSON.stringify({
    messages: [{ role: 'user', content: 'Xin chào' }],
    provider: 'openai',
  }),
});

const data = await res.json();
console.log(data.content);
```
