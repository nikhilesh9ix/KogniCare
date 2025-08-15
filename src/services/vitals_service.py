import random
import time
import threading
import os
from datetime import datetime, timedelta
from src.models import VitalSigns, Alert

class VitalsSimulator:
    """Handles real-time vitals simulation"""
    
    def __init__(self):
        self.current_vitals = VitalSigns()
        self.vitals_history = []
        self.alerts_list = []
        self.simulation_started = False
        
        # Normal ranges for vitals - optimized to reduce false alerts
        self.VITAL_RANGES = {
            'heart_rate': {'normal': (60, 100), 'warning': (45, 120), 'critical': (35, 140)},
            'spo2': {'normal': (95, 100), 'warning': (88, 94), 'critical': (0, 87)},
            'temperature': {'normal': (36.0, 38.0), 'warning': (35.0, 39.0), 'critical': (33.0, 41.0)},
            'respiratory_rate': {'normal': (10, 25), 'warning': (8, 30), 'critical': (5, 35)}
        }
    
    def get_vital_status(self, vital_name, value):
        """Determine the status of a vital sign"""
        ranges = self.VITAL_RANGES[vital_name]
        
        if ranges['normal'][0] <= value <= ranges['normal'][1]:
            return 'normal'
        elif ranges['warning'][0] <= value <= ranges['warning'][1]:
            return 'warning'
        else:
            return 'critical'
    
    def generate_realistic_vitals(self):
        """Generate realistic vital signs with controlled variation"""
        # Production mode: very conservative with occasional alerts
        is_production = os.environ.get('DEBUG', 'False').lower() == 'false'
        
        if is_production:
            # Very controlled changes in production - mostly stay normal
            if random.random() < 0.05:  # 5% chance of any change
                self.current_vitals.heart_rate += random.randint(-1, 1)
                self.current_vitals.spo2 += random.randint(-1, 1) if random.random() < 0.3 else 0
                self.current_vitals.temperature += random.uniform(-0.05, 0.05)
                self.current_vitals.respiratory_rate += random.randint(-1, 1) if random.random() < 0.3 else 0
            
            # Occasionally create a brief alert condition (very rare)
            if random.random() < 0.001:  # 0.1% chance of alert condition
                alert_type = random.choice(['temp_high', 'hr_low', 'rr_high'])
                if alert_type == 'temp_high':
                    self.current_vitals.temperature = 38.2  # Warning level
                elif alert_type == 'hr_low':
                    self.current_vitals.heart_rate = 55  # Warning level  
                elif alert_type == 'rr_high':
                    self.current_vitals.respiratory_rate = 26  # Warning level
            
            # Keep within safe bounds - allow brief excursions for alerts
            self.current_vitals.heart_rate = max(50, min(100, self.current_vitals.heart_rate))
            self.current_vitals.spo2 = max(95, min(100, self.current_vitals.spo2))
            self.current_vitals.temperature = max(36.0, min(38.5, round(self.current_vitals.temperature, 1)))
            self.current_vitals.respiratory_rate = max(12, min(28, self.current_vitals.respiratory_rate))
        else:
            # Development mode: more variation for testing
            self.current_vitals.heart_rate += random.randint(-2, 2)
            self.current_vitals.spo2 += random.randint(-1, 1) if random.random() < 0.3 else 0
            self.current_vitals.temperature += random.uniform(-0.1, 0.1)
            self.current_vitals.respiratory_rate += random.randint(-1, 1) if random.random() < 0.4 else 0
            
            # Keep within wider testing ranges
            self.current_vitals.heart_rate = max(45, min(120, self.current_vitals.heart_rate))
            self.current_vitals.spo2 = max(88, min(100, self.current_vitals.spo2))
            self.current_vitals.temperature = max(35.5, min(39.0, round(self.current_vitals.temperature, 1)))
            self.current_vitals.respiratory_rate = max(8, min(30, self.current_vitals.respiratory_rate))
        
        self.current_vitals.timestamp = datetime.now().isoformat()
        
        # Add to history
        self.vitals_history.append(self.current_vitals.to_dict())
        
        # Keep only last 100 readings
        if len(self.vitals_history) > 100:
            self.vitals_history.pop(0)
        
        # Check for alerts - less frequently in production
        check_frequency = 0.1 if is_production else 0.3
        if random.random() < check_frequency:
            self.check_vitals_alerts()
    
    def check_vitals_alerts(self):
        """Check vital signs and generate alerts if necessary"""
        # Limit total alerts to prevent memory issues
        MAX_ALERTS = 50
        
        vitals_dict = self.current_vitals.to_dict()
        for vital_name, value in vitals_dict.items():
            if vital_name == 'timestamp':
                continue
                
            status = self.get_vital_status(vital_name, value)
            
            if status in ['warning', 'critical']:
                # Check for recent similar alerts (within 60 seconds)
                current_time = datetime.now()
                recent_alerts = [a for a in self.alerts_list if 
                               a.vital == vital_name and 
                               a.type == status and
                               (current_time - datetime.fromisoformat(a.timestamp)).total_seconds() < 60]
                
                # Only add alert if no recent similar alerts
                if not recent_alerts and len(self.alerts_list) < MAX_ALERTS:
                    alert = Alert(
                        alert_type=status,
                        vital=vital_name,
                        value=value,
                        message=f"{vital_name.replace('_', ' ').title()} is {status}: {value}"
                    )
                    alert.id = len(self.alerts_list) + 1
                    self.alerts_list.append(alert)
                    # Reduce console spam in production
                    if len(self.alerts_list) <= 10:  # Only log first 10 alerts
                        print(f"Alert generated: {alert.message}")
        
        # Keep only recent alerts (last 30 minutes)
        cutoff_time = datetime.now() - timedelta(minutes=30)
        self.alerts_list = [a for a in self.alerts_list if 
                           datetime.fromisoformat(a.timestamp) > cutoff_time]
    
    def vitals_simulation_loop(self):
        """Background thread to simulate real-time vitals"""
        try:
            is_production = os.environ.get('DEBUG', 'False').lower() == 'false'
            sleep_interval = 30 if is_production else 10  # Slower in production
            
            while True:
                self.generate_realistic_vitals()
                time.sleep(sleep_interval)
        except Exception as e:
            print(f"Simulation error: {e}")
            # Restart simulation after error
            time.sleep(5)
            self.vitals_simulation_loop()
    
    def start_simulation(self):
        """Start the vitals simulation if not already started"""
        # Skip simulation if disabled via environment variable
        if os.environ.get('DISABLE_SIMULATION', 'false').lower() == 'true':
            print("Simulation disabled via DISABLE_SIMULATION environment variable")
            return
        
        # Enable controlled simulation in production
        is_production = os.environ.get('DEBUG', 'False').lower() == 'false'
        if is_production:
            print("Production mode: Starting controlled vitals simulation")
        else:
            print("Development mode: Starting full vitals simulation")
            
        if not self.simulation_started:
            try:
                simulation_thread = threading.Thread(target=self.vitals_simulation_loop, daemon=True)
                simulation_thread.start()
                self.simulation_started = True
                print("Vitals simulation started successfully")
            except Exception as e:
                print(f"Failed to start simulation: {e}")
    
    def get_current_vitals(self):
        """Get current vital signs"""
        return self.current_vitals.to_dict()
    
    def get_vitals_history(self, limit=20):
        """Get historical vital signs data"""
        return self.vitals_history[-limit:]
    
    def get_alerts(self, limit=10):
        """Get current alerts"""
        return [alert.to_dict() for alert in self.alerts_list[-limit:]]
    
    def clear_alerts(self):
        """Clear all alerts"""
        self.alerts_list = []
        return True
    
    def create_test_alert(self):
        """Generate a test emergency alert"""
        test_alert = Alert(
            alert_type='critical',
            vital='heart_rate',
            value=180,
            message='TEST ALERT: Critical heart rate detected - 180 BPM'
        )
        test_alert.id = len(self.alerts_list) + 1
        self.alerts_list.append(test_alert)
        return test_alert.to_dict()

# Global instance
vitals_simulator = VitalsSimulator()
