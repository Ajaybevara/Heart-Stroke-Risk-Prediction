#!/bin/bash
# Environment Setup Script for Production

echo "🔧 Setting up production environment..."

# Check if .env.production exists
if [ ! -f ".env.production" ]; then
    echo "📋 Creating .env.production from template..."
    cp .env.production.template .env.production
    echo "✅ Created .env.production"
    echo "⚠️  Please edit .env.production with your actual production values"
else
    echo "✅ .env.production already exists"
fi

# Create necessary directories
echo "📁 Creating production directories..."
mkdir -p uploads/
mkdir -p logs/
mkdir -p backups/

# Set proper permissions
echo "🔒 Setting secure permissions..."
chmod 600 .env.production
chmod 755 uploads/
chmod 755 logs/

echo ""
echo "🎯 Production setup complete!"
echo ""
echo "📋 Next steps:"
echo "1. Edit .env.production with your production values"
echo "2. Set up Google Cloud Project"
echo "3. Configure Firebase service account"
echo "4. Run: ./deploy-gcp.sh"
echo ""
echo "📚 See PRODUCTION_DEPLOYMENT.md for detailed instructions"