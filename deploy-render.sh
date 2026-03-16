#!/bin/bash
# Render Deployment Helper Script

echo "🚀 Render Deployment Helper"
echo ""
echo "Since Render deployments are done through the web dashboard,"
echo "this script provides guidance for manual deployment."
echo ""

echo "📋 Render Deployment Steps:"
echo "1. Push your code to GitHub"
echo "2. Go to https://render.com"
echo "3. Click 'New' → 'Web Service'"
echo "4. Connect your GitHub repository"
echo "5. Configure the following settings:"
echo ""
echo "   Build Command: pip install -r requirements.txt"
echo "   Start Command: gunicorn --bind 0.0.0.0:\$PORT main:app --workers 2 --threads 4 --worker-class gthread"
echo "   Python Version: 3.9"
echo ""
echo "6. Add environment variables in the dashboard"
echo "7. Click 'Create Web Service'"
echo ""

echo "✅ Your app will be automatically deployed!"
echo "🌐 Check your Render dashboard for the live URL"