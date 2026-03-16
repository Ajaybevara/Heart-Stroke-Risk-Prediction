@echo off
REM Production Setup Script for Windows

echo 🔧 Setting up production environment...

REM Check if .env.production exists
if not exist ".env.production" (
    echo 📋 Creating .env.production from template...
    copy .env.production.template .env.production
    echo ✅ Created .env.production
    echo ⚠️  Please edit .env.production with your actual production values
) else (
    echo ✅ .env.production already exists
)

REM Create necessary directories
echo 📁 Creating production directories...
if not exist "uploads" mkdir uploads
if not exist "logs" mkdir logs
if not exist "backups" mkdir backups

echo.
echo 🎯 Production setup complete!
echo.
echo 📋 Next steps:
echo 1. Edit .env.production with your production values
echo 2. Set up Google Cloud Project
echo 3. Configure Firebase service account
echo 4. Run: deploy-gcp.bat
echo.
echo 📚 See PRODUCTION_DEPLOYMENT.md for detailed instructions
pause