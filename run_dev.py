#!/usr/bin/env python3
"""
Development server startup script
"""
import os
import sys

# Add the project root to Python path
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from app import create_app
from src.services import vitals_simulator

if __name__ == "__main__":
    # Set development environment
    os.environ['FLASK_ENV'] = 'development'
    os.environ['DEBUG'] = 'true'
    
    app = create_app('development')
    
    # Start simulation
    vitals_simulator.start_simulation()
    
    print("Starting KogniCare Development Server...")
    print("Dashboard available at: http://localhost:5000")
    print("API endpoints available at: http://localhost:5000/api/")
    
    app.run(host='0.0.0.0', port=5000, debug=True)
