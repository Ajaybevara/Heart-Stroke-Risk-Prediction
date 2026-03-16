# Render Deployment Guide - Heart Stroke Risk Prediction

## Overview
This guide covers deploying your Flask application to Render with Firebase integration.

## Why Render?

- **Developer-friendly** - Simple Git-based deployment
- **Free tier available** - 750 hours/month free
- **Automatic SSL** - HTTPS included
- **Auto-scaling** - Handles traffic spikes
- **Built-in monitoring** - Health checks and logs
- **Database options** - PostgreSQL and Redis available

## Prerequisites

### 1. Render Account
- Sign up at [render.com](https://render.com)
- Connect your GitHub account

### 2. GitHub Repository
- Push your code to a GitHub repository
- Make sure all files are committed

### 3. Firebase Configuration
- Your Firebase project is already configured
- Keep your Firebase credentials ready

## Quick Deployment Steps

### Step 1: Setup
```bash
# On Windows
setup-render.bat

# On Linux/Mac
./setup-render.sh
```

### Step 2: Configure Environment
Edit `.env.render` with your production values:
- Firebase API keys
- Email credentials
- Secure secret key

### Step 3: Push to GitHub
```bash
git add .
git commit -m "Deploy to Render"
git push origin main
```

### Step 4: Create Render Service

1. **Go to Render Dashboard**
   - Visit [dashboard.render.com](https://dashboard.render.com)

2. **Create New Web Service**
   - Click "New" → "Web Service"
   - Connect your GitHub repository

3. **Configure Build Settings**
   ```
   Name: stroke-prediction
   Environment: Python 3
   Build Command: pip install -r requirements.txt
   Start Command: gunicorn --bind 0.0.0.0:$PORT main:app --workers 2 --threads 4 --worker-class gthread
   ```

4. **Set Environment Variables**
   In the Environment section, add:
   ```
   FLASK_ENV=production
   SECRET_KEY=your-very-secure-random-key
   NEXT_PUBLIC_FIREBASE_API_KEY=your-api-key
   NEXT_PUBLIC_FIREBASE_AUTH_DOMAIN=your-domain.firebaseapp.com
   NEXT_PUBLIC_FIREBASE_PROJECT_ID=your-project-id
   NEXT_PUBLIC_FIREBASE_STORAGE_BUCKET=your-project.appspot.com
   NEXT_PUBLIC_FIREBASE_MESSAGING_SENDER_ID=your-sender-id
   NEXT_PUBLIC_FIREBASE_APP_ID=your-app-id
   EMAIL_SENDER=your-email@gmail.com
   EMAIL_PASSWORD=your-gmail-app-password
   SMTP_SERVER=smtp.gmail.com
   SMTP_PORT=587
   ```

5. **Deploy**
   - Click "Create Web Service"
   - Render will build and deploy automatically

## Advanced Configuration

### Health Checks
- Render automatically monitors `/health` endpoint
- Configure custom health check path if needed

### Auto-Deploy
- Enable auto-deploy from GitHub pushes
- Set branch to deploy from (usually `main`)

### Custom Domain
1. Go to service settings
2. Add custom domain
3. Configure DNS records as instructed

### Database (Optional)
Add a PostgreSQL database:
1. Create new PostgreSQL service in Render
2. Copy connection string to environment variables
3. Update app to use PostgreSQL instead of JSON files

### Environment Variables Reference

| Variable | Description | Required |
|----------|-------------|----------|
| `FLASK_ENV` | Set to `production` | ✅ |
| `SECRET_KEY` | Random secure key | ✅ |
| `NEXT_PUBLIC_FIREBASE_*` | Firebase configuration | ✅ |
| `EMAIL_SENDER` | Gmail address | ✅ |
| `EMAIL_PASSWORD` | Gmail app password | ✅ |
| `PORT` | Auto-provided by Render | ❌ |
| `DATABASE_URL` | PostgreSQL connection | ❌ |

## Monitoring & Troubleshooting

### Logs
- View real-time logs in Render dashboard
- Filter by build logs vs. runtime logs

### Health Monitoring
- Automatic health checks every 30 seconds
- Service status visible in dashboard

### Common Issues

1. **Build Fails**
   - Check Python version (3.9 recommended)
   - Verify requirements.txt is complete
   - Check for missing dependencies

2. **App Won't Start**
   - Verify environment variables are set
   - Check Firebase configuration
   - Ensure PORT variable is used correctly

3. **Firebase Auth Issues**
   - Verify API keys match Firebase project
   - Check Firebase security rules
   - Ensure domain is whitelisted

4. **Email Not Working**
   - Use Gmail app password (not regular password)
   - Enable "Less secure app access" or use app password
   - Check SMTP settings

### Performance Optimization

- **Workers:** Adjust gunicorn workers based on load
- **Caching:** Consider adding Redis for session storage
- **Database:** Migrate from JSON files to PostgreSQL for better performance
- **Static Files:** Use Render's CDN for static assets

## Cost Estimation

- **Free Tier:** 750 hours/month (~$0)
- **Paid Tier:** Starts at $7/month for additional resources
- **Database:** PostgreSQL starts at $7/month
- **Custom Domain:** Free with paid plan

## Security Best Practices

- ✅ Use strong SECRET_KEY
- ✅ Enable HTTPS (automatic)
- ✅ Keep dependencies updated
- ✅ Use environment variables for secrets
- ✅ Regular security audits
- ✅ Monitor for vulnerabilities

## Backup & Recovery

- **Code:** GitHub provides version control
- **Database:** Use Render's PostgreSQL backups
- **Files:** Consider cloud storage for uploads
- **Configuration:** Document all environment variables

## Support

- **Render Docs:** https://docs.render.com/
- **Community:** Render Discord or forums
- **Firebase Docs:** https://firebase.google.com/docs

---

**Estimated Setup Time:** 15-30 minutes
**Free Tier Limits:** 750 hours/month, suitable for development/testing
**Production Ready:** Yes, with monitoring and auto-scaling