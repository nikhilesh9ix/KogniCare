# KogniCare Render Deployment Checklist

## Pre-Deployment Checklist

### 📁 Files Required
- [x] `app.py` - Main Flask application
- [x] `requirements.txt` - Python dependencies (including gunicorn)
- [x] `Procfile` - Process configuration for Render
- [x] `render.yaml` - Render service configuration (optional)
- [x] `.gitignore` - Exclude sensitive files
- [x] `templates/` - HTML templates directory
- [x] `static/` - Static assets directory

### 🔧 Configuration Check
- [x] App configured to read `PORT` from environment
- [x] Debug mode controlled by `DEBUG` environment variable
- [x] Host set to `0.0.0.0` for external access
- [x] Gunicorn added to requirements.txt
- [x] Health check endpoint available at `/api/health`

### 🚀 Deployment Steps

1. **Repository Setup**
   - [ ] Push code to GitHub/GitLab/Bitbucket
   - [ ] Ensure `.env` file is NOT in repository (check .gitignore)
   - [ ] Verify all necessary files are committed

2. **Render Configuration**
   - [ ] Create new Web Service on Render
   - [ ] Connect your repository
   - [ ] Set build command: `pip install -r requirements.txt`
   - [ ] Set start command: `gunicorn app:app`
   - [ ] Choose appropriate instance type (Free tier available)

3. **Environment Variables**
   - [ ] Set `OPENROUTER_API_KEY` (if using AI features)
   - [ ] Set `DEBUG=False` for production
   - [ ] Other variables (optional):
     - `AI_MODEL` (default: microsoft/phi-3.5-mini-128k-instruct)
     - `OPENROUTER_URL` (default: https://openrouter.ai/api/v1/chat/completions)

4. **Post-Deployment Testing**
   - [ ] Visit deployed URL
   - [ ] Test dashboard loads properly
   - [ ] Verify vital signs simulation works
   - [ ] Test health check: `https://your-app.onrender.com/api/health`
   - [ ] Test AI chat (if API key configured)
   - [ ] Generate and download a test report

### 🔍 Monitoring

**Health Check Endpoint:** `/api/health`
```json
{
  "status": "healthy",
  "timestamp": "2024-01-01T12:00:00Z",
  "service": "kognicare",
  "version": "1.0.0"
}
```

**System Status Endpoint:** `/api/system/status`
- Shows AI API availability
- Displays system statistics
- Reports service health

### ⚠️ Important Notes

- **Free Tier:** Render free tier spins down after 15 minutes of inactivity
- **Cold Starts:** First request after spin-down may take 30-60 seconds
- **Logs:** Monitor deployment logs for any startup errors
- **HTTPS:** Render automatically provides SSL certificates

### 🆘 Troubleshooting

**Build Fails:**
- Check requirements.txt syntax
- Verify Python version compatibility
- Review build logs in Render dashboard

**App Won't Start:**
- Verify start command: `gunicorn app:app`
- Check that main file is named `app.py`
- Review application logs

**Features Not Working:**
- AI Chat: Verify `OPENROUTER_API_KEY` is set
- Reports: Check ReportLab dependency in requirements.txt
- Static Files: Ensure files are in `static/` directory

### 📊 Expected Deployment Time
- **Initial Deploy:** 3-5 minutes
- **Subsequent Deploys:** 2-3 minutes
- **Cold Start (Free Tier):** 30-60 seconds

---

✅ **Ready for Production!** Your KogniCare application is now configured for Render deployment.
