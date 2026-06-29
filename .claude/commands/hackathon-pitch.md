# /hackathon-pitch — Prepare Pitch & Demo

## Command
```
/hackathon-pitch [action]
```

## Description
Hỗ trợ chuẩn bị pitch và demo cho hackathon.

## Actions

### review
Review pitch deck hiện tại.
```
/hackathon-pitch review
```
Check: slides, timing, content, flow

### script
Generate speaker script cho 1 slide.
```
/hackathon-pitch script [slide-number]
```
Output: Exact words + timing + body language

### demo
Create demo script cho 1 feature.
```
/hackathon-pitch demo [feature]
```
Output: Steps + timestamps + talking points + backup plan

### qa
Generate Q&A preparation.
```
/hackathon-pitch qa
```
Output: 10 common questions + answers + key points

### practice
Practice pitch với timer.
```
/hackathon-pitch practice
```
Output: 5-minute timer + reminders

## Instructions

Khi user gọi `/hackathon-pitch`:

1. **Read pitch materials**:
   - docs/pitch-deck.md — slide structure
   - docs/demo-script.md — demo scripts
   - docs/RESOURCES.md — winning tips

2. **Understand context**:
   - Product name
   - Problem being solved
   - Key features
   - Tech stack

3. **Generate content**:
   - Concise, punchy language
   - Vietnamese context
   - Data-driven claims

4. **Time management**:
   - Exactly 5 minutes
   - Per-slide timing
   - Buffer for Q&A

## Response Format (script)
```
# Slide [N]: [Title]

## ⏱️ Timing
[Start time] - [End time] ([Duration]s)

## 🎤 Script
"[Exact words to say]"

## 🤝 Body Language
[Key gestures, eye contact, positioning]

## ➡️ Transition
"[Next slide transition words]"

## 🚨 Reminders
- [Key point to emphasize]
- [Common mistake to avoid]
```
