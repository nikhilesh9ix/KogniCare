from flask import Blueprint, render_template
from src.services import vitals_simulator

main_bp = Blueprint('main', __name__)

@main_bp.route('/')
def index():
    """Serve the main dashboard"""
    vitals_simulator.start_simulation()  # Start simulation on first request
    return render_template('index.html')
