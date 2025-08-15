import unittest
import sys
import os

# Add the project root to Python path
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from src.services.vitals_service import VitalsSimulator

class TestVitalsService(unittest.TestCase):
    """Test cases for vitals service"""
    
    def setUp(self):
        """Set up test fixtures"""
        self.simulator = VitalsSimulator()
    
    def test_vital_status_normal(self):
        """Test vital status detection for normal values"""
        self.assertEqual(self.simulator.get_vital_status('heart_rate', 75), 'normal')
        self.assertEqual(self.simulator.get_vital_status('spo2', 98), 'normal')
        self.assertEqual(self.simulator.get_vital_status('temperature', 37.0), 'normal')
        self.assertEqual(self.simulator.get_vital_status('respiratory_rate', 18), 'normal')
    
    def test_vital_status_warning(self):
        """Test vital status detection for warning values"""
        self.assertEqual(self.simulator.get_vital_status('heart_rate', 110), 'warning')
        self.assertEqual(self.simulator.get_vital_status('spo2', 92), 'warning')
        self.assertEqual(self.simulator.get_vital_status('temperature', 38.5), 'warning')
        self.assertEqual(self.simulator.get_vital_status('respiratory_rate', 28), 'warning')
    
    def test_vital_status_critical(self):
        """Test vital status detection for critical values"""
        self.assertEqual(self.simulator.get_vital_status('heart_rate', 150), 'critical')
        self.assertEqual(self.simulator.get_vital_status('spo2', 85), 'critical')
        self.assertEqual(self.simulator.get_vital_status('temperature', 40.0), 'critical')
        self.assertEqual(self.simulator.get_vital_status('respiratory_rate', 40), 'critical')
    
    def test_generate_vitals(self):
        """Test vital signs generation"""
        original_vitals = self.simulator.get_current_vitals()
        self.simulator.generate_realistic_vitals()
        new_vitals = self.simulator.get_current_vitals()
        
        # Check that vitals have timestamp
        self.assertIn('timestamp', new_vitals)
        
        # Check that vitals are within reasonable ranges
        self.assertGreater(new_vitals['heart_rate'], 30)
        self.assertLess(new_vitals['heart_rate'], 200)
        self.assertGreater(new_vitals['spo2'], 70)
        self.assertLessEqual(new_vitals['spo2'], 100)
    
    def test_alerts_creation(self):
        """Test alert creation"""
        # Clear any existing alerts
        self.simulator.clear_alerts()
        
        # Create a test alert
        test_alert = self.simulator.create_test_alert()
        
        self.assertIsNotNone(test_alert)
        self.assertEqual(test_alert['type'], 'critical')
        self.assertEqual(test_alert['vital'], 'heart_rate')
        
        # Check that alert was added to the list
        alerts = self.simulator.get_alerts()
        self.assertEqual(len(alerts), 1)
    
    def test_clear_alerts(self):
        """Test clearing alerts"""
        # Create a test alert
        self.simulator.create_test_alert()
        
        # Verify alert exists
        alerts = self.simulator.get_alerts()
        self.assertGreater(len(alerts), 0)
        
        # Clear alerts
        self.simulator.clear_alerts()
        
        # Verify alerts are cleared
        alerts = self.simulator.get_alerts()
        self.assertEqual(len(alerts), 0)

if __name__ == '__main__':
    unittest.main()
