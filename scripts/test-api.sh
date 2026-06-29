#!/bin/bash
# test-api.sh — Test all API endpoints

BASE_URL="${1:-http://localhost:8000}"

echo "🧪 Testing API Endpoints"
echo "========================="
echo "Base URL: $BASE_URL"
echo ""

# Health check
echo "1️⃣  GET /health"
curl -s "$BASE_URL/health" | jq . 2>/dev/null || curl -s "$BASE_URL/health"
echo ""

# List providers
echo ""
echo "2️⃣  GET /api/v1/ai/providers"
curl -s "$BASE_URL/api/v1/ai/providers" | jq . 2>/dev/null || curl -s "$BASE_URL/api/v1/ai/providers"
echo ""

# Test chat (non-streaming)
echo ""
echo "3️⃣  POST /api/v1/ai/chat (OpenAI)"
curl -s -X POST "$BASE_URL/api/v1/ai/chat" \
  -H "Content-Type: application/json" \
  -d '{"messages":[{"role":"user","content":"Hello, introduce yourself in Vietnamese"}],"provider":"openai","max_tokens":100}' | jq . 2>/dev/null || echo "❌ Request failed"
echo ""

echo "✅ API Tests Complete"
