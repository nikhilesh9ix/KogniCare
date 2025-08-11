# 🔐 Environment Variables Setup

## Security Notice
This project uses environment variables to keep sensitive information (like API keys) secure and out of version control.

## Setup Instructions

### 1. Copy the Environment Template
```bash
cp .env.example .env
```

### 2. Edit the .env File
Open `.env` and replace the placeholder values with your actual configuration:

```env
# OpenRouter API Configuration
OPENROUTER_API_KEY=your_actual_api_key_here
OPENROUTER_URL=https://openrouter.ai/api/v1/chat/completions
AI_MODEL=microsoft/phi-3.5-mini-128k-instruct

# Server Configuration
HOST=0.0.0.0
PORT=5000
DEBUG=True
```

### 3. Get Your OpenRouter API Key
1. Visit [OpenRouter.ai](https://openrouter.ai/)
2. Sign up for an account
3. Navigate to API Keys section
4. Generate a new API key
5. Copy the key and paste it in your `.env` file

### 4. Important Security Notes
- ✅ **Never commit `.env` files** - They contain sensitive information
- ✅ **Use `.env.example`** - This template shows required variables without exposing secrets
- ✅ **Keep API keys private** - Don't share them in chat, email, or public repositories
- ✅ **Rotate keys regularly** - Generate new API keys periodically for security

### 5. Deployment
For production deployment, set environment variables directly in your hosting platform:
- **Heroku**: Use Config Vars in dashboard
- **AWS**: Use Systems Manager Parameter Store or Secrets Manager
- **Azure**: Use App Service Configuration
- **Docker**: Use environment variables in docker-compose.yml

## Troubleshooting

### Missing .env File
If you get an error about missing environment variables:
1. Make sure `.env` file exists in the project root
2. Check that all required variables are set
3. Restart the application after making changes

### Invalid API Key
If AI features don't work:
1. Verify your OpenRouter API key is correct
2. Check that you have sufficient credits on OpenRouter
3. Ensure the API key has the right permissions

### Environment Loading Issues
If environment variables aren't loading:
1. Make sure `python-dotenv` is installed: `pip install python-dotenv`
2. Check that `.env` file is in the same directory as `config.py`
3. Verify the file format matches the example

## Example Production Setup

### Docker Environment
```dockerfile
# In your Dockerfile
ENV OPENROUTER_API_KEY=${OPENROUTER_API_KEY}
ENV DEBUG=False
```

### Docker Compose
```yaml
version: '3.8'
services:
  kognicare:
    build: .
    environment:
      - OPENROUTER_API_KEY=${OPENROUTER_API_KEY}
      - DEBUG=False
      - HOST=0.0.0.0
      - PORT=5000
```

---

**🔒 Remember: Security is crucial in healthcare applications. Always protect sensitive information!**
