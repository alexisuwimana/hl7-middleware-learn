from config import db
from models import HL7Message, LabResult
from main import app  # make sure you're importing from the file that creates the app

with app.app_context():
    # Create a sample HL7 message
    message = HL7Message(
        patient_id="P123",
        first_name="Alice",
        last_name="Smith"
    )
    db.session.add(message)
    db.session.commit()

    # Create a related lab result
    result = LabResult(
        message_id=message.id,
        test_code="HGB",
        test_name="Hemoglobin",
        value="13.2",
        unit="g/dL",
        reference_range="12.0-16.0",
        flag="N"
    )
    db.session.add(result)
    db.session.commit()

    print("✅ Sample data added.")
