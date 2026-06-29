# /hackathon-start — Initialize Hackathon Project

## Command
```
/hackathon-start [problem] [tech-focus]
```

## Description
Initialize project với task đầu tiên cho hackathon. Đọc CLAUDE.md và PRE-HACKATHON.md trước.

## Examples
```
/hackathon-start healthcare ai-diagnosis
/hackathon-start education smart-tutoring
/hackathon-start agriculture crop-detection
```

## Instructions

Khi user gọi `/hackathon-start`:

1. **Read context files**:
   - CLAUDE.md — project structure
   - docs/PRE-HACKATHON.md — checklist
   - docs/RESOURCES.md — winning strategies

2. **Understand problem**:
   - [problem] = domain (healthcare, education, agriculture, finance, environment)
   - [tech-focus] = AI feature chính

3. **Setup checklist**:
   - Verify backend chạy được: `uvicorn app.main:app --reload`
   - Verify frontend chạy được: `npm run dev`
   - Deploy staging: `vercel --prod` (frontend), `railway up` (backend)

4. **Brainstorm features**:
   - 3 tính năng core cho problem
   - MVP scope (chỉ 1 feature hoạt động hoàn chỉnh)
   - Tech decisions: AI provider nào, Vietnamese NLP library nào

5. **Create issue tracker**:
   - Backend: API endpoints cần build
   - Frontend: components cần build
   - Integration: frontend-backend wiring
   - Polish: UI, animations, responsive

6. **Assign first task**:
   - Backend → Setup database schema + first AI endpoint
   - Frontend → Landing page + navigation
   - Designer → Wireframe + design system

7. **Set checkpoint**:
   - 4h: Demo được 1 feature cơ bản
   - 8h: Demo luồng end-to-end
   - 12h: MVP hoàn chỉnh

## Response Format

```
# 🎯 Hackathon Day 1 — [Date]

## Problem: [problem]
## Tech Focus: [tech-focus]

## 🏗️ MVP Scope
1. Feature 1: [mô tả]
2. Feature 2: [mô tả]
3. Feature 3: [mô tả] (nice-to-have)

## 📋 Task分配
- Backend: [tasks]
- Frontend: [tasks]
- Designer: [tasks]

## ⏰ Checkpoints
- [4h]: [milestone]
- [8h]: [milestone]
- [12h]: [milestone]

## 🚀 First Action
[Bước cụ thể cho user bắt đầu ngay]
```
