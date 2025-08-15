import io
from datetime import datetime
from reportlab.lib.pagesizes import letter
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.units import inch
from reportlab.lib import colors

class ReportGenerator:
    """Handles PDF report generation"""
    
    def __init__(self):
        self.styles = getSampleStyleSheet()
        self.title_style = ParagraphStyle(
            'CustomTitle',
            parent=self.styles['Heading1'],
            fontSize=18,
            spaceAfter=30,
            textColor=colors.HexColor('#0ea5e9')
        )
    
    def generate_patient_report(self, patient_info, current_vitals, alerts_list, get_vital_status_func):
        """Generate a PDF patient report"""
        try:
            # Create a BytesIO buffer
            buffer = io.BytesIO()
            
            # Create the PDF document
            doc = SimpleDocTemplate(buffer, pagesize=letter)
            story = []
            
            # Title
            title = Paragraph("Patient Monitoring Report", self.title_style)
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
            
            story.append(Paragraph("Patient Information", self.styles['Heading2']))
            story.append(patient_table)
            story.append(Spacer(1, 20))
            
            # Current Vitals
            vitals_data = [
                ['Vital Sign', 'Current Value', 'Status'],
                ['Heart Rate', f"{current_vitals['heart_rate']} BPM", get_vital_status_func('heart_rate', current_vitals['heart_rate']).title()],
                ['SpO2', f"{current_vitals['spo2']}%", get_vital_status_func('spo2', current_vitals['spo2']).title()],
                ['Temperature', f"{current_vitals['temperature']}°C", get_vital_status_func('temperature', current_vitals['temperature']).title()],
                ['Respiratory Rate', f"{current_vitals['respiratory_rate']} BPM", get_vital_status_func('respiratory_rate', current_vitals['respiratory_rate']).title()]
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
            
            story.append(Paragraph("Current Vital Signs", self.styles['Heading2']))
            story.append(vitals_table)
            story.append(Spacer(1, 20))
            
            # Recent Alerts
            if alerts_list:
                story.append(Paragraph("Recent Alerts", self.styles['Heading2']))
                for alert in alerts_list[-5:]:  # Last 5 alerts
                    alert_text = f"• {alert['message']} ({alert['timestamp'][:19]})"
                    story.append(Paragraph(alert_text, self.styles['Normal']))
            
            story.append(Spacer(1, 20))
            
            # Footer
            footer_text = f"Report generated on {datetime.now().strftime('%Y-%m-%d %H:%M:%S')} by Kognicare AI Monitoring System"
            story.append(Paragraph(footer_text, self.styles['Normal']))
            
            # Build PDF
            doc.build(story)
            
            # Get the value of the BytesIO buffer
            buffer.seek(0)
            
            return buffer
            
        except Exception as e:
            raise Exception(f"Failed to generate report: {str(e)}")

# Global instance
report_generator = ReportGenerator()
