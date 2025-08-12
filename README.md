# 🩺 Kognicare - AI-Integrated Patient Monitoring System

*Where AI meets real-time care.*

## 📌 Overview

Kognicare is a smart, AI-powered patient monitoring system MVP that demonstrates real-time health tracking using simulated data. It features a modern web dashboard for healthcare professionals, an LLM-based chatbot for intelligent insights, and automated health alerts.

## 🧠 Key Features

- **Real-Time Vitals Monitoring**: Simulated live updates of heart rate, SpO₂, temperature, and respiratory rate
- **Smart Alert System**: Automated detection of abnormal patterns with severity levels
- **AI Medical Assistant**: LLM-powered chatbot (Phi-3.5 Mini) for medical insights and Q&A
- **Interactive Dashboard**: Modern, responsive UI with live charts and patient information
- **PDF Report Generation**: Automated patient reports with vital trends and alerts
- **Professional Interface**: Hospital-grade design with intuitive navigation

## 🔧 Technical Stack

| Component | Technology |
|-----------|------------|
| Frontend | HTML5, CSS3, JavaScript, Chart.js |
| Backend | Python Flask |
| AI/LLM | Phi-3.5 Mini 128K Instruct via OpenRouter API |
| Data Visualization | Chart.js, Font Awesome |
| Reports | ReportLab (PDF generation) |
| Styling | Modern CSS Grid/Flexbox, Responsive design |

## 🚀 Quick Start

### Prerequisites

- Python 3.8+
- Internet connection (for AI features)
- Modern web browser

### Installation

1. **Clone and setup the project:**
```bash
# Navigate to project directory
cd "c:\Files\Files\BTech College\Projects\Kognicare"

# Install Python dependencies
pip install -r requirements.txt
```

2. **AI Setup:**
The system is pre-configured with Phi-3.5 Mini 128K Instruct via OpenRouter API. No additional setup required - the AI assistant will work out of the box!

3. **Run the application:**
```bash
python app.py
```

4. **Access the dashboard:**
Open your browser to `http://localhost:5000`

## 📊 Features Demonstration

### Real-Time Monitoring
- Live vital signs updates every 5 seconds
- Color-coded status indicators (Normal/Warning/Critical)
- Interactive charts showing trends over time

### AI Assistant
- Natural language queries about patient status
- Contextual responses based on current vitals
- Medical insights and recommendations

### Alert System
- Automated threshold-based alerts
- Emergency notifications for critical conditions
- Alert history and management

### Reporting
- Generate comprehensive PDF reports
- Export chart data
- Patient summary with vital statistics

## 🎯 Project Structure

```
Kognicare/
├── app.py                 # Flask backend application
├── requirements.txt       # Python dependencies
├── templates/
│   └── index.html        # Main dashboard interface
├── README.md             # This file
└── docs/                 # Additional documentation
```

## 🔌 API Endpoints

| Endpoint | Method | Description |
|----------|--------|-------------|
| `/` | GET | Main dashboard |
| `/api/vitals` | GET | Current vital signs |
| `/api/vitals/history` | GET | Historical vital data |
| `/api/patient` | GET | Patient information |
| `/api/alerts` | GET | Current alerts |
| `/api/alerts/clear` | POST | Clear all alerts |
| `/api/alerts/test` | POST | Generate test alert |
| `/api/chat` | POST | AI assistant chat |
| `/api/report/generate` | POST | Generate PDF report |
| `/api/system/status` | GET | System status |

## 🤖 AI Integration

The system integrates with OpenRouter API to provide intelligent medical assistance:

- **Model**: Phi-3.5 Mini 128K Instruct
- **Provider**: Microsoft (via OpenRouter API)
- **Features**: Context-aware responses, medical insights, alert explanations
- **Benefits**: No local setup required, always up-to-date, fast responses

### AI Assistant Capabilities
- Real-time analysis of patient vitals
- Explanation of alerts and their significance  
- Medical insights and recommendations
- Natural language Q&A about patient status
- Context-aware responses based on current patient data

### Fallback Mode
If the API is unavailable, the system operates with intelligent predefined responses to ensure continuous functionality.

## 🎨 Design Features

- **Modern UI**: Clean, hospital-grade design with intuitive navigation
- **Responsive**: Works on desktop, tablet, and mobile devices
- **Real-time Updates**: Live data refresh without page reload
- **Professional Styling**: Medical-themed color scheme and typography
- **Accessibility**: Clear visual indicators and readable fonts

## 🔧 Configuration

### Vital Sign Thresholds
The system monitors the following ranges:

| Vital | Normal | Warning | Critical |
|-------|--------|---------|----------|
| Heart Rate | 60-100 BPM | 50-120 BPM | <40 or >150 BPM |
| SpO₂ | 95-100% | 90-94% | <90% |
| Temperature | 36.0-37.5°C | 35.0-38.5°C | <35 or >38.5°C |
| Respiratory Rate | 12-20 BPM | 8-25 BPM | <8 or >25 BPM |

## 🚀 Future Enhancements

- Integration with real IoT health sensors
- Computer vision for patient movement analysis
- Multi-patient monitoring dashboard
- EMR/EHR system integration
- Advanced AI predictions and trend analysis
- Mobile application
- Cloud deployment with scalability

## 🌐 Deployment

### Deploy to Render

This application is ready for deployment to Render. See [RENDER_DEPLOYMENT.md](RENDER_DEPLOYMENT.md) for detailed instructions.

**Quick Deploy:**

1. Push your code to GitHub/GitLab
2. Connect to Render
3. Set `OPENROUTER_API_KEY` environment variable
4. Deploy with these settings:
   - Build Command: `pip install -r requirements.txt`
   - Start Command: `gunicorn app:app`

### Local Production Mode

To run in production mode locally:

```bash
# Set environment variables
set DEBUG=False
set PORT=8080

# Run with gunicorn
gunicorn app:app --bind 0.0.0.0:8080
```

## 🤝 Contributing

This is an educational MVP project. Contributions and suggestions are welcome:

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Submit a pull request

## ⚠️ Important Notes

- **Educational Purpose**: This is an MVP for demonstration and learning
- **Not for Clinical Use**: Not intended for actual patient monitoring
- **Simulated Data**: All patient data is simulated for demonstration
- **AI Disclaimer**: AI responses are for educational purposes only

## 📝 License

This project is created for educational purposes. Please ensure proper licensing for any commercial use.

## 🆘 Support

For issues or questions:

1. Check the console for error messages
2. Ensure all dependencies are installed
3. Verify Ollama is running (for AI features)
4. Check network connectivity

---

### Built with ❤️ for healthcare innovation and education
