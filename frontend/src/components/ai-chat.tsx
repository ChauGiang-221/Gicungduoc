'use client';

import { useState, useRef, useEffect } from 'react';
import { Button } from '@/components/ui/button';
import type { AIProvider, ChatMessage } from '@/lib/api';

const API_URL = process.env.NEXT_PUBLIC_API_URL || 'http://localhost:8000';

export function AIChat() {
  const [input, setInput] = useState('');
  const [provider, setProvider] = useState<AIProvider>('openai');
  const [messages, setMessages] = useState<ChatMessage[]>([]);
  const [isLoading, setIsLoading] = useState(false);
  const bottomRef = useRef<HTMLDivElement>(null);

  useEffect(() => {
    bottomRef.current?.scrollIntoView({ behavior: 'smooth' });
  }, [messages]);

  const sendMessage = async (e: React.FormEvent) => {
    e.preventDefault();
    if (!input.trim() || isLoading) return;

    const userMsg: ChatMessage = { role: 'user', content: input };
    const newMessages = [...messages, userMsg];
    setMessages(newMessages);
    setInput('');
    setIsLoading(true);

    try {
      const res = await fetch(`${API_URL}/api/v1/ai/chat/stream`, {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ messages: newMessages, provider, stream: true }),
      });

      if (!res.ok || !res.body) throw new Error('Request failed');

      const reader = res.body.getReader();
      const decoder = new TextDecoder();
      let assistantContent = '';
      setMessages((prev) => [...prev, { role: 'assistant', content: '' }]);

      while (true) {
        const { done, value } = await reader.read();
        if (done) break;
        const chunk = decoder.decode(value);
        for (const line of chunk.split('\n\n')) {
          if (line.startsWith('data: ')) {
            const data = line.slice(6);
            if (data === '[DONE]') break;
            assistantContent += data;
            setMessages((prev) => {
              const updated = [...prev];
              updated[updated.length - 1] = { role: 'assistant', content: assistantContent };
              return updated;
            });
          }
        }
      }
    } catch {
      setMessages((prev) => [...prev, { role: 'assistant', content: 'Lỗi: Không kết nối được backend. Kiểm tra API đang chạy chưa.' }]);
    } finally {
      setIsLoading(false);
    }
  };

  const providers: { id: AIProvider; label: string }[] = [
    { id: 'openai', label: 'GPT-4' },
    { id: 'anthropic', label: 'Claude' },
    { id: 'google', label: 'Gemini' },
  ];

  return (
    <div className="flex flex-col h-[600px] max-w-3xl mx-auto border rounded-xl bg-white dark:bg-slate-800 shadow-sm">
      <div className="flex gap-2 p-4 border-b">
        {providers.map((p) => (
          <Button
            key={p.id}
            variant={provider === p.id ? 'default' : 'outline'}
            size="sm"
            onClick={() => setProvider(p.id)}
          >
            {p.label}
          </Button>
        ))}
      </div>

      <div className="flex-1 overflow-y-auto p-4 space-y-3">
        {messages.length === 0 && (
          <p className="text-center text-slate-400 mt-8">Bắt đầu trò chuyện với AI...</p>
        )}
        {messages.map((msg, i) => (
          <div
            key={i}
            className={`p-3 rounded-lg max-w-[85%] ${
              msg.role === 'user'
                ? 'bg-blue-100 dark:bg-blue-900 ml-auto'
                : 'bg-slate-100 dark:bg-slate-700'
            }`}
          >
            <div className="text-xs font-semibold mb-1 opacity-60">
              {msg.role === 'user' ? 'Bạn' : 'AI'}
            </div>
            <div className="whitespace-pre-wrap text-sm">{msg.content}</div>
          </div>
        ))}
        <div ref={bottomRef} />
      </div>

      <form onSubmit={sendMessage} className="flex gap-2 p-4 border-t">
        <input
          value={input}
          onChange={(e) => setInput(e.target.value)}
          placeholder="Nhập câu hỏi..."
          disabled={isLoading}
          className="flex-1 px-4 py-2 border rounded-md bg-background focus:outline-none focus:ring-2 focus:ring-ring"
        />
        <Button type="submit" disabled={isLoading || !input.trim()}>
          {isLoading ? '...' : 'Gửi'}
        </Button>
      </form>
    </div>
  );
}
