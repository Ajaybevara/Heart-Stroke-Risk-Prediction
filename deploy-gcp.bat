@echo off
REM Production Deployment Script for Google Cloud Platform (Windows)

echo 🚀 Starting production deployment to Google Cloud Platform...

REM Check if gcloud is installed
gcloud version >nul 2>&1
if %errorlevel% neq 0 (
    echo ❌ gcloud CLI not found. Please install Google Cloud SDK first.
    echo    Visit: https://cloud.google.com/sdk/docs/install
    pause
    exit /b 1
)

REM Check if user is logged in
gcloud auth list --filter=status:ACTIVE --format="value(account)" 2>nul | findstr . >nul
if %errorlevel% neq 0 (
    echo ❌ Not logged in to Google Cloud. Please run: gcloud auth login
    pause
    exit /b 1
)

REM Set project (you'll need to change this to your project ID)
set PROJECT_ID=your-gcp-project-id
echo 📋 Using project: %PROJECT_ID%
gcloud config set project %PROJECT_ID%

REM Enable required APIs
echo 🔧 Enabling required APIs...
gcloud services enable appengine.googleapis.com
gcloud services enable firestore.googleapis.com
gcloud services enable cloudbuild.googleapis.com

REM Deploy to App Engine
echo 📦 Deploying to Google App Engine...
gcloud app deploy --version=prod --quiet

REM Get the deployed URL
for /f "tokens=*" %%i in ('gcloud app describe --format="value(defaultHostname)"') do set DEPLOYED_URL=%%i
echo ✅ Deployment complete!
echo 🌐 Your app is live at: https://%DEPLOYED_URL%

echo.
echo 📋 Next steps:
echo 1. Set up production environment variables in GCP Console
echo 2. Configure Firebase service account key
echo 3. Set up production database (PostgreSQL)
echo 4. Configure monitoring and logging
echo 5. Set up SSL certificate (App Engine provides this automatically)
pause