"""
VN AI Innovation Hackathon - Multi-provider AI Service

Supports: OpenAI, Anthropic Claude, Google Gemini
"""
from typing import AsyncGenerator, Literal
from openai import AsyncOpenAI
from anthropic import AsyncAnthropic
import google.generativeai as genai

from app.config import get_settings

settings = get_settings()

AIProvider = Literal["openai", "anthropic", "google"]


class AIService:
    def __init__(self):
        self.openai_client = AsyncOpenAI(api_key=settings.OPENAI_API_KEY)
        self.anthropic_client = AsyncAnthropic(api_key=settings.ANTHROPIC_API_KEY)

        if settings.GOOGLE_API_KEY:
            genai.configure(api_key=settings.GOOGLE_API_KEY)

    def _get_model(self, provider: AIProvider) -> str:
        return {
            "openai": settings.OPENAI_MODEL,
            "anthropic": settings.ANTHROPIC_MODEL,
            "google": settings.GOOGLE_MODEL,
        }[provider]

    async def chat(
        self,
        messages: list[dict[str, str]],
        provider: AIProvider = "openai",
        stream: bool = False,
        temperature: float | None = None,
        max_tokens: int | None = None,
        system_prompt: str | None = None,
    ) -> str | AsyncGenerator[str, None]:
        temperature = temperature or settings.TEMPERATURE
        max_tokens = max_tokens or settings.MAX_TOKENS

        if provider == "openai":
            return await self._chat_openai(messages, stream, temperature, max_tokens)
        elif provider == "anthropic":
            return await self._chat_anthropic(messages, stream, temperature, max_tokens, system_prompt)
        elif provider == "google":
            return await self._chat_google(messages, stream, temperature, max_tokens, system_prompt)
        raise ValueError(f"Unknown provider: {provider}")

    # ===== OpenAI =====
    async def _chat_openai(self, messages, stream, temperature, max_tokens):
        if stream:
            return self._stream_openai(messages, temperature, max_tokens)

        response = await self.openai_client.chat.completions.create(
            model=self._get_model("openai"),
            messages=messages,
            temperature=temperature,
            max_tokens=max_tokens,
        )
        return response.choices[0].message.content

    async def _stream_openai(self, messages, temperature, max_tokens):
        stream = await self.openai_client.chat.completions.create(
            model=self._get_model("openai"),
            messages=messages,
            temperature=temperature,
            max_tokens=max_tokens,
            stream=True,
        )
        async for chunk in stream:
            if chunk.choices[0].delta.content:
                yield chunk.choices[0].delta.content

    # ===== Anthropic =====
    async def _chat_anthropic(self, messages, stream, temperature, max_tokens, system_prompt):
        system = system_prompt or ""
        conversation = [m for m in messages if m["role"] != "system"]
        if not system:
            for m in messages:
                if m["role"] == "system":
                    system = m["content"]
                    break

        if stream:
            return self._stream_anthropic(system, conversation, temperature, max_tokens)

        response = await self.anthropic_client.messages.create(
            model=self._get_model("anthropic"),
            system=system,
            messages=conversation,
            temperature=temperature,
            max_tokens=max_tokens,
        )
        return response.content[0].text

    async def _stream_anthropic(self, system, conversation, temperature, max_tokens):
        async with self.anthropic_client.messages.stream(
            model=self._get_model("anthropic"),
            system=system,
            messages=conversation,
            temperature=temperature,
            max_tokens=max_tokens,
        ) as stream:
            async for text in stream.text_stream:
                yield text

    # ===== Google Gemini =====
    async def _chat_google(self, messages, stream, temperature, max_tokens, system_prompt):
        model = genai.GenerativeModel(self._get_model("google"))
        prompt = self._format_google_messages(messages, system_prompt)
        config = genai.GenerationConfig(
            temperature=temperature,
            max_output_tokens=max_tokens,
        )

        if stream:
            return self._stream_google(model, prompt, config)

        response = await model.generate_content_async(prompt, generation_config=config)
        return response.text

    async def _stream_google(self, model, prompt, config):
        response = await model.generate_content_async(
            prompt, generation_config=config, stream=True
        )
        async for chunk in response:
            if chunk.text:
                yield chunk.text

    def _format_google_messages(self, messages: list[dict], system_prompt: str | None) -> str:
        parts = []
        if system_prompt:
            parts.append(f"Instructions: {system_prompt}")
        for msg in messages:
            role = msg["role"]
            content = msg["content"]
            if role == "system":
                parts.append(f"Instructions: {content}")
            elif role == "user":
                parts.append(f"User: {content}")
            elif role == "assistant":
                parts.append(f"Assistant: {content}")
        return "\n\n".join(parts)


ai_service = AIService()
