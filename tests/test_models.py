import unittest
import sys
import os

# Add the project root to Python path
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from src.models import Patient, VitalSigns, Alert

class TestModels(unittest.TestCase):
    """Test cases for data models"""
    
    def test_patient_creation(self):
        """Test patient model creation"""
        patient = Patient(
            name="Test Patient",
            age=30,
            gender="Male",
            room="Test Room",
            admission_date="Today",
            condition="Test Condition",
            attending_doctor="Dr. Test",
            nurse="Nurse Test"
        )
        
        self.assertEqual(patient.name, "Test Patient")
        self.assertEqual(patient.age, 30)
        self.assertEqual(patient.gender, "Male")
        
        # Test to_dict method
        patient_dict = patient.to_dict()
        self.assertIsInstance(patient_dict, dict)
        self.assertEqual(patient_dict['name'], "Test Patient")
    
    def test_vital_signs_creation(self):
        """Test vital signs model creation"""
        vitals = VitalSigns(
            heart_rate=80,
            spo2=98,
            temperature=37.0,
            respiratory_rate=16
        )
        
        self.assertEqual(vitals.heart_rate, 80)
        self.assertEqual(vitals.spo2, 98)
        self.assertEqual(vitals.temperature, 37.0)
        self.assertEqual(vitals.respiratory_rate, 16)
        
        # Test to_dict method
        vitals_dict = vitals.to_dict()
        self.assertIsInstance(vitals_dict, dict)
        self.assertIn('timestamp', vitals_dict)
    
    def test_alert_creation(self):
        """Test alert model creation"""
        alert = Alert(
            alert_type="warning",
            vital="heart_rate",
            value=120,
            message="High heart rate detected"
        )
        
        self.assertEqual(alert.type, "warning")
        self.assertEqual(alert.vital, "heart_rate")
        self.assertEqual(alert.value, 120)
        self.assertFalse(alert.acknowledged)
        
        # Test to_dict method
        alert_dict = alert.to_dict()
        self.assertIsInstance(alert_dict, dict)
        self.assertIn('timestamp', alert_dict)

if __name__ == '__main__':
    unittest.main()
