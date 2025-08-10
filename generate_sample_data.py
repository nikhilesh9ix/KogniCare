import json
from datetime import datetime, timedelta
import random

def generate_sample_vitals_data(hours=24):
    """Generate sample historical vitals data for demonstration"""
    data = []
    start_time = datetime.now() - timedelta(hours=hours)
    
    # Base values
    base_hr = 75
    base_spo2 = 97
    base_temp = 36.8
    base_resp = 16
    
    for i in range(hours * 12):  # Every 5 minutes
        timestamp = start_time + timedelta(minutes=i * 5)
        
        # Add realistic variations
        hr_variation = random.randint(-5, 8)
        spo2_variation = random.randint(-2, 3)
        temp_variation = random.uniform(-0.3, 0.4)
        resp_variation = random.randint(-2, 4)
        
        # Create occasional anomalies
        if random.random() < 0.05:  # 5% chance of anomaly
            hr_variation += random.choice([-15, 20])
        
        data.append({
            'timestamp': timestamp.isoformat(),
            'heart_rate': max(40, min(150, base_hr + hr_variation)),
            'spo2': max(85, min(100, base_spo2 + spo2_variation)),
            'temperature': round(max(35.0, min(40.0, base_temp + temp_variation)), 1),
            'respiratory_rate': max(8, min(30, base_resp + resp_variation))
        })
    
    return data

def generate_sample_alerts():
    """Generate sample alert history"""
    alerts = [
        {
            'id': 1,
            'type': 'warning',
            'vital': 'heart_rate',
            'value': 105,
            'message': 'Heart rate elevated - 105 BPM',
            'timestamp': (datetime.now() - timedelta(hours=2)).isoformat(),
            'acknowledged': True
        },
        {
            'id': 2,
            'type': 'normal',
            'vital': 'spo2',
            'value': 98,
            'message': 'SpO2 returned to normal range - 98%',
            'timestamp': (datetime.now() - timedelta(hours=1)).isoformat(),
            'acknowledged': True
        },
        {
            'id': 3,
            'type': 'warning',
            'vital': 'temperature',
            'value': 38.2,
            'message': 'Temperature slightly elevated - 38.2°C',
            'timestamp': (datetime.now() - timedelta(minutes=30)).isoformat(),
            'acknowledged': False
        }
    ]
    return alerts

if __name__ == "__main__":
    # Generate sample data
    vitals_data = generate_sample_vitals_data(24)
    alerts_data = generate_sample_alerts()
    
    # Save to files
    with open('sample_vitals.json', 'w') as f:
        json.dump(vitals_data, f, indent=2)
    
    with open('sample_alerts.json', 'w') as f:
        json.dump(alerts_data, f, indent=2)
    
    print("✅ Sample data generated:")
    print(f"  - {len(vitals_data)} vitals records (24 hours)")
    print(f"  - {len(alerts_data)} sample alerts")
    print("  - Files: sample_vitals.json, sample_alerts.json")
