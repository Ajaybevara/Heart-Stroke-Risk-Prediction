#!/bin/bash
# Production Deployment Script for Google Cloud Platform

echo "🚀 Starting production deployment to Google Cloud Platform..."

# Check if gcloud is installed
if ! command -v gcloud &> /dev/null; then
    echo "❌ gcloud CLI not found. Please install Google Cloud SDK first."
    echo "   Visit: https://cloud.google.com/sdk/docs/install"
    exit 1
fi

# Check if user is logged in
if ! gcloud auth list --filter=status:ACTIVE --format="value(account)" | head -n 1 > /dev/null; then
    echo "❌ Not logged in to Google Cloud. Please run: gcloud auth login"
    exit 1
fi

# Set project (you'll need to change this to your project ID)
PROJECT_ID="your-gcp-project-id"
echo "📋 Using project: $PROJECT_ID"
gcloud config set project $PROJECT_ID

# Enable required APIs
echo "🔧 Enabling required APIs..."
gcloud services enable appengine.googleapis.com
gcloud services enable firestore.googleapis.com
gcloud services enable cloudbuild.googleapis.com

# Deploy to App Engine
echo "📦 Deploying to Google App Engine..."
gcloud app deploy --version=prod --quiet

# Get the deployed URL
DEPLOYED_URL=$(gcloud app describe --format="value(defaultHostname)")
echo "✅ Deployment complete!"
echo "🌐 Your app is live at: https://$DEPLOYED_URL"

echo ""
echo "📋 Next steps:"
echo "1. Set up production environment variables in GCP Console"
echo "2. Configure Firebase service account key"
echo "3. Set up production database (PostgreSQL)"
echo "4. Configure monitoring and logging"
echo "5. Set up SSL certificate (App Engine provides this automatically)"