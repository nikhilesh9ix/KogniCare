# Kognicare Configuration File

# Patient Information
PATIENT_NAME = "John Doe"
PATIENT_AGE = 65
PATIENT_GENDER = "Male"
PATIENT_ROOM = "ICU-201"
PATIENT_CONDITION = "Cancer"
ATTENDING_DOCTOR = "Dr. Sarah Wilson"
ASSIGNED_NURSE = "Emily Johnson"

# Vital Signs Ranges (Normal, Warning, Critical)
VITAL_RANGES = {
    'heart_rate': {
        'normal': (60, 100),
        'warning': (50, 120),
        'critical': (40, 150)
    },
    'spo2': {
        'normal': (95, 100),
        'warning': (90, 94),
        'critical': (0, 89)
    },
    'temperature': {
        'normal': (36.0, 37.5),
        'warning': (35.0, 38.5),
        'critical': (34.0, 40.0)
    },
    'respiratory_rate': {
        'normal': (12, 20),
        'warning': (8, 25),
        'critical': (6, 30)
    }
}

# Simulation Settings
UPDATE_INTERVAL = 5  # seconds
MAX_HISTORY_RECORDS = 100
MAX_ALERTS_DISPLAY = 10

# AI Settings
OPENROUTER_API_KEY = "OPENROUTER_API_KEY"
OPENROUTER_URL = "OPENROUTER_URL"
AI_MODEL = "microsoft/phi-3.5-mini-128k-instruct"
AI_TIMEOUT = 30  # seconds

# Server Settings
HOST = "0.0.0.0"
PORT = 5000
DEBUG = True
