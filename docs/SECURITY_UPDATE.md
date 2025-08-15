# 🚨 IMPORTANT: Setup Required After Cloning

Your repository now uses environment variables for security. **The API key is no longer embedded in the code.**

## Quick Setup for New Users

### 1. Clone and Install
```bash
git clone https://github.com/nikhilesh9ix/KogniCare.git
cd KogniCare
pip install -r requirements.txt
```

### 2. Configure Environment Variables
```bash
# Copy the template
cp .env.example .env

# Edit .env and add your actual API key:
# OPENROUTER_API_KEY=your_actual_api_key_here
```

### 3. Run the Application
```bash
python app.py
# or
start.bat
```

## ✅ Security Improvements Made

- 🔐 **API keys moved to environment variables**
- 🚫 **No sensitive data in version control**
- 📝 **Environment template provided (.env.example)**
- 📚 **Comprehensive setup documentation (ENV_SETUP.md)**
- 🛡️ **Production-ready configuration**

## 🔍 What Changed

1. **config.py**: Now uses `os.getenv()` to load from environment
2. **requirements.txt**: Added `python-dotenv` for .env support
3. **.env.example**: Template showing required variables
4. **ENV_SETUP.md**: Complete environment setup guide

## 🎯 Benefits

- **Secure**: API keys never exposed in Git history
- **Flexible**: Easy to configure for different environments
- **Professional**: Follows industry security best practices
- **Deployable**: Ready for production hosting platforms
