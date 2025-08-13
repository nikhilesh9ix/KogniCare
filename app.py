from flask import Flask, render_template, jsonify, request, send_file
from flask_cors import CORS
import json
import random
import time
from datetime import datetime, timedelta
import threading
import requests
import io
from reportlab.lib.pagesizes import letter
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.units import inch
from reportlab.lib import colors
import csv
import os

app = Flask(__name__)
CORS(app)

# Global variables for real-time data
current_vitals = {
    'heart_rate': 78,
    'spo2': 98,
    'temperature': 37.1,
    'respiratory_rate': 16,
    'timestamp': datetime.now().isoformat()
}

# Store historical data
vitals_history = []
alerts_list = []

# Flag to track if simulation is started
simulation_started = False

# Patient information
patient_info = {
    'name': 'John Doe',
    'age': 65,
    'gender': 'Male',
    'room': 'ICU-201',
    'admission_date': '2 days ago',
    'condition': 'Cancer',
    'attending_doctor': 'Dr. Sarah Wilson',
    'nurse': 'Emily Johnson'
}

# Normal ranges for vitals - optimized to reduce false alerts
VITAL_RANGES = {
    'heart_rate': {'normal': (60, 100), 'warning': (45, 120), 'critical': (35, 140)},
    'spo2': {'normal': (95, 100), 'warning': (88, 94), 'critical': (0, 87)},
    'temperature': {'normal': (36.0, 38.0), 'warning': (35.0, 39.0), 'critical': (33.0, 41.0)},
    'respiratory_rate': {'normal': (10, 25), 'warning': (8, 30), 'critical': (5, 35)}
}

def get_vital_status(vital_name, value):
    """Determine the status of a vital sign"""
    ranges = VITAL_RANGES[vital_name]
    
    if ranges['normal'][0] <= value <= ranges['normal'][1]:
        return 'normal'
    elif ranges['warning'][0] <= value <= ranges['warning'][1]:
        return 'warning'
    else:
        return 'critical'

def generate_realistic_vitals():
    """Generate realistic vital signs with controlled variation"""
    global current_vitals
    
    # Production mode: even more conservative
    is_production = os.environ.get('DEBUG', 'False').lower() == 'false'
    
    if is_production:
        # Very minimal changes in production
        current_vitals['heart_rate'] += random.randint(-1, 1) if random.random() < 0.2 else 0
        current_vitals['spo2'] += random.randint(-1, 1) if random.random() < 0.1 else 0
        current_vitals['temperature'] += random.uniform(-0.05, 0.05) if random.random() < 0.2 else 0
        current_vitals['respiratory_rate'] += random.randint(-1, 1) if random.random() < 0.15 else 0
        
        # Stay well within normal ranges
        current_vitals['heart_rate'] = max(70, min(90, current_vitals['heart_rate']))
        current_vitals['spo2'] = max(97, min(100, current_vitals['spo2']))
        current_vitals['temperature'] = max(36.5, min(37.3, round(current_vitals['temperature'], 1)))
        current_vitals['respiratory_rate'] = max(14, min(20, current_vitals['respiratory_rate']))
    else:
        # Development mode: more variation for testing
        current_vitals['heart_rate'] += random.randint(-2, 2)
        current_vitals['spo2'] += random.randint(-1, 1) if random.random() < 0.3 else 0
        current_vitals['temperature'] += random.uniform(-0.1, 0.1)
        current_vitals['respiratory_rate'] += random.randint(-1, 1) if random.random() < 0.4 else 0
        
        # Keep within normal ranges to minimize alerts
        current_vitals['heart_rate'] = max(65, min(95, current_vitals['heart_rate']))
        current_vitals['spo2'] = max(96, min(100, current_vitals['spo2']))
        current_vitals['temperature'] = max(36.2, min(37.8, round(current_vitals['temperature'], 1)))
        current_vitals['respiratory_rate'] = max(12, min(22, current_vitals['respiratory_rate']))
    
    current_vitals['timestamp'] = datetime.now().isoformat()
    
    # Add to history
    vitals_history.append(current_vitals.copy())
    
    # Keep only last 100 readings
    if len(vitals_history) > 100:
        vitals_history.pop(0)
    
    # Check for alerts less frequently in production
    check_frequency = 0.1 if is_production else 0.3
    if random.random() < check_frequency:
        check_vitals_alerts()
    check_vitals_alerts()

def check_vitals_alerts():
    """Check vital signs and generate alerts if necessary"""
    global alerts_list
    
    # Limit total alerts to prevent memory issues
    MAX_ALERTS = 50
    
    for vital_name, value in current_vitals.items():
        if vital_name == 'timestamp':
            continue
            
        status = get_vital_status(vital_name, value)
        
        if status in ['warning', 'critical']:
            # Check for recent similar alerts (within 60 seconds)
            current_time = datetime.now()
            recent_alerts = [a for a in alerts_list if 
                           a['vital'] == vital_name and 
                           a['type'] == status and
                           (current_time - datetime.fromisoformat(a['timestamp'])).total_seconds() < 60]
            
            # Only add alert if no recent similar alerts
            if not recent_alerts and len(alerts_list) < MAX_ALERTS:
                alert = {
                    'id': len(alerts_list) + 1,
                    'type': status,
                    'vital': vital_name,
                    'value': value,
                    'message': f"{vital_name.replace('_', ' ').title()} is {status}: {value}",
                    'timestamp': current_time.isoformat(),
                    'acknowledged': False
                }
                alerts_list.append(alert)
                # Reduce console spam in production
                if len(alerts_list) <= 10:  # Only log first 10 alerts
                    print(f"Alert generated: {alert['message']}")
    
    # Keep only recent alerts (last 30 minutes)
    cutoff_time = datetime.now() - timedelta(minutes=30)
    alerts_list = [a for a in alerts_list if 
                   datetime.fromisoformat(a['timestamp']) > cutoff_time]

def vitals_simulation():
    """Background thread to simulate real-time vitals"""
    try:
        while True:
            generate_realistic_vitals()
            time.sleep(10)  # Update every 10 seconds (reduced frequency)
    except Exception as e:
        print(f"Simulation error: {e}")
        # Restart simulation after error
        time.sleep(5)
        vitals_simulation()

def start_simulation():
    """Start the vitals simulation if not already started"""
    global simulation_started
    
    # Skip simulation if disabled via environment variable
    if os.environ.get('DISABLE_SIMULATION', 'false').lower() == 'true':
        return
        
    if not simulation_started:
        try:
            simulation_thread = threading.Thread(target=vitals_simulation, daemon=True)
            simulation_thread.start()
            simulation_started = True
            print("Vitals simulation started")
        except Exception as e:
            print(f"Failed to start simulation: {e}")

@app.route('/')
def index():
    """Serve the main dashboard"""
    start_simulation()  # Start simulation on first request
    return render_template('index.html')

@app.route('/api/vitals')
def get_vitals():
    """Get current vital signs"""
    start_simulation()  # Ensure simulation is running
    return jsonify(current_vitals)

@app.route('/api/health')
def health_check():
    """Health check endpoint for monitoring"""
    return jsonify({
        'status': 'healthy',
        'timestamp': datetime.now().isoformat(),
        'service': 'kognicare',
        'version': '1.0.0'
    })

@app.route('/api/vitals/history')
def get_vitals_history():
    """Get historical vital signs data"""
    return jsonify(vitals_history[-20:])  # Last 20 readings

@app.route('/api/patient')
def get_patient_info():
    """Get patient information"""
    return jsonify(patient_info)

@app.route('/api/alerts')
def get_alerts():
    """Get current alerts"""
    return jsonify(alerts_list[-10:])  # Last 10 alerts

@app.route('/api/alerts/clear', methods=['POST'])
def clear_alerts():
    """Clear all alerts"""
    global alerts_list
    alerts_list = []
    return jsonify({'success': True, 'message': 'All alerts cleared'})

@app.route('/api/alerts/test', methods=['POST'])
def test_emergency():
    """Generate a test emergency alert"""
    global alerts_list
    
    test_alert = {
        'id': len(alerts_list) + 1,
        'type': 'critical',
        'vital': 'heart_rate',
        'value': 180,
        'message': 'TEST ALERT: Critical heart rate detected - 180 BPM',
        'timestamp': datetime.now().isoformat(),
        'acknowledged': False
    }
    
    alerts_list.append(test_alert)
    return jsonify({'success': True, 'alert': test_alert})

@app.route('/api/chat', methods=['POST'])
def chat_with_ai():
    """Chat with AI assistant using Phi-3.5 Mini 128K Instruct via OpenRouter API"""
    try:
        data = request.get_json()
        user_message = data.get('message', '')
        
        # Prepare context for the AI
        system_prompt = """You are a medical AI assistant helping healthcare professionals monitor patients. 
        Provide helpful, professional medical insights while always recommending consulting with a doctor for medical decisions.
        Keep responses concise but informative."""
        
        user_context = f"""
        Current Patient: {patient_info['name']}
        Current Vitals: Heart Rate: {current_vitals['heart_rate']} BPM, SpO2: {current_vitals['spo2']}%, 
        Temperature: {current_vitals['temperature']}°C, Respiratory Rate: {current_vitals['respiratory_rate']} BPM
        
        Recent Alerts: {len(alerts_list)} total alerts
        
        Question: {user_message}
        """
        
        # Try to call OpenRouter API with Phi-3.5 Mini 128K Instruct
        try:
            api_response = requests.post(
                'https://openrouter.ai/api/v1/chat/completions',
                headers={
                    'Authorization': 'Bearer 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',
                    'Content-Type': 'application/json',
                    'HTTP-Referer': 'http://localhost:5000',
                    'X-Title': 'Kognicare Patient Monitoring'
                },
                json={
                    'model': 'microsoft/phi-3.5-mini-128k-instruct',
                    'messages': [
                        {'role': 'system', 'content': system_prompt},
                        {'role': 'user', 'content': user_context}
                    ],
                    'max_tokens': 500,
                    'temperature': 0.7
                },
                timeout=30
            )
            
            if api_response.status_code == 200:
                response_data = api_response.json()
                ai_response = response_data['choices'][0]['message']['content']
            else:
                raise Exception(f"API Error: {api_response.status_code}")
                
        except Exception as e:
            print(f"AI API Error: {e}")
            # Fallback response if API is not available
            ai_response = f"""I'm currently operating in fallback mode. Based on your question about "{user_message}", here are some general insights:

Current patient status: Heart Rate {current_vitals['heart_rate']} BPM, SpO2 {current_vitals['spo2']}%, Temp {current_vitals['temperature']}°C

Key recommendations:
- Continue monitoring vital signs closely
- Watch for any trending changes in heart rate or oxygen saturation
- Ensure patient comfort and proper positioning
- Maintain communication with attending physician

Please consult with Dr. Sarah Wilson for any specific medical concerns or decisions."""

        return jsonify({
            'response': ai_response,
            'timestamp': datetime.now().isoformat()
        })
        
    except Exception as e:
        return jsonify({
            'error': 'Failed to process chat request',
            'details': str(e)
        }), 500

@app.route('/api/report/generate', methods=['POST'])
def generate_patient_report():
    """Generate a PDF patient report"""
    try:
        # Create a BytesIO buffer
        buffer = io.BytesIO()
        
        # Create the PDF document
        doc = SimpleDocTemplate(buffer, pagesize=letter)
        story = []
        
        # Get styles
        styles = getSampleStyleSheet()
        title_style = ParagraphStyle(
            'CustomTitle',
            parent=styles['Heading1'],
            fontSize=18,
            spaceAfter=30,
            textColor=colors.HexColor('#0ea5e9')
        )
        
        # Title
        title = Paragraph("Patient Monitoring Report", title_style)
        story.append(title)
        story.append(Spacer(1, 12))
        
        # Patient Information
        patient_data = [
            ['Patient Name:', patient_info['name']],
            ['Age:', str(patient_info['age'])],
            ['Gender:', patient_info['gender']],
            ['Room:', patient_info['room']],
            ['Admission:', patient_info['admission_date']],
            ['Condition:', patient_info['condition']],
            ['Attending Doctor:', patient_info['attending_doctor']],
            ['Nurse:', patient_info['nurse']]
        ]
        
        patient_table = Table(patient_data, colWidths=[2*inch, 4*inch])
        patient_table.setStyle(TableStyle([
            ('BACKGROUND', (0, 0), (0, -1), colors.HexColor('#f8f9fd')),
            ('TEXTCOLOR', (0, 0), (-1, -1), colors.black),
            ('ALIGN', (0, 0), (-1, -1), 'LEFT'),
            ('FONTNAME', (0, 0), (0, -1), 'Helvetica-Bold'),
            ('FONTSIZE', (0, 0), (-1, -1), 10),
            ('GRID', (0, 0), (-1, -1), 1, colors.black)
        ]))
        
        story.append(Paragraph("Patient Information", styles['Heading2']))
        story.append(patient_table)
        story.append(Spacer(1, 20))
        
        # Current Vitals
        vitals_data = [
            ['Vital Sign', 'Current Value', 'Status'],
            ['Heart Rate', f"{current_vitals['heart_rate']} BPM", get_vital_status('heart_rate', current_vitals['heart_rate']).title()],
            ['SpO2', f"{current_vitals['spo2']}%", get_vital_status('spo2', current_vitals['spo2']).title()],
            ['Temperature', f"{current_vitals['temperature']}°C", get_vital_status('temperature', current_vitals['temperature']).title()],
            ['Respiratory Rate', f"{current_vitals['respiratory_rate']} BPM", get_vital_status('respiratory_rate', current_vitals['respiratory_rate']).title()]
        ]
        
        vitals_table = Table(vitals_data, colWidths=[2*inch, 1.5*inch, 1.5*inch])
        vitals_table.setStyle(TableStyle([
            ('BACKGROUND', (0, 0), (-1, 0), colors.HexColor('#0ea5e9')),
            ('TEXTCOLOR', (0, 0), (-1, 0), colors.whitesmoke),
            ('ALIGN', (0, 0), (-1, -1), 'CENTER'),
            ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
            ('FONTSIZE', (0, 0), (-1, -1), 10),
            ('GRID', (0, 0), (-1, -1), 1, colors.black)
        ]))
        
        story.append(Paragraph("Current Vital Signs", styles['Heading2']))
        story.append(vitals_table)
        story.append(Spacer(1, 20))
        
        # Recent Alerts
        if alerts_list:
            story.append(Paragraph("Recent Alerts", styles['Heading2']))
            for alert in alerts_list[-5:]:  # Last 5 alerts
                alert_text = f"• {alert['message']} ({alert['timestamp'][:19]})"
                story.append(Paragraph(alert_text, styles['Normal']))
        
        story.append(Spacer(1, 20))
        
        # Footer
        footer_text = f"Report generated on {datetime.now().strftime('%Y-%m-%d %H:%M:%S')} by Kognicare AI Monitoring System"
        story.append(Paragraph(footer_text, styles['Normal']))
        
        # Build PDF
        doc.build(story)
        
        # Get the value of the BytesIO buffer
        buffer.seek(0)
        
        return send_file(
            buffer,
            as_attachment=True,
            download_name=f"patient_report_{patient_info['name'].replace(' ', '_')}_{datetime.now().strftime('%Y%m%d_%H%M%S')}.pdf",
            mimetype='application/pdf'
        )
        
    except Exception as e:
        return jsonify({
            'error': 'Failed to generate report',
            'details': str(e)
        }), 500

@app.route('/api/system/status')
def system_status():
    """Get system status including AI API availability"""
    try:
        # Check OpenRouter API availability
        api_status = requests.get('https://openrouter.ai/api/v1/models', 
                                 headers={'Authorization': 'Bearer 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'},
                                 timeout=5)
        api_available = api_status.status_code == 200
        
        if api_available:
            models_data = api_status.json()
            phi_available = any('phi-3.5-mini-128k-instruct' in model.get('id', '') for model in models_data.get('data', []))
        else:
            phi_available = False
            
    except Exception:
        api_available = False
        phi_available = False
    
    return jsonify({
        'vitals_simulation': 'active',
        'ai_api_available': api_available,
        'phi3_available': phi_available,
        'ai_provider': 'OpenRouter (Phi-3.5 Mini 128K Instruct)',
        'total_alerts': len(alerts_list),
        'vitals_history_count': len(vitals_history),
        'system_time': datetime.now().isoformat()
    })

if __name__ == "__main__":
    # Create templates directory if it doesn't exist
    if not os.path.exists('templates'):
        os.makedirs('templates')
    
    # Start the simulation thread when running directly (not via gunicorn)
    start_simulation()
    
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)
