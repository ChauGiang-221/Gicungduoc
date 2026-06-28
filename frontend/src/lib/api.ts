// AI Core Client
export type AIProvider = 'openai' | 'anthropic' | 'google';

export interface ChatMessage {
  role: 'system' | 'user' | 'assistant';
  content: string;
}

export interface ChatRequest {
  messages: ChatMessage[];
  provider?: AIProvider;
  stream?: boolean;
  temperature?: number;
  max_tokens?: number;
}

const API_URL = process.env.NEXT_PUBLIC_API_URL || 'http://localhost:8000';

export async function chat(request: ChatRequest) {
  const res = await fetch(`${API_URL}/api/v1/ai/chat`, {
    method: 'POST',
    headers: { 'Content-Type': 'application/json' },
    body: JSON.stringify(request),
  });

  if (!res.ok) throw new Error('API Request Failed');
  return res.json();
}
