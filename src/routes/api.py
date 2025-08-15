from flask import Blueprint, jsonify, request, send_file
from datetime import datetime
from src.services import vitals_simulator, ai_assistant, report_generator
from src.models import Patient

# Create blueprint
api_bp = Blueprint('api', __name__, url_prefix='/api')

# Patient information
patient_info = Patient(
    name='John Doe',
    age=65,
    gender='Male',
    room='ICU-201',
    admission_date='2 days ago',
    condition='Cancer',
    attending_doctor='Dr. Sarah Wilson',
    nurse='Emily Johnson'
).to_dict()

@api_bp.route('/vitals')
def get_vitals():
    """Get current vital signs"""
    vitals_simulator.start_simulation()  # Start controlled simulation
    return jsonify(vitals_simulator.get_current_vitals())

@api_bp.route('/health')
def health_check():
    """Health check endpoint for monitoring"""
    return jsonify({
        'status': 'healthy',
        'timestamp': datetime.now().isoformat(),
        'service': 'kognicare',
        'version': '1.0.0'
    })

@api_bp.route('/vitals/history')
def get_vitals_history():
    """Get historical vital signs data"""
    return jsonify(vitals_simulator.get_vitals_history())

@api_bp.route('/patient')
def get_patient_info():
    """Get patient information"""
    return jsonify(patient_info)

@api_bp.route('/alerts')
def get_alerts():
    """Get current alerts"""
    return jsonify(vitals_simulator.get_alerts())

@api_bp.route('/alerts/clear', methods=['POST'])
def clear_alerts():
    """Clear all alerts"""
    vitals_simulator.clear_alerts()
    return jsonify({'success': True, 'message': 'All alerts cleared'})

@api_bp.route('/alerts/test', methods=['POST'])
def test_emergency():
    """Generate a test emergency alert"""
    test_alert = vitals_simulator.create_test_alert()
    return jsonify({'success': True, 'alert': test_alert})

@api_bp.route('/chat', methods=['POST'])
def chat_with_ai():
    """Chat with AI assistant using Phi-3.5 Mini 128K Instruct via OpenRouter API"""
    try:
        data = request.get_json()
        user_message = data.get('message', '')
        
        current_vitals = vitals_simulator.get_current_vitals()
        alerts = vitals_simulator.get_alerts()
        
        response = ai_assistant.chat(
            user_message, 
            patient_info, 
            current_vitals, 
            len(alerts)
        )
        
        return jsonify(response)
        
    except Exception as e:
        return jsonify({
            'error': 'Failed to process chat request',
            'details': str(e)
        }), 500

@api_bp.route('/report/generate', methods=['POST'])
def generate_patient_report():
    """Generate a PDF patient report"""
    try:
        current_vitals = vitals_simulator.get_current_vitals()
        alerts = vitals_simulator.get_alerts()
        
        buffer = report_generator.generate_patient_report(
            patient_info,
            current_vitals,
            alerts,
            vitals_simulator.get_vital_status
        )
        
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

@api_bp.route('/system/status')
def system_status():
    """Get system status including AI API availability"""
    try:
        ai_status = ai_assistant.check_api_status()
        alerts = vitals_simulator.get_alerts()
        vitals_history = vitals_simulator.get_vitals_history(100)
        
        return jsonify({
            'vitals_simulation': 'active',
            'ai_api_available': ai_status['api_available'],
            'phi3_available': ai_status['phi3_available'],
            'ai_provider': ai_status['provider'],
            'total_alerts': len(alerts),
            'vitals_history_count': len(vitals_history),
            'system_time': datetime.now().isoformat()
        })
    except Exception as e:
        return jsonify({
            'error': 'Failed to get system status',
            'details': str(e)
        }), 500
