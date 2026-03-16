# Heart-Stroke-Risk-Prediction

A comprehensive web application for stroke risk prediction using machine learning, built with Flask and Firebase authentication.

## Features

- 🔐 **Firebase Authentication** (Email/Password + Google Sign-In)
- 🧠 **ML Stroke Risk Prediction** (Ensemble of 3 models)
- 💊 **Medication Reminders** with email notifications
- 📊 **Health History Tracking**
- 👨‍⚕️ **Doctor Recommendations** based on risk factors
- 🍎 **Personalized Food Recommendations**
- 📱 **Responsive Dashboard**
- 🔒 **Production-Ready Security**

## Quick Start (Development)

1. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

2. **Set up environment:**
   ```bash
   cp .env .env.local  # Edit with your values
   ```

3. **Run the application:**
   ```bash
   python app.py
   ```

4. **Open:** http://localhost:5000

## Production Deployment

### Render (Recommended for Simplicity)

Render is perfect for your Flask app with Firebase integration. It offers a generous free tier and automatic deployments.

#### Quick Render Deployment:

1. **Setup for Render:**
   ```bash
   # On Linux/Mac
   ./setup-render.sh

   # On Windows
   setup-render.bat
   ```

2. **Push to GitHub:**
   ```bash
   git add .
   git commit -m "Ready for production"
   git push origin main
   ```

3. **Deploy on Render:**
   - Go to [render.com](https://render.com)
   - Click "New" → "Web Service"
   - Connect your GitHub repository
   - Configure build settings:
     - **Build Command:** `pip install -r requirements.txt`
     - **Start Command:** `gunicorn --bind 0.0.0.0:$PORT main:app --workers 2 --threads 4 --worker-class gthread`

4. **Set Environment Variables:**
   In Render dashboard → Environment:
   ```
   FLASK_ENV=production
   SECRET_KEY=your-secure-key-here
   NEXT_PUBLIC_FIREBASE_API_KEY=your-key
   NEXT_PUBLIC_FIREBASE_AUTH_DOMAIN=your-domain
   NEXT_PUBLIC_FIREBASE_PROJECT_ID=your-project
   EMAIL_SENDER=your-email@gmail.com
   EMAIL_PASSWORD=your-app-password
   ```

5. **Deploy!** 🚀

#### Render Features:
- ✅ **Free Tier:** 750 hours/month
- ✅ **Auto-SSL:** Automatic HTTPS
- ✅ **Auto-deploy:** From Git pushes
- ✅ **Built-in Monitoring**
- ✅ **PostgreSQL Database** (optional add-on)
- ✅ **Custom Domains** supported

### Google Cloud Platform (Alternative)

For GCP deployment, see `PRODUCTION_DEPLOYMENT.md`

### Manual Deployment Options

- **App Engine:** Use `app.yaml` configuration
- **Cloud Run:** Use provided `Dockerfile`
- **Docker:** `docker build -t stroke-prediction .`

## Project Structure

```
├── app.py                 # Main Flask application
├── main.py               # Gunicorn entry point
├── config.py             # Production configuration
├── requirements.txt      # Python dependencies
├── app.yaml             # Google App Engine config
├── Dockerfile           # Container configuration
├── .env.production.template  # Production env template
├── static/              # CSS, JS, images
├── templates/           # HTML templates
├── data/                # JSON data storage
├── saved_models/        # ML models
└── docs/                # Documentation
```

## Environment Variables

### Required for Production:
- `SECRET_KEY`: Flask secret key
- `NEXT_PUBLIC_FIREBASE_*`: Firebase configuration
- `EMAIL_SENDER`: Email for notifications
- `EMAIL_PASSWORD`: App password for email

### Optional:
- `DATABASE_URL`: PostgreSQL connection string
- `REDIS_URL`: Redis for caching
- `SENTRY_DSN`: Error monitoring

## API Endpoints

- `GET /health` - Health check
- `POST /predict` - Stroke risk prediction
- `GET/POST /api/medications` - Medication management
- `POST /firebase-login` - Firebase authentication

## Security Features

- ✅ Firebase Authentication
- ✅ CSRF Protection
- ✅ Secure Session Management
- ✅ Input Validation
- ✅ HTTPS Enforcement
- ✅ File Upload Restrictions

## Monitoring & Logging

- Health checks at `/health`
- Structured logging
- Error tracking (optional Sentry integration)
- Performance monitoring

## Contributing

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Add tests if applicable
5. Submit a pull request

## License

This project is licensed under the MIT License - see the LICENSE file for details.

## Support

For deployment issues, see `PRODUCTION_DEPLOYMENT.md`
For Firebase setup, see `FIREBASE_AUTH_README.md`