#!/bin/bash
# deploy.sh — Deploy frontend + backend

echo "🚀 Deploy to Production"
echo "======================"

# Deploy Frontend (Vercel)
echo ""
echo "📦 Deploying Frontend (Vercel)..."
cd frontend
vercel --prod

# Deploy Backend (Railway)
echo ""
echo "📦 Deploying Backend (Railway)..."
cd ../backend
railway up

echo ""
echo "✅ Deploy complete!"
echo ""
echo "📝 Update environment variables on both platforms:"
echo "   Frontend: NEXT_PUBLIC_API_URL=https://[backend-url].railway.app"
echo "   Backend:  OPENAI_API_KEY, ANTHROPIC_API_KEY, GOOGLE_API_KEY"
