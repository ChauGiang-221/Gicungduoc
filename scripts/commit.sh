#!/bin/bash
# commit.sh — Quick git commit và push

# Get commit message from args or prompt
MSG="${1:-feat: quick update}"

echo "📦 Git Commit & Push"
echo "===================="

# Check git status
STATUS=$(git status --short)
if [ -z "$STATUS" ]; then
    echo "⚠️  No changes to commit"
    exit 0
fi

echo "Changes:"
echo "$STATUS"
echo ""

# Stage all
git add -A

# Commit
git commit -m "$MSG" -m "Co-Authored-By: Claude Opus 4.8 <noreply@anthropic.com>"

# Push
echo ""
echo "🚀 Pushing to origin..."
git push origin main

echo ""
echo "✅ Done! Check https://github.com/ChauGiang-221/Gicungduoc"
