# /hackathon-code — Generate Code for Hackathon

## Command
```
/hackathon-code [type] [description]
```

## Description
Generate code nhanh cho hackathon task. Dùng cho cả backend và frontend.

## Examples
```
/hackathon-code backend api-endpoint "POST /api/v1/analyze-image"
/hackathon-code frontend component "Image uploader with preview"
/hackathon-code ai prompt "Vietnamese sentiment analysis"
/hackathon-code fix "API returns 500 on large file upload"
```

## Types

### backend
Generate FastAPI endpoint, database model, hoặc service.
- Read backend/app/main.py để hiểu router structure
- Read backend/app/models/schemas.py để hiểu Pydantic models
- Read backend/app/services/ai_service.py để hiểu AI pattern

### frontend
Generate React component, page, hoặc API client.
- Read frontend/src/app/page.tsx để hiểu current structure
- Read frontend/src/components/ai-chat.tsx để hiểu component pattern
- Read frontend/src/lib/api.ts để hiểu API client pattern

### ai
Generate prompt template, system prompt, hoặc AI integration code.
- Read backend/app/services/ai_service.py để hiểu current AI pattern
- Reference docs/AI-HELPER.md cho Vietnamese NLP tips

### fix
Debug và fix bug.
- Read error message từ user
- Propose root cause + solution
- Provide fixed code

### deploy
Hướng dẫn deploy hoặc fix deployment issue.
- Platform: Vercel (frontend) hoặc Railway (backend)
- Check environment variables
- Verify build logs

## Instructions

Khi user gọi `/hackathon-code`:

1. **Identify type**: backend | frontend | ai | fix | deploy

2. **Read relevant context**:
   ```
   backend → backend/app/main.py, backend/app/api/
   frontend → frontend/src/app/, frontend/src/components/
   ai → backend/app/services/ai_service.py, docs/RESOURCES.md
   fix → ask for error message first
   deploy → docs/DEPLOYMENT.md
   ```

3. **Generate code**:
   - TypeScript cho frontend
   - Python cho backend
   - Match existing patterns trong codebase
   - Add docstrings/comments

4. **Provide file path**:
   - Nói rõ file nào cần tạo/sửa
   - Line numbers nếu sửa

5. **Test suggestion**:
   - Command để test
   - Expected output

## Response Format

```
# [Type]: [Description]

## 📁 File
`[path/to/file]`

## 💻 Code
```[language]
[code]
```

## 🧪 Test
```bash
[test command]
```

## ⚠️ Notes
[anything important]
```
