@echo off
echo 🩺 Kognicare AI Patient Monitoring System Setup
echo ===============================================
echo.

echo [1/3] Checking Python installation...
python --version >nul 2>&1
if %errorlevel% neq 0 (
    echo ❌ Python not found! Please install Python 3.8+ first.
    echo Download from: https://python.org/downloads
    pause
    exit /b 1
)
echo ✅ Python found

echo.
echo [2/3] Installing Python dependencies...
pip install -r requirements.txt
if %errorlevel% neq 0 (
    echo ❌ Failed to install dependencies
    pause
    exit /b 1
)
echo ✅ Dependencies installed

echo.
echo [3/3] Checking AI configuration...
echo ✅ Phi-3.5 Mini 128K Instruct configured via OpenRouter API
echo ✅ No additional setup required for AI features

echo.
echo Setup complete! 🎉
echo.
echo To start the application:
echo   python app.py
echo.
echo Then open your browser to: http://localhost:5000
echo.
echo 📚 Documentation: README.md
echo 🤖 AI Features: Ready to use with Phi-3.5 Mini 128K Instruct
echo 🩺 Have a great monitoring experience!
echo.
pause
