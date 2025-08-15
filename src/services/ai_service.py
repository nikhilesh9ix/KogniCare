import requests
from datetime import datetime

class AIAssistant:
    """Handles AI chat functionality using Phi-3.5 Mini 128K Instruct via OpenRouter API"""
    
    def __init__(self):
        self.api_key = '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'
        self.base_url = 'https://openrouter.ai/api/v1/chat/completions'
        self.model = 'microsoft/phi-3.5-mini-128k-instruct'
        
        self.system_prompt = """You are a medical AI assistant helping healthcare professionals monitor patients. 
        Provide helpful, professional medical insights while always recommending consulting with a doctor for medical decisions.
        Keep responses concise but informative."""
    
    def chat(self, user_message, patient_info, current_vitals, alerts_count):
        """Process chat message with AI assistant"""
        try:
            user_context = f"""
            Current Patient: {patient_info['name']}
            Current Vitals: Heart Rate: {current_vitals['heart_rate']} BPM, SpO2: {current_vitals['spo2']}%, 
            Temperature: {current_vitals['temperature']}°C, Respiratory Rate: {current_vitals['respiratory_rate']} BPM
            
            Recent Alerts: {alerts_count} total alerts
            
            Question: {user_message}
            """
            
            # Try to call OpenRouter API with Phi-3.5 Mini 128K Instruct
            try:
                api_response = requests.post(
                    self.base_url,
                    headers={
                        'Authorization': f'Bearer {self.api_key}',
                        'Content-Type': 'application/json',
                        'HTTP-Referer': 'http://localhost:5000',
                        'X-Title': 'Kognicare Patient Monitoring'
                    },
                    json={
                        'model': self.model,
                        'messages': [
                            {'role': 'system', 'content': self.system_prompt},
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

Please consult with {patient_info['attending_doctor']} for any specific medical concerns or decisions."""

            return {
                'response': ai_response,
                'timestamp': datetime.now().isoformat()
            }
            
        except Exception as e:
            return {
                'error': 'Failed to process chat request',
                'details': str(e)
            }
    
    def check_api_status(self):
        """Check OpenRouter API availability"""
        try:
            api_status = requests.get(
                'https://openrouter.ai/api/v1/models', 
                headers={'Authorization': f'Bearer {self.api_key}'},
                timeout=5
            )
            api_available = api_status.status_code == 200
            
            if api_available:
                models_data = api_status.json()
                phi_available = any('phi-3.5-mini-128k-instruct' in model.get('id', '') for model in models_data.get('data', []))
            else:
                phi_available = False
                
        except Exception:
            api_available = False
            phi_available = False
        
        return {
            'api_available': api_available,
            'phi3_available': phi_available,
            'provider': 'OpenRouter (Phi-3.5 Mini 128K Instruct)'
        }

# Global instance
ai_assistant = AIAssistant()
