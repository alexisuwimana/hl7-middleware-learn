# file: patient_info.py
def capture_patient():
    name = input("Patient Name: ")
    dob = input("Date of Birth (YYYY-MM-DD): ")
    gender = input("Gender (M/F): ")
    with open("patient.txt", "w") as f:
        f.write(f"Name: {name}\nDOB: {dob}\nGender: {gender}")
    print("Patient info saved!")


capture_patient()
