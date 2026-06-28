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
  system_prompt?: string;
  user_id?: string;
}

export interface ChatResponse {
  content: string;
  provider: string;
  model: string;
  tokens_used?: number;
}

export interface Conversation {
  id: string;
  title: string;
  user_id: string;
  created_at: string;
  updated_at: string;
  message_count: number;
}
