# Production Deployment Guide - Heart Stroke Risk Prediction

## Overview
This guide covers deploying your Flask application to production on Google Cloud Platform (GCP) with Firebase integration.

## Prerequisites

### 1. Google Cloud Account & Setup
- Create a GCP account at https://cloud.google.com
- Install Google Cloud SDK: https://cloud.google.com/sdk/docs/install
- Authenticate: `gcloud auth login`
- Set project: `gcloud config set project YOUR_PROJECT_ID`

### 2. Firebase Configuration
- Your Firebase project is already configured
- For production, create a service account key:
  1. Go to Firebase Console > Project Settings > Service Accounts
  2. Generate new private key
  3. Download JSON file (keep secure!)

### 3. Domain & SSL
- App Engine provides automatic SSL certificates
- Custom domain can be configured in GCP Console

## Production Configuration

### Environment Variables
Set these in GCP Console > App Engine > Settings > Environment Variables:

```
SECRET_KEY=your-very-secure-random-key-here
FLASK_ENV=production
NEXT_PUBLIC_FIREBASE_API_KEY=your-firebase-api-key
NEXT_PUBLIC_FIREBASE_AUTH_DOMAIN=your-project.firebaseapp.com
NEXT_PUBLIC_FIREBASE_PROJECT_ID=your-project-id
NEXT_PUBLIC_FIREBASE_STORAGE_BUCKET=your-project.appspot.com
NEXT_PUBLIC_FIREBASE_MESSAGING_SENDER_ID=your-sender-id
NEXT_PUBLIC_FIREBASE_APP_ID=your-app-id
EMAIL_SENDER=your-production-email@gmail.com
EMAIL_PASSWORD=your-app-password
SMTP_SERVER=smtp.gmail.com
SMTP_PORT=587
```

### Database Migration (Recommended)
Your app currently uses JSON files. For production, migrate to:

1. **Cloud Firestore** (recommended for Firebase integration)
2. **Cloud SQL (PostgreSQL)** for relational data
3. **Cloud Storage** for file uploads

## Deployment Steps

### Method 1: App Engine (Recommended)

1. **Update app.yaml** with your project settings
2. **Run deployment script:**
   ```bash
   chmod +x deploy-gcp.sh
   ./deploy-gcp.sh
   ```

3. **Set environment variables** in GCP Console

### Method 2: Cloud Run (Containerized)

1. **Build and push Docker image:**
   ```bash
   gcloud builds submit --tag gcr.io/YOUR_PROJECT_ID/stroke-prediction
   ```

2. **Deploy to Cloud Run:**
   ```bash
   gcloud run deploy stroke-prediction \
     --image gcr.io/YOUR_PROJECT_ID/stroke-prediction \
     --platform managed \
     --allow-unauthenticated \
     --set-env-vars SECRET_KEY=your-key
   ```

## Security Checklist

- ✅ Environment variables configured
- ✅ Firebase service account key secured
- ✅ Debug mode disabled
- ✅ HTTPS enabled (automatic with App Engine)
- ✅ CORS configured for production domain
- ✅ Database connections secured
- ✅ File upload restrictions in place

## Monitoring & Maintenance

### Logging
- View logs: `gcloud app logs tail`
- Set up Cloud Logging alerts

### Monitoring
- Enable Cloud Monitoring
- Set up uptime checks
- Configure error reporting

### Backup
- Database backups (if using Cloud SQL)
- File storage backups (if using Cloud Storage)

## Performance Optimization

### App Engine Scaling
- Automatic scaling configured in app.yaml
- Monitor instance usage in GCP Console

### Database Optimization
- Use connection pooling
- Implement caching (Redis/Memcache)
- Database indexing

### CDN
- Use Cloud CDN for static assets
- Configure caching headers

## Cost Optimization

### App Engine
- Monitor instance hours
- Use appropriate instance classes
- Set up budget alerts

### Database
- Choose appropriate storage tier
- Monitor query performance
- Set up automated backups

## Troubleshooting

### Common Issues
1. **Deployment fails**: Check app.yaml configuration
2. **Environment variables**: Verify in GCP Console
3. **Firebase auth fails**: Check service account permissions
4. **Database connection**: Verify connection strings

### Support
- GCP Documentation: https://cloud.google.com/appengine/docs
- Firebase Docs: https://firebase.google.com/docs
- Stack Overflow: Tag with `google-app-engine` and `firebase`

## Post-Deployment Checklist

- [ ] App accessible via HTTPS
- [ ] Firebase authentication working
- [ ] Email notifications functional
- [ ] Database connections established
- [ ] Static files loading correctly
- [ ] Error logging configured
- [ ] Monitoring alerts set up
- [ ] SSL certificate valid
- [ ] Domain configured (if custom)

---

**Estimated Monthly Cost**: $10-50 for small production deployment
**Expected Performance**: <1s response time, 99.9% uptime