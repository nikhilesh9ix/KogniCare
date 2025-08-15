from datetime import datetime

class Patient:
    """Patient data model"""
    def __init__(self, name, age, gender, room, admission_date, condition, attending_doctor, nurse):
        self.name = name
        self.age = age
        self.gender = gender
        self.room = room
        self.admission_date = admission_date
        self.condition = condition
        self.attending_doctor = attending_doctor
        self.nurse = nurse
        self.created_at = datetime.now()
    
    def to_dict(self):
        return {
            'name': self.name,
            'age': self.age,
            'gender': self.gender,
            'room': self.room,
            'admission_date': self.admission_date,
            'condition': self.condition,
            'attending_doctor': self.attending_doctor,
            'nurse': self.nurse
        }

class VitalSigns:
    """Vital signs data model"""
    def __init__(self, heart_rate=78, spo2=98, temperature=37.1, respiratory_rate=16):
        self.heart_rate = heart_rate
        self.spo2 = spo2
        self.temperature = temperature
        self.respiratory_rate = respiratory_rate
        self.timestamp = datetime.now().isoformat()
    
    def to_dict(self):
        return {
            'heart_rate': self.heart_rate,
            'spo2': self.spo2,
            'temperature': self.temperature,
            'respiratory_rate': self.respiratory_rate,
            'timestamp': self.timestamp
        }

class Alert:
    """Alert data model"""
    def __init__(self, alert_type, vital, value, message):
        self.id = None  # Will be set when added to alerts list
        self.type = alert_type
        self.vital = vital
        self.value = value
        self.message = message
        self.timestamp = datetime.now().isoformat()
        self.acknowledged = False
    
    def to_dict(self):
        return {
            'id': self.id,
            'type': self.type,
            'vital': self.vital,
            'value': self.value,
            'message': self.message,
            'timestamp': self.timestamp,
            'acknowledged': self.acknowledged
        }
