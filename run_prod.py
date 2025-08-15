#!/usr/bin/env python3
"""
Production server startup script using Gunicorn
"""
import os
import sys

# Add the project root to Python path
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

def create_production_app():
    """Create production app instance"""
    os.environ['FLASK_ENV'] = 'production'
    os.environ['DEBUG'] = 'false'
    
    from app import create_app
    return create_app('production')

# For Gunicorn
app = create_production_app()

if __name__ == "__main__":
    # Start production server directly
    app = create_production_app()
    
    from src.services import vitals_simulator
    vitals_simulator.start_simulation()
    
    port = int(os.environ.get('PORT', 5000))
    print(f"Starting KogniCare Production Server on port {port}...")
    
    app.run(host='0.0.0.0', port=port, debug=False)
