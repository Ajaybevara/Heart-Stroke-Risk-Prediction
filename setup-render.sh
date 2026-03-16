#!/bin/bash
# Render Setup Script

echo "🔧 Setting up for Render deployment..."

# Create render environment file
if [ ! -f ".env.render" ]; then
    echo "📋 Creating .env.render from template..."
    cp .env.render.template .env.render
    echo "✅ Created .env.render"
    echo "⚠️  Please edit .env.render with your actual values"
    echo "   (This is just for reference - actual env vars go in Render dashboard)"
else
    echo "✅ .env.render already exists"
fi

# Create necessary directories
echo "📁 Creating production directories..."
mkdir -p uploads/
mkdir -p logs/

# Check if git repository
if [ ! -d ".git" ]; then
    echo "⚠️  No git repository found. Initialize git:"
    echo "   git init"
    echo "   git add ."
    echo "   git commit -m 'Initial commit'"
fi

echo ""
echo "🎯 Render setup complete!"
echo ""
echo "📋 Next steps:"
echo "1. Edit .env.render with your production values (for reference)"
echo "2. Commit and push your code to GitHub:"
echo "   git add ."
echo "   git commit -m 'Ready for Render deployment'"
echo "   git push origin main"
echo "3. Go to https://render.com and create a new Web Service"
echo "4. Connect your GitHub repository"
echo "5. Use these settings:"
echo "   - Build Command: pip install -r requirements.txt"
echo "   - Start Command: gunicorn --bind 0.0.0.0:\$PORT main:app --workers 2 --threads 4 --worker-class gthread"
echo "6. Add environment variables in Render dashboard (copy from .env.render)"
echo "7. Deploy!"
echo ""
echo "📚 See RENDER_DEPLOYMENT.md for detailed instructions"