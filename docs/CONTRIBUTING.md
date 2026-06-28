# Contributing Guidelines

## Workflow

1. Fork repo.
2. Create feature branch từ `main`.
3. Develop và test local.
4. Commit với message rõ ràng.
5. Tạo Pull Request.

## Branch naming

- `feature/ten-tinh-nang`
- `fix/sua-bug`
- `docs/cap-nhat-tai-lieu`
- `refactor/ten-module`

## Commit message format

```
<type>: <subject>

<body>

<footer>
```

Ví dụ:

```
feat: them chat AI streaming

- Implement streaming endpoint
- Them loading state
- Handle error gracefully
```

## Code style

### Python
- Dùng `ruff` hoặc `black` formatter.
- Type hints cho function signatures.
- Docstring cho public functions.

### TypeScript
- ESLint config từ Next.js.
- Strict mode.
- Component name PascalCase.
- File name kebab-case hoặc PascalCase.

## Review process

- Ít nhất 1 approve trước khi merge.
- CI phải pass.
- Không merge nếu có conflict.
