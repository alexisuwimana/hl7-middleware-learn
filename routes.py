from flask import jsonify
from config import app
from models import HL7Message


@app.route('/api/lab-results')
def get_lab_results():
    results = HL7Message.query.all()
    return jsonify([{
        'id': msg.id,
        'patient_id': msg.patient_id,
        'first_name': msg.first_name,
        'last_name': msg.last_name
    } for msg in results])
