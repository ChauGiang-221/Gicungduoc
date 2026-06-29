#!/bin/bash
# setup.sh — Setup hackathon project in 5 minutes

echo "🚀 VN AI Innovation Hackathon - Quick Setup"
echo "=========================================="

# Check Node.js
if ! command -v node &> /dev/null; then
    echo "❌ Node.js not found. Install from https://nodejs.org"
    exit 1
fi

# Check Python
if ! command -v python &> /dev/null; then
    echo "❌ Python not found. Install from https://python.org"
    exit 1
fi

echo "✅ Node.js: $(node --version)"
echo "✅ Python: $(python --version)"

# Setup Backend
echo ""
echo "📦 Setting up Backend..."
cd backend
python -m venv venv

if [[ "$OSTYPE" == "msys" || "$OSTYPE" == "win32" ]]; then
    source venv/Scripts/activate
    VENV_ACT="venv\Scripts\activate"
else
    source venv/bin/activate
    VENV_ACT="source venv/bin/activate"
fi

pip install -r requirements.txt

if [ ! -f .env ]; then
    cp .env.example .env
    echo "⚠️  Created .env - please add your API keys!"
fi

echo "✅ Backend ready"
echo "   Run: cd backend && $VENV_ACT && uvicorn app.main:app --reload"

# Setup Frontend
echo ""
echo "📦 Setting up Frontend..."
cd ../frontend
npm install

if [ ! -f .env.local ]; then
    cp .env.example .env.local
    echo "⚠️  Created .env.local - please configure NEXT_PUBLIC_API_URL"
fi

echo "✅ Frontend ready"
echo "   Run: cd frontend && npm run dev"

echo ""
echo "=========================================="
echo "✅ Setup complete!"
echo ""
echo "Next steps:"
echo "1. Add API keys to backend/.env"
echo "2. Configure frontend/.env.local"
echo "3. Run: cd backend && $VENV_ACT && uvicorn app.main:app --reload"
echo "4. Run: cd frontend && npm run dev"
echo ""
echo "📚 Docs: https://github.com/ChauGiang-221/Gicungduoc"
