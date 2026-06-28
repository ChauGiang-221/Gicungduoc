# Hackathon Branches

## Branch Strategy

### Main Branches
- `main`: Production-ready code.
- `dev`: Integration branch for testing.
- `staging`: Pre-deployment testing.

### Feature Branches
- `feature/frontend/ui-components`: UI components development.
- `feature/frontend/ai-chat`: Chat interface implementation.
- `feature/backend/ai-service`: AI provider integration.
- `feature/backend/database`: Firestore setup.
- `feature/api/streaming`: Streaming response support.

### Bug Fix Branches
- `fix/frontend/...`: Frontend bug fixes.
- `fix/backend/...`: Backend bug fixes.

### Release Branches
- `release/v1.0.0`: Pre-release testing.

## Workflow

1. Create feature branch from `dev`.
2. Develop and commit regularly.
3. Push to remote frequently.
4. Create PR to `dev` when ready.
5. Review and merge after approval.
6. Merge `dev` to `main` for deployment.

## Protection Rules

### Main
- Require PR.
- Require 2 approvals.
- Require CI pass.
- No direct pushes.

### Dev
- Require PR.
- Require 1 approval.
- Require CI pass.

## Merge Strategy

- Use squash merge for feature branches.
- Use merge commit for release branches.
- Keep history clean and readable.
