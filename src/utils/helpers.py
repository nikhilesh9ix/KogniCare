"""
Utility functions for KogniCare application
"""
from datetime import datetime
import csv
import json

def format_timestamp(timestamp_str):
    """Format timestamp for display"""
    try:
        dt = datetime.fromisoformat(timestamp_str.replace('Z', '+00:00'))
        return dt.strftime('%Y-%m-%d %H:%M:%S')
    except Exception:
        return timestamp_str

def export_vitals_to_csv(vitals_history, filename=None):
    """Export vitals history to CSV file"""
    if not filename:
        filename = f"vitals_export_{datetime.now().strftime('%Y%m%d_%H%M%S')}.csv"
    
    with open(filename, 'w', newline='') as csvfile:
        fieldnames = ['timestamp', 'heart_rate', 'spo2', 'temperature', 'respiratory_rate']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        
        writer.writeheader()
        for vital in vitals_history:
            writer.writerow(vital)
    
    return filename

def export_alerts_to_json(alerts_list, filename=None):
    """Export alerts to JSON file"""
    if not filename:
        filename = f"alerts_export_{datetime.now().strftime('%Y%m%d_%H%M%S')}.json"
    
    with open(filename, 'w') as jsonfile:
        json.dump(alerts_list, jsonfile, indent=2)
    
    return filename

def validate_vital_ranges(vital_name, value):
    """Validate if vital sign value is within expected ranges"""
    ranges = {
        'heart_rate': (30, 200),
        'spo2': (70, 100),
        'temperature': (30.0, 45.0),
        'respiratory_rate': (5, 50)
    }
    
    if vital_name not in ranges:
        return False
    
    min_val, max_val = ranges[vital_name]
    return min_val <= value <= max_val

def calculate_vital_trend(history, vital_name, window=5):
    """Calculate trend for a specific vital sign"""
    if len(history) < window:
        return 'insufficient_data'
    
    recent_values = [entry[vital_name] for entry in history[-window:]]
    
    # Simple trend calculation
    if len(recent_values) >= 2:
        trend = recent_values[-1] - recent_values[0]
        if abs(trend) < 0.1:  # Threshold for stable
            return 'stable'
        elif trend > 0:
            return 'increasing'
        else:
            return 'decreasing'
    
    return 'stable'
