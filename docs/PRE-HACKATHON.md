# VN AI Innovation Hackathon - Pre-Hackathon Checklist

> **Hackathon Duration:** 48 hours
> **Tech Stack:** Next.js + FastAPI + AI (OpenAI/Claude/Gemini) + Firebase
> **Team Roles:** Backend, Frontend, UI/UX Designer

---

## Mục lục

1. [7-Day Prep Checklist](#7-day-prep-checklist)
2. [48-Hour Prep Checklist](#48-hour-prep-checklist)
3. [24-Hour Prep Checklist](#24-hour-prep-checklist)
4. [Morning Of Checklist](#morning-of-checklist)
5. [During Hackathon Checklist](#during-hackathon-checklist)
6. [Pitch Prep Checklist](#pitch-prep-checklist)
7. [Post-Hackathon Checklist](#post-hackathon-checklist)
8. [Emergency Contacts](#emergency-contacts)
9. [Technical Backup Plan](#technical-backup-plan)
10. [Common Failure Scenarios](#common-failure-scenarios)
11. [What to Bring](#what-to-bring)
12. [Mental Preparation](#mental-preparation)

---

## 7-DAY PREP CHECKLIST

### Tuần trước Hackathon (7 ngày trước)

#### Infrastructure & Repository Setup

- [ ] **HIGH** | 2h | Backend | Thiết lập Git repository chính thức với cấu trúc monorepo (frontend, backend, shared)
- [ ] **HIGH** | 1h | Backend | Cấu hình CI/CD pipeline cơ bản (GitHub Actions)
- [ ] **HIGH** | 30m | Backend | Tạo Docker Compose file cho local development
- [ ] **MEDIUM** | 1h | All | Clone repository về máy tất cả thành viên, verify môi trường chạy được
- [ ] **HIGH** | 2h | Backend | Triển khai FastAPI boilerplate với cấu trúc project chuẩn
- [ ] **HIGH** | 1h | Frontend | Triển khai Next.js boilerplate với TypeScript và Tailwind
- [ ] **HIGH** | 30m | All | Tạo API contract document (OpenAPI/Swagger) - dùng chung

#### Authentication & Database Setup

- [ ] **HIGH** | 2h | Backend | Cấu hình Firebase Authentication (email, Google OAuth)
- [ ] **HIGH** | 2h | Backend | Thiết lập Firebase Firestore schema và security rules
- [ ] **HIGH** | 1h | Backend | Tạo seed data và migration scripts
- [ ] **MEDIUM** | 1h | All | Verify tất cả team member có thể access Firebase console

#### AI Integration Setup

- [ ] **HIGH** | 2h | Backend | Tạo AI service abstraction layer (hỗ trợ OpenAI/Claude/Gemini)
- [ ] **HIGH** | 1h | Backend | Setup API keys cho tất cả AI providers (development environment)
- [ ] **MEDIUM** | 1h | Backend | Tạo rate limiting và fallback logic cho AI calls
- [ ] **HIGH** | 1h | Backend | Implement basic retry mechanism với exponential backoff
- [ ] **MEDIUM** | 30m | Backend | Tạo mock responses cho AI calls (dùng khi API limit)

#### UI/UX Preparation

- [ ] **HIGH** | 3h | Designer | Hoàn thành wireframes cho 3-5 screens chính
- [ ] **HIGH** | 2h | Designer | Tạo component library trong Figma với states (hover, active, disabled, loading)
- [ ] **MEDIUM** | 1h | Designer | Prepare design system (colors, typography, spacing tokens)
- [ ] **HIGH** | 2h | Designer | Tạo responsive breakpoints specification (mobile, tablet, desktop)
- [ ] **MEDIUM** | 1h | Designer | Prepare icon library và asset exports

#### Communication & Project Management

- [ ] **HIGH** | 30m | All | Tạo Slack/Discord channel cho hackathon communication
- [ ] **HIGH** | 30m | All | Thiết lập shared Notion/Notion alternative cho documentation
- [ ] **MEDIUM** | 1h | All | Cấu hình video call setup (Zoom/Google Meet) cho remote coordination
- [ ] **HIGH** | 30m | All | Tạo shared calendar với key milestones và deadlines

#### Knowledge Preparation

- [ ] **MEDIUM** | 2h | Backend | Review và practice FastAPI best practices (dependency injection, async patterns)
- [ ] **MEDIUM** | 2h | Frontend | Review Next.js 14 App Router patterns và Server Components
- [ ] **MEDIUM** | 2h | Backend | Study AI API documentation (rate limits, pricing, best practices)
- [ ] **LOW** | 1h | All | Review hackathon rules và judging criteria (nếu có public)

---

## 48-HOUR PREP CHECKLIST

### 2 ngày trước Hackathon

#### Final Technical Verification

- [ ] **HIGH** | 30m | Backend | Chạy full stack locally, verify tất cả endpoints hoạt động
- [ ] **HIGH** | 30m | Frontend | Verify build process: `npm run build` không có errors
- [ ] **HIGH** | 30m | Backend | Test Firebase connections (Auth, Firestore, Storage)
- [ ] **HIGH** | 30m | All | Verify VPN/Network access tại venue (nếu biết trước location)
- [ ] **MEDIUM** | 30m | Backend | Test AI API calls với production-like payload

#### Dependency & Package Management

- [ ] **HIGH** | 30m | All | Run `npm audit` / `pip audit`, resolve critical vulnerabilities
- [ ] **HIGH** | 30m | All | Freeze dependencies versions (package-lock.json, requirements.lock)
- [ ] **MEDIUM** | 30m | Frontend | Download and cache CDN dependencies locally (nếu có)
- [ ] **HIGH** | 30m | All | Backup tất cả node_modules và venv (offline contingency)

#### Project Structure Finalization

- [ ] **HIGH** | 1h | All | Review và lock API contracts giữa frontend và backend
- [ ] **HIGH** | 30m | All | Tạo README với setup instructions (ai cũng có thể run được)
- [ ] **MEDIUM** | 30m | Designer | Export final design assets (SVG, PNG, Figma link)
- [ ] **MEDIUM** | 30m | All | Setup error tracking (Sentry hoặc similar - free tier)

#### Team Preparation

- [ ] **HIGH** | 1h | All | Họp team: phân công responsibilities cho hackathon
- [ ] **HIGH** | 1h | All | Xác định MVP scope và agree trên feature prioritization
- [ ] **MEDIUM** | 30m | All | Thống nhất git workflow (branch naming, commit conventions, PR process)
- [ ] **MEDIUM** | 30m | All | Discuss và align về coding style guide

#### Physical Preparation

- [ ] **MEDIUM** | 30m | All | Check venue logistics (parking, food, accommodation nếu cần)
- [ ] **MEDIUM** | 30m | All | Reserve accommodation gần venue (nếu overnight)
- [ ] **LOW** | 30m | All | Mua snacks và beverages cho 2 ngày

---

## 24-HOUR PREP CHECKLIST

### Ngày cuối trước Hackathon

#### Final Code Freeze & Backup

- [ ] **HIGH** | 30m | All | Commit và push tất cả code hiện tại lên main/master
- [ ] **HIGH** | 30m | All | Tạo backup branch: `backup-pre-hackathon-v1`
- [ ] **HIGH** | 30m | All | Verify repository có thể clone và run ở máy khác
- [ ] **HIGH** | 30m | All | Export và backup Firebase data (schemas, rules config)

#### Environment Setup Verification

- [ ] **HIGH** | 1h | All | Mỗi thành viên verify có thể setup dev environment từ scratch trong 30 phút
- [ ] **HIGH** | 30m | All | Test pair programming setup (VS Code Live Share hoặc similar)
- [ ] **MEDIUM** | 30m | All | Verify tất cả team member có quyền access Firebase project
- [ ] **HIGH** | 30m | All | Test deployment script (nếu có) - deploy lên staging

#### Hardware & Equipment Check

- [ ] **HIGH** | 30m | All | Kiểm tra laptop battery health và charging cables
- [ ] **HIGH** | 1h | All | Backup laptop - full system image hoặc Time Machine
- [ ] **MEDIUM** | 30m | All | Chuẩn bị power banks và extension cords
- [ ] **MEDIUM** | 30m | All | Test external monitors, keyboards, mice (nếu có)
- [ ] **MEDIUM** | 30m | All | Verify headphones/microphone cho video calls

#### Documentation & Communication

- [ ] **MEDIUM** | 30m | All | Tạo shared document với team roster và contact info
- [ ] **MEDIUM** | 30m | All | Tạo escalation matrix (who to contact when stuck)
- [ ] **MEDIUM** | 30m | All | Setup emergency contact sharing (Google Contacts hoặc similar)

#### Personal Preparation

- [ ] **MEDIUM** | 1h | All | Pack clothes cho 2 ngày (layer vì điều hòa)
- [ ] **MEDIUM** | 30m | All | Chuẩn bị toiletries và personal medications
- [ ] **MEDIUM** | 1h | All | Ngủ đủ giấc - target 8 tiếng đêm nay

---

## MORNING OF CHECKLIST

### Sáng ngày Hackathon bắt đầu

#### Pre-Departure Checklist

- [ ] **HIGH** | 10m | All | Charge laptop > 80%
- [ ] **HIGH** | 5m | All | Bring ALL chargers (laptop, phone, power bank)
- [ ] **HIGH** | 5m | All | Verify ID và event registration confirmation
- [ ] **HIGH** | 5m | All | Bring venue address và directions (printed backup)
- [ ] **MEDIUM** | 5m | All | Bring business cards (networking opportunity)
- [ ] **MEDIUM** | 5m | All | Check weather và bring umbrella/jacket if needed

#### Dev Environment Quick Start (Tại chỗ)

- [ ] **HIGH** | 10m | All | Clone repository (fresh clone vào laptop)
- [ ] **HIGH** | 5m | All | Copy .env.example → .env, fill in API keys
- [ ] **HIGH** | 15m | All | Run `npm install` && `pip install -r requirements.txt`
- [ ] **HIGH** | 5m | All | Run `docker-compose up` (nếu dùng containers)
- [ ] **HIGH** | 10m | All | Verify: `npm run dev` và backend server start successfully
- [ ] **HIGH** | 10m | All | Quick smoke test - navigate to localhost, verify page loads

#### Team Standup

- [ ] **HIGH** | 15m | All | Quick team sync: agree on daily standup times
- [ ] **HIGH** | 10m | All | Confirm分工 (Backend/Frontend/Designer coordination points)
- [ ] **MEDIUM** | 5m | All | Setup shared screen sharing cho code review sessions
- [ ] **HIGH** | 5m | All | Create hackathon-specific Slack/Discord channel

#### Workspace Setup (Tại venue)

- [ ] **HIGH** | 10m | All | Find good seating arrangement (near power outlets)
- [ ] **MEDIUM** | 10m | All | Setup dual monitor if available
- [ ] **MEDIUM** | 5m | All | Connect to venue WiFi, save password
- [ ] **HIGH** | 5m | All | Test network speed (download/upload) - critical for AI APIs
- [ ] **MEDIUM** | 5m | All | Setup phone in Do Not Disturb mode

---

## DURING HACKATHON CHECKLIST

### Trong suốt Hackathon (48 tiếng)

#### Time Management Framework

| Phase | Time | Goal |
|-------|------|------|
| Hours 0-4 | Ideation & Architecture | Finalize idea, setup architecture |
| Hours 4-20 | Core Features | MVP functionality |
| Hours 20-32 | Polish & Integration | UI/UX polish, AI integration |
| Hours 32-46 | Testing & Refinement | Bug fixes, performance optimization |
| Hours 46-48 | Pitch Prep & Final | Demo recording, presentation |

#### Daily Standups (mỗi 8 tiếng)

- [ ] **HIGH** | 15m | All | Morning standup (8:00): Yesterday accomplishments, today's goals, blockers
- [ ] **HIGH** | 15m | All | Midday standup (16:00): Progress check, reprioritization
- [ ] **HIGH** | 15m | All | Evening standup (00:00): Day summary, overnight tasks

#### Decision Making Rules

- [ ] **HIGH** | - | All | "Perfect is the enemy of done" - ship MVP first, optimize later
- [ ] **HIGH** | - | All | Major decisions require team consensus within 15 minutes
- [ ] **MEDIUM** | - | All | If stuck > 30 minutes, escalate to team immediately
- [ ] **HIGH** | - | All | Document all decisions in shared doc (context + rationale)

#### Code Quality Gates

- [ ] **HIGH** | 5m | All | Commit mỗi feature/component xong (DO NOT accumulate)
- [ ] **HIGH** | 10m | All | Pull before push - always rebase on latest
- [ ] **MEDIUM** | - | All | Write meaningful commit messages: `feat:`, `fix:`, `refactor:`
- [ ] **MEDIUM** | 10m | All | Pair review trước merge critical features

#### Communication Protocols

- [ ] **HIGH** | - | All | Slack/Discord: Use threads, @mention only when urgent
- [ ] **HIGH** | - | All | Blocking issue → immediate team ping, don't wait for standup
- [ ] **MEDIUM** | - | All | Daily summary post trong channel: accomplishments + tomorrow's plan
- [ ] **LOW** | - | All | Minimize meetings - maximize coding time

#### Health & Energy Management

- [ ] **HIGH** | 30m | All | Take 15-minute breaks every 2 hours (walk around)
- [ ] **HIGH** | 30m | All | Stay hydrated - drink water consistently
- [ ] **MEDIUM** | 30m | All | Eat regular meals (don't skip breakfast, lunch)
- [ ] **HIGH** | 2h | All | Sleep minimum 4-5 hours/night (cognitive function degrades without)
- [ ] **MEDIUM** | 15m | All | Eye breaks - look away from screen every 20 minutes
- [ ] **LOW** | 10m | All | Stretch breaks - prevent strain injuries

#### Regular Git Hygiene

- [ ] **HIGH** | 10m | All | `git checkout -b feature/your-name-feature` for each feature
- [ ] **HIGH** | 5m | All | Pull request khi feature done (even partial)
- [ ] **HIGH** | 5m | All | Keep main branch deployable at all times
- [ ] **MEDIUM** | - | All | Tag releases: `v0.1.0`, `v0.2.0`, `v1.0.0` (final)

---

## PITCH PREP CHECKLIST

### 2 tiếng cuối trước Presentation

#### Final Demo Preparation (T-120:00 đến T-60:00)

- [ ] **HIGH** | 10m | All | Record demo video (backup nếu live demo fails)
- [ ] **HIGH** | 15m | All | Test demo flow end-to-end 3 lần (cold start → happy path)
- [ ] **HIGH** | 10m | All | Prepare fallback demo (simplified version nếu main fails)
- [ ] **MEDIUM** | 5m | All | Screenshot key features cho slide backup

#### Slide Preparation (T-60:00 đến T-30:00)

- [ ] **HIGH** | 20m | Designer | Create 8-10 slide deck: Title, Problem, Solution, Demo, Tech Stack, Team, Future
- [ ] **HIGH** | 10m | All | Practice pitch timing (5-7 minutes)
- [ ] **MEDIUM** | 5m | All | Prepare speaker notes (bullet points, not full script)
- [ ] **HIGH** | 10m | All | Assign speaking parts: Who presents what section

#### Technical Backup (T-30:00 đến T-15:00)

- [ ] **HIGH** | 5m | All | Push final code lên GitHub
- [ ] **HIGH** | 5m | All | Verify demo environment is stable (deploy lần cuối)
- [ ] **HIGH** | 5m | All | Prepare local copy của demo (offline fallback)
- [ ] **HIGH** | 5m | All | Export API keys locally (nếu cần demo từ laptop)

#### Rehearsal (T-15:00 đến T-0)

- [ ] **HIGH** | 10m | All | Full rehearse với timer
- [ ] **MEDIUM** | 5m | All | Q&A preparation - anticipate 3-5 questions
- [ ] **MEDIUM** | 5m | All | Assign roles: main speaker, demo operator, Q&A backup

#### Final Check (T-5:00)

- [ ] **HIGH** | 2m | All | Phone on silent
- [ ] **HIGH** | 2m | All | Laptop screen brightness maxed
- [ ] **HIGH** | 1m | All | Demo environment ready (new tab/private window)

---

## POST-HACKATHON CHECKLIST

### Sau khi kết thúc Hackathon

#### Immediate Follow-up (Trong 24 giờ)

- [ ] **MEDIUM** | 30m | All | Clean up workspace, return borrowed equipment
- [ ] **MEDIUM** | 30m | All | Backup all files từ venue (photos, notes, recordings)
- [ ] **HIGH** | 1h | All | Rest and recover - sleep, eat properly, hydrate
- [ ] **MEDIUM** | 30m | All | Submit any required post-hackathon forms (nếu có)

#### Team Debrief (48 giờ sau)

- [ ] **HIGH** | 1h | All | Team retrospective: What went well, what to improve
- [ ] **HIGH** | 30m | All | Document lessons learned cho future hackathons
- [ ] **MEDIUM** | 30m | All | Share photos và memories (Discord channel)
- [ ] **MEDIUM** | 1h | All | Clean up codebase: remove debug logs, temporary files

#### Networking & Outreach (1 tuần sau)

- [ ] **MEDIUM** | 30m | All | Connect on LinkedIn với judges, organizers, other teams
- [ ] **MEDIUM** | 30m | All | Thank you emails/messages tới organizers và mentors
- [ ] **LOW** | 30m | All | Share project on social media (với permission từ organizers)
- [ ] **MEDIUM** | 1h | All | Update LinkedIn: Add hackathon experience + project link

#### Project Continuation (Optional)

- [ ] **MEDIUM** | 2h | All | Evaluate project viability (market fit, team interest)
- [ ] **LOW** | 1h | All | Create public GitHub repo (sau khi review sensitive data)
- [ ] **LOW** | 2h | All | Write blog post về hackathon experience
- [ ] **MEDIUM** | 1h | All | Submit project to relevant product hunt / showcase platforms

#### Future Hackathon Preparation

- [ ] **LOW** | 1h | All | Update personal hackathon playbook với improvements
- [ ] **LOW** | 30m | All | Review team feedback forms
- [ ] **LOW** | 30m | All | Update equipment checklist cho lần sau

---

## EMERGENCY CONTACTS

### Internal Team Contacts

| Name | Role | Phone | WhatsApp | Email |
|------|------|-------|----------|-------|
| [Team Member 1] | Backend Lead | [Phone] | [WhatsApp] | [Email] |
| [Team Member 2] | Frontend Lead | [Phone] | [WhatsApp] | [Email] |
| [Team Member 3] | Designer | [Phone] | [WhatsApp] | [Email] |
| [Team Member 4] | [Role] | [Phone] | [WhatsApp] | [Email] |

### Hackathon Official Contacts

| Role | Name | Contact | Availability |
|------|------|---------|--------------|
| Main Organizer | [Name] | [Phone] | 24/7 during event |
| Technical Support | [Name] | [Phone] | During event |
| Venue Coordinator | [Name] | [Phone] | During event |
| Emergency Hotline | - | [Phone] | 24/7 |

### External Emergency Services

| Service | Vietnam Number | Notes |
|---------|----------------|-------|
| Police | 113 | Emergency |
| Ambulance | 115 | Medical emergency |
| Fire | 114 | Fire emergency |
| Non-emergency | 1022 | General emergency assistance |

---

## TECHNICAL BACKUP PLAN

### AI API Failures

**Scenario:** OpenAI/Claude/Gemini API is down or rate-limited

**Recovery:**
1. [ ] **HIGH** | Use cached responses (implement response caching)
2. [ ] **HIGH** | Switch to fallback AI provider automatically
3. [ ] **HIGH** | Use mock/demo responses for presentation
4. [ ] **MEDIUM** | Implement retry with exponential backoff
5. [ ] **MEDIUM** | Queue requests for later processing

### Database Failures

**Scenario:** Firebase is unreachable or throttled

**Recovery:**
1. [ ] **HIGH** | Switch to local SQLite/PostgreSQL backup
2. [ ] **HIGH** | Implement offline-first with local storage
3. [ ] **MEDIUM** | Use in-memory data store temporarily
4. [ ] **MEDIUM** | Queue writes for later sync

### Network Failures

**Scenario:** No internet connection

**Recovery:**
1. [ ] **HIGH** | Use local development server (localhost fallback)
2. [ ] **HIGH** | Tether to mobile hotspot
3. [ ] **HIGH** | Work with local mock data
4. [ ] **MEDIUM** | Use offline-capable PWA features

### Code Conflicts

**Scenario:** Git merge conflicts on critical file

**Recovery:**
1. [ ] **HIGH** | Use `git stash` to save local changes
2. [ ] **HIGH** | Pull latest, resolve conflicts systematically
3. [ ] **HIGH** | Test thoroughly after merge
4. [ ] **MEDIUM** | Have backup of working version before merge

### Hardware Failure

**Scenario:** Laptop crashes or stops working

**Recovery:**
1. [ ] **HIGH** | Cloud backup always available (GitHub, Firebase)
2. [ ] **HIGH** | Pair programming on remaining working laptop
3. [ ] **MEDIUM** | Rent/borrow equipment (check with organizers)
4. [ ] **MEDIUM** | Use online IDE (GitHub Codespaces, Replit)

---

## COMMON FAILURE SCENARIOS

### 1. Feature Overload

**Problem:** Trying to build too many features, nothing is complete

**Symptoms:**
- 48 hours passed, nothing is demoable
- Multiple half-finished features
- Demo fails because features don't integrate

**Recovery:**
1. [ ] **HIGH** | STOP immediately, assess current state
2. [ ] **HIGH** | Cut scope to top 2-3 features
3. [ ] **HIGH** | Focus all effort on making those 2-3 features work perfectly
4. [ ] **MEDIUM** | Agree as team: "What's our MVP?"
5. [ ] **HIGH** | Delete/disable all non-essential features

### 2. Integration Breakdown

**Problem:** Frontend and backend can't communicate

**Symptoms:**
- API calls returning 404/500 errors
- Data format mismatches
- CORS errors

**Recovery:**
1. [ ] **HIGH** | Verify API contract document exists and is followed
2. [ ] **HIGH** | Test API endpoints with Postman/curl directly
3. [ ] **HIGH** | Use mock server (MirageJS/MSW) to decouple
4. [ ] **MEDIUM** | Schedule 30-minute integration sync meeting
5. [ ] **HIGH** | Add CORS headers to backend

### 3. AI Prompt Explosion

**Problem:** AI responses are unpredictable, unusable

**Symptoms:**
- Random/irrelevant responses
- Format mismatches
- Hallucinations

**Recovery:**
1. [ ] **HIGH** | Simplify prompt to absolute minimum
2. [ ] **HIGH** | Add strict output format specification
3. [ ] **HIGH** | Implement output validation
4. [ ] **MEDIUM** | Create fallback rule-based response
5. [ ] **MEDIUM** | Use few-shot examples in prompt

### 4. Scope Creep

**Problem:** Continuous addition of features mid-hackathon

**Symptoms:**
- Team constantly pivoting
- Original idea is unrecognizable
- No clear direction

**Recovery:**
1. [ ] **HIGH** | Return to original problem statement
2. [ ] **HIGH** | Write down 3 core features that solve the problem
3. [ ] **HIGH** | Any new idea → backlog, NOT implementation
4. [ ] **MEDIUM** | Set scope freeze: no new features after hour 20

### 5. Team Conflict

**Problem:** Disagreements causing delays

**Symptoms:**
- Team members working in silos
- Inconsistent architecture decisions
- Passive-aggressive communication

**Recovery:**
1. [ ] **HIGH** | 5-minute mediation: each person shares concern
2. [ ] **HIGH** | Lead/manager makes final call (this is hackathon, move fast)
3. [ ] **MEDIUM** | Agree on decision-making principle: "MVP over perfection"
4. [ ] **MEDIUM** | Focus on problem, not person

### 6. Demo Failure

**Problem:** Demo doesn't work on presentation day

**Symptoms:**
- Feature crashes during demo
- Can't login/authenticate
- Data doesn't load

**Recovery:**
1. [ ] **HIGH** | ALWAYS have pre-recorded video backup
2. [ ] **HIGH** | Test demo on presentation machine beforehand
3. [ ] **HIGH** | Simplify demo flow to most reliable path
4. [ ] **MEDIUM** | Have screenshots as ultimate fallback
5. [ ] **HIGH** | Practice demo 5+ times

---

## WHAT TO BRING

### Electronics

| Item | Priority | Quantity | Notes |
|------|----------|----------|-------|
| Laptop + Charger | HIGH | 1 | Fully charged, plugged in |
| Power Bank | HIGH | 1 | 20,000mAh+ recommended |
| Extension Cord | HIGH | 1 | 3-outlet minimum |
| Phone + Charger | HIGH | 1 | For communication, backup |
| Headphones | MEDIUM | 1 | Noise-canceling preferred |
| USB-C Hub/Adapter | MEDIUM | 1 | HDMI, USB-A, SD card |
| Portable Mouse | LOW | 1 | Personal preference |
| Ethernet Cable | MEDIUM | 1 | Backup network option |
| External Monitor | LOW | 1 | If available |

### Documentation

| Item | Priority | Quantity | Notes |
|------|----------|----------|-------|
| ID / Registration Confirmation | HIGH | 1 | Digital + printed backup |
| Team Roster | HIGH | 1 | Contact info + roles |
| API Keys (Offline Copy) | HIGH | 1 | Printed backup of keys |
| Architecture Diagrams | MEDIUM | 1 | For reference |
| Notion/Notion Link Access | HIGH | 1 | Shared docs |

### Comfort Items

| Item | Priority | Quantity | Notes |
|------|----------|----------|-------|
| Reusable Water Bottle | HIGH | 1 | Stay hydrated |
| Snacks | HIGH | Many | High-protein, low-sugar |
| Coffee/Tea | MEDIUM | Personal | Or buy at venue |
| Eye Mask | MEDIUM | 1 | For power naps |
| Blanket/Jacket | MEDIUM | 1 | Venue can be cold |
| Toothbrush + Toothpaste | MEDIUM | 1 | Freshen up |
| Deodorant | MEDIUM | 1 | Long hours |
| Pain Relievers | MEDIUM | 1 | Headache, cramps |

### Clothing

| Item | Priority | Quantity | Notes |
|------|----------|----------|-------|
| Comfortable Clothes | HIGH | 2-3 | Change for day 2 |
| Hoodie/Sweater | HIGH | 1 | Cold AC |
| Comfortable Shoes | HIGH | 1 | Walk around breaks |
| Hat/Cap | LOW | 1 | Sun protection |

### Networking

| Item | Priority | Quantity | Notes |
|------|----------|----------|-------|
| Business Cards | MEDIUM | Many | Custom hackathon cards |
| Resume Copies | MEDIUM | 10 | For recruiters |
| Elevator Pitch | HIGH | 1 | 30-second self-intro |

---

## MENTAL PREPARATION

### Mindset Shifts

#### DO

- [ ] **HIGH** | Embrace imperfection - "done is better than perfect"
- [ ] **HIGH** | Prioritize ruthlessly - not everything will get done
- [ ] **HIGH** | Ask for help early - don't suffer in silence
- [ ] **MEDIUM** | Celebrate small wins - every working feature is progress
- [ ] **MEDIUM** | Take breaks - your brain needs rest to perform
- [ ] **HIGH** | Trust your team - delegate and empower
- [ ] **MEDIUM** | Stay flexible - pivot when something isn't working

#### DON'T

- [ ] **HIGH** | Don't try to build everything - scope ruthlessly
- [ ] **HIGH** | Don't code for 48 hours straight - you'll make bad decisions
- [ ] **HIGH** | Don't wait until the last minute to test demo
- [ ] **MEDIUM** | Don't ignore conflicts - address them quickly
- [ ] **MEDIUM** | Don't compare to other teams - focus on your progress
- [ ] **HIGH** | Don't skip sleep entirely - even 4 hours helps

### Pre-Hackathon Affirmations

Say to yourself (or team):

1. "We will build something amazing in 48 hours."
2. "It's okay to cut features to ship a working demo."
3. "We are a team - we succeed together and fail together."
4. "Our best work comes from clear communication and trust."
5. "Every hackathon is a learning experience - enjoy the journey."

### Stress Management Techniques

| Technique | When to Use | Duration |
|-----------|-------------|----------|
| Deep Breathing (4-7-8) | Anxiety, panic | 1 minute |
| Walk Around | Mental block | 5-10 minutes |
| Power Nap | Exhaustion | 20 minutes max |
| Stretching | Physical tension | 5 minutes |
| Talk to Someone | Feeling overwhelmed | 10 minutes |

### Red Flags - Stop Immediately

If you experience these, take a break NOW:

- [ ] Headaches that won't go away
- [ ] Can't focus on simple tasks
- [ ] Making same mistake repeatedly
- [ ] Feeling angry/frustrated at teammates
- [ ] Can't remember what you coded 5 minutes ago
- [ ] Heart palpitations or dizziness

---

## Quick Reference Card

```
╔══════════════════════════════════════════════════════════════════╗
║                    VN AI INNOVATION HACKATHON                     ║
╠══════════════════════════════════════════════════════════════════╣
║  TEAM: _______________________  PROJECT: _______________________  ║
╠══════════════════════════════════════════════════════════════════╣
║  KEY TIMES                                                        ║
║  ├─ Hackathon Start: _____________                               ║
║  ├─ Morning Standup: 08:00                                        ║
║  ├─ Midday Standup: 16:00                                         ║
║  ├─ Evening Standup: 00:00                                        ║
║  └─ Pitch Submission: T-2 hours                                   ║
╠══════════════════════════════════════════════════════════════════╣
║  MVP FEATURES (max 3)                                             ║
║  1. _________________________________________________________     ║
║  2. _________________________________________________________     ║
║  3. _________________________________________________________     ║
╠══════════════════════════════════════════════════════════════════╣
║  EMERGENCY CONTACTS                                               ║
║  ├─ Team Lead: _____________ - _____________                      ║
║  ├─ Organizer: _____________ - _____________                      ║
║  └─ Tech Support: _____________ - _____________                   ║
╠══════════════════════════════════════════════════════════════════╣
║  REMEMBER: "Perfect is the enemy of done" - Ship it!              ║
╚══════════════════════════════════════════════════════════════════╝
```

---

**Document Version:** 2.0
**Last Updated:** June 2026
**Team:** [Your Team Name]
**Project:** [Your Project Name]