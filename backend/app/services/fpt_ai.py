"""FPT AI Inference service with SSE streaming support."""
import json
import os
import requests
from app.config import get_settings


class FPTInference:
    """FPT AI Inference - OpenAI-compatible API with SSE streaming."""

    def __init__(self):
        settings = get_settings()
        self.api_key = settings.AI_TOKEN
        self.model = settings.MODEL_NAME
        self.endpoint = settings.AI_ENDPOINT

    def chat_complete(
        self,
        messages: list[dict],
        temperature: float = 0.7,
        max_tokens: int = 2048,
        stream: bool = False,
    ) -> dict:
        """Non-streaming chat completion."""
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
            f"{self.endpoint}/chat/completions",
            headers=headers,
            json=payload,
            timeout=60,
        )

        response.raise_for_status()
        return response.json()

    def chat_stream(self, messages: list[dict], temperature: float = 0.7, max_tokens: int = 2048):
        """SSE Streaming - yields content chunks."""
        headers = {
            "Content-Type": "application/json",
            "Authorization": f"Bearer {self.api_key}",
        }

        payload = {
            "model": self.model,
            "messages": messages,
            "temperature": temperature,
            "max_tokens": max_tokens,
            "stream": True,
        }

        response = requests.post(
            f"{self.endpoint}/chat/completions",
            headers=headers,
            json=payload,
            stream=True,
            timeout=60,
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
                    elif data.get("error"):
                        yield f"[ERROR: {data['error']}]"
                except json.JSONDecodeError:
                    pass
