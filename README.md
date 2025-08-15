# Project Title

KogniCare - AI-Integrated Patient Monitoring System

## Team Name and Members

**Team Name:** Enigma

**Team Members:**
- Kuppili Nikhilesh Raju
- Hansika Belgavi

## Problem Statement Reference

Hospitals, especially in emerging markets, face critical patient safety risks due to limited staff, delayed emergency responses, and overwhelming volumes of patient data. The absence of continuous real-time monitoring means early warning signs often go unnoticed, leading to preventable complications, misdiagnosis — particularly in cancer detection — and treatment errors. These gaps not only increase healthcare costs but also put lives at risk, especially in high-demand environments like oncology centers and under-resourced hospitals.

## Overview of your solution

KogniCare is a smart, AI-powered patient monitoring system MVP that demonstrates real-time health tracking using simulated data. It features a modern web dashboard for healthcare professionals, an LLM-based chatbot for intelligent insights, and automated health alerts. The solution addresses the need for continuous patient monitoring with AI-assisted decision making in healthcare environments.

## Features list

- **Real-Time Vitals Monitoring**: Simulated live updates of heart rate, SpO₂, temperature, and respiratory rate
- **Smart Alert System**: Automated detection of abnormal patterns with severity levels
- **AI Medical Assistant**: LLM-powered chatbot (Phi-3.5 Mini) for medical insights and Q&A
- **Interactive Dashboard**: Modern, responsive UI with live charts and patient information
- **PDF Report Generation**: Automated patient reports with vital trends and alerts
- **Professional Interface**: Hospital-grade design with intuitive navigation

## Tech Stack

| Component | Technology |
|-----------|------------|
| Frontend | HTML5, CSS3, JavaScript, Chart.js |
| Backend | Python Flask |
| AI/LLM | Phi-3.5 Mini 128K Instruct via OpenRouter API |
| Data Visualization | Chart.js, Font Awesome |
| Reports | ReportLab (PDF generation) |
| Styling | Modern CSS Grid/Flexbox, Responsive design |

## Installation & Setup instructions

### Prerequisites
- Python 3.8+
- Internet connection (for AI features)
- Modern web browser

### Installation Steps

1. **Clone the repository:**
```bash
git clone https://code.swecha.org/nikhilesh9ix/kognicare.git
cd kognicare
```

2. **Install Python dependencies:**
```bash
pip install -r requirements.txt
```

3. **Run the application:**
```bash
python app.py
```

4. **Access the dashboard:**
Open your browser to `http://localhost:5000`

## Usage guide

1. **Starting the Application**: Run `python app.py` and navigate to `http://localhost:5000`
2. **Monitoring Vitals**: View real-time patient vitals on the main dashboard
3. **AI Assistant**: Use the chat interface to ask questions about patient status
4. **Alerts**: Monitor the alert panel for any critical notifications
5. **Reports**: Generate PDF reports using the report generation feature
6. **Navigation**: Use the intuitive interface to explore different features

## Demo links (video/live deployment)

- **Demo Video**: [Add your demo video link here]
- **Live Deployment**: https://kognicare.onrender.com
- **Presentation**: [Add presentation link if available]

## License

This project is created for educational purposes as part of a hackathon. Please ensure proper licensing for any commercial use.
