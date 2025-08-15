# KogniCare - Render Deployment Guide

This guide will help you deploy your KogniCare application to Render.

## Prerequisites

1. A Render account (sign up at [render.com](https://render.com))
2. Your code pushed to a Git repository (GitHub, GitLab, or Bitbucket)
3. An OpenRouter API key (if using AI features)

## Deployment Steps

### Method 1: Using Render Dashboard (Recommended)

1. **Connect your repository:**
   - Log in to your Render dashboard
   - Click "New +" → "Web Service"
   - Connect your Git repository containing this project

2. **Configure the service:**
   - **Name:** `kognicare` (or your preferred name)
   - **Region:** Choose the closest to your users
   - **Branch:** `main` or `master`
   - **Runtime:** `Python 3`
   - **Build Command:** `pip install -r requirements.txt`
   - **Start Command:** `gunicorn app:app`

3. **Set environment variables:**
   - Go to the "Environment" tab
   - Add the following variables:

     ```bash
     OPENROUTER_API_KEY=your_actual_api_key_here
     DEBUG=False
     ```

4. **Deploy:**
   - Click "Create Web Service"
   - Wait for the build and deployment to complete
   - Your app will be available at `https://your-service-name.onrender.com`

### Method 2: Using render.yaml (Infrastructure as Code)

1. **Push the render.yaml file** (already included in this project)
2. **Connect repository** and Render will automatically detect the configuration
3. **Add environment variables** in the Render dashboard:
   - `OPENROUTER_API_KEY`: Your OpenRouter API key

## Environment Variables

The following environment variables can be configured in Render:

| Variable | Description | Default | Required |
|----------|-------------|---------|----------|
| `OPENROUTER_API_KEY` | Your OpenRouter API key for AI features | - | No (AI features won't work without it) |
| `DEBUG` | Enable debug mode | `False` | No |
| `HOST` | Server host | `0.0.0.0` | No |
| `PORT` | Server port (automatically set by Render) | `5000` | No |

## Post-Deployment

1. **Test the application:**
   - Visit your deployed URL
   - Check that the dashboard loads properly
   - Verify that vital signs simulation is working

2. **Test AI features (if configured):**
   - Generate a health report
   - Check system status endpoint: `https://your-app.onrender.com/api/system/status`

3. **Monitor logs:**
   - Use Render's built-in log viewer to monitor application health
   - Check for any startup errors or runtime issues

## Important Notes

- **Free tier limitations:** Render's free tier spins down after 15 minutes of inactivity
- **Cold starts:** The first request after inactivity may take 30-60 seconds
- **Persistent storage:** Use external services for persistent data storage
- **HTTPS:** Render automatically provides HTTPS for all deployments

## Troubleshooting

### Common Issues

1. **Build fails:**
   - Check that `requirements.txt` includes all dependencies
   - Verify Python version compatibility

2. **Application won't start:**
   - Check the start command: `gunicorn app:app`
   - Verify the main application file is named `app.py`

3. **AI features not working:**
   - Ensure `OPENROUTER_API_KEY` environment variable is set
   - Check API key validity at OpenRouter dashboard

4. **Static files not loading:**
   - Render automatically serves static files from Flask applications
   - Ensure static files are in the `static/` directory

## Support

For Render-specific issues, check:

- [Render Documentation](https://render.com/docs)
- [Render Community Forum](https://community.render.com)

For application-specific issues, refer to the main project documentation.
