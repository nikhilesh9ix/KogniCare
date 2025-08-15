# KogniCare - AI-Integrated Patient Monitoring System

## 📁 Project Structure

```
KogniCare/
├── 📁 src/                          # Source code
│   ├── 📁 models/                   # Data models
│   │   └── __init__.py             # Patient, VitalSigns, Alert models
│   ├── 📁 routes/                   # Flask routes/blueprints
│   │   ├── __init__.py
│   │   ├── main.py                 # Main dashboard routes
│   │   └── api.py                  # API endpoints
│   ├── 📁 services/                 # Business logic services
│   │   ├── __init__.py
│   │   ├── vitals_service.py       # Vitals simulation & management
│   │   ├── ai_service.py           # AI chat integration
│   │   └── report_service.py       # PDF report generation
│   ├── 📁 utils/                    # Utility functions
│   │   ├── __init__.py
│   │   ├── config.py               # Configuration management
│   │   └── helpers.py              # Helper functions
│   └── __init__.py
├── 📁 static/                       # Static assets
│   ├── 📁 css/                     # Stylesheets
│   ├── 📁 js/                      # JavaScript files
│   ├── 📁 media/                   # Images, videos
│   └── README.md
├── 📁 templates/                    # Jinja2 templates
│   └── index.html                  # Main dashboard template
├── 📁 tests/                       # Test files
│   ├── __init__.py
│   ├── test_models.py              # Model tests
│   └── test_services.py            # Service tests
├── 📁 scripts/                     # Utility scripts
│   ├── generate_sample_data.py     # Data generation
│   ├── setup.bat                   # Windows setup
│   ├── start.bat                   # Windows start script
│   └── start.sh                    # Unix start script
├── 📁 docs/                        # Documentation
│   ├── 📁 deployment/              # Deployment guides
│   │   ├── DEPLOYMENT_CHANGES_SUMMARY.md
│   │   ├── DEPLOYMENT_CHECKLIST.md
│   │   ├── DEPLOYMENT_FIX.md
│   │   └── RENDER_DEPLOYMENT.md
│   ├── 📁 setup/                   # Setup guides
│   │   ├── ENV_SETUP.md
│   │   ├── OLLAMA_SETUP.md
│   │   ├── SETUP_GUIDE.md
│   │   └── VIDEO_SETUP.md
│   ├── CONTRIBUTING.md
│   ├── PROJECT_SUMMARY.md
│   └── SECURITY_UPDATE.md
├── app.py                          # Main application entry point
├── app_original_backup.py          # Backup of original monolithic app
├── run_dev.py                      # Development server runner
├── run_prod.py                     # Production server runner
├── run_tests.py                    # Test runner
├── config.py                       # Legacy config (for compatibility)
├── requirements.txt                # Python dependencies
├── Procfile                        # Heroku deployment
├── .env.example                    # Environment variables template
├── .env.template                   # Alternative env template
├── .gitignore                      # Git ignore rules
└── README.md                       # This file
```

## 🚀 Quick Start

### Development Mode
```bash
# Install dependencies
pip install -r requirements.txt

# Copy environment template
cp .env.template .env
# Edit .env with your configuration

# Run development server
python run_dev.py
```

### Production Mode
```bash
# Run production server
python run_prod.py

# Or with Gunicorn
gunicorn -w 4 -b 0.0.0.0:5000 run_prod:app
```

### Running Tests
```bash
python run_tests.py
```

## 🏗️ Architecture Overview

### **Modular Design**
- **Separation of Concerns**: Each module has a specific responsibility
- **Scalability**: Easy to add new features and services
- **Maintainability**: Clean, organized code structure
- **Testability**: Each component can be tested independently

### **Core Components**

#### **Models** (`src/models/`)
- **Patient**: Patient information data model
- **VitalSigns**: Vital signs data structure
- **Alert**: Alert/notification data model

#### **Services** (`src/services/`)
- **VitalsSimulator**: Real-time vitals simulation and monitoring
- **AIAssistant**: Integration with Phi-3.5 Mini AI model
- **ReportGenerator**: PDF report generation service

#### **Routes** (`src/routes/`)
- **Main Routes**: Dashboard and UI endpoints
- **API Routes**: RESTful API endpoints for data access

#### **Utils** (`src/utils/`)
- **Configuration**: Environment-based configuration management
- **Helpers**: Utility functions for data processing

## 🔧 Configuration

### Environment Variables
Create a `.env` file based on `.env.template`:

```env
# Flask Configuration
DEBUG=false
SECRET_KEY=your-secret-key-here

# AI Service Configuration
OPENROUTER_API_KEY=your-api-key-here
AI_MODEL=microsoft/phi-3.5-mini-128k-instruct

# Simulation Configuration
DISABLE_SIMULATION=false
SIMULATION_INTERVAL_PROD=30
SIMULATION_INTERVAL_DEV=10

# Server Configuration
PORT=5000
HOST=0.0.0.0
```

## 📊 API Endpoints

### **Vitals Management**
- `GET /api/vitals` - Get current vital signs
- `GET /api/vitals/history` - Get historical data
- `GET /api/patient` - Get patient information

### **Alert System**
- `GET /api/alerts` - Get current alerts
- `POST /api/alerts/clear` - Clear all alerts
- `POST /api/alerts/test` - Generate test alert

### **AI Integration**
- `POST /api/chat` - Chat with AI assistant

### **Reports**
- `POST /api/report/generate` - Generate PDF report

### **System**
- `GET /api/health` - Health check
- `GET /api/system/status` - System status

## 🧪 Testing

The project includes comprehensive tests for:
- **Data Models**: Patient, VitalSigns, Alert classes
- **Services**: Vitals simulation, AI integration, reports
- **API Endpoints**: All REST API functionality

Run tests with:
```bash
python run_tests.py
```

## 🔄 Benefits of New Structure

### **Before (Monolithic)**
- Single 493-line `app.py` file
- All functionality mixed together
- Difficult to maintain and extend
- Hard to test individual components

### **After (Modular)**
- ✅ **Organized**: Clear separation of concerns
- ✅ **Maintainable**: Easy to modify individual components
- ✅ **Scalable**: Simple to add new features
- ✅ **Testable**: Comprehensive test coverage
- ✅ **Configurable**: Environment-based configuration
- ✅ **Production-Ready**: Proper deployment structure

## 🚀 Deployment

### **Development**
```bash
python run_dev.py
```

### **Production (Direct)**
```bash
python run_prod.py
```

### **Production (Gunicorn)**
```bash
gunicorn -w 4 -b 0.0.0.0:5000 run_prod:app
```

### **Docker** (Future Enhancement)
```dockerfile
FROM python:3.9-slim
WORKDIR /app
COPY requirements.txt .
RUN pip install -r requirements.txt
COPY . .
CMD ["python", "run_prod.py"]
```

## 📈 Future Enhancements

1. **Database Integration**: Add SQLAlchemy for data persistence
2. **User Authentication**: Implement user management system
3. **Real Device Integration**: Connect to actual medical devices
4. **Advanced Analytics**: Machine learning for predictive analytics
5. **Mobile App**: React Native or Flutter mobile application
6. **Microservices**: Split into independent microservices
7. **Container Orchestration**: Kubernetes deployment
8. **Real-time Notifications**: WebSocket integration

## 🤝 Contributing

Please refer to `docs/CONTRIBUTING.md` for contribution guidelines.

## 📄 License

See the original project documentation for license information.

---

*This modular structure provides a solid foundation for scaling the KogniCare application while maintaining code quality and developer productivity.*
