from config import app, db
import models

with app.app_context():
    db.create_all()
    print("✅ Database created.")
