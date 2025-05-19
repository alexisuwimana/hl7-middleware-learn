from config import db


class HL7Message(db.Model):
    __tablename__ = 'hl7_message'  # ✅ explicitly define table name

    id = db.Column(db.Integer, primary_key=True)
    patient_id = db.Column(db.String(20))
    first_name = db.Column(db.String(50))
    last_name = db.Column(db.String(50))
    lab_results = db.relationship('LabResult', backref='message', lazy=True)


class LabResult(db.Model):
    __tablename__ = 'lab_result'  # ✅ explicitly define table name

    id = db.Column(db.Integer, primary_key=True)
    message_id = db.Column(db.Integer, db.ForeignKey(
        'hl7_message.id'), nullable=False)  # ✅ matches __tablename__
    test_code = db.Column(db.String(20))
    test_name = db.Column(db.String(50))
    value = db.Column(db.String(20))
    unit = db.Column(db.String(20))
    reference_range = db.Column(db.String(50))
    flag = db.Column(db.String(10))
