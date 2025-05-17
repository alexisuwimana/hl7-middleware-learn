# hl7_message = """MSH|^~\\&|LIS|LabDept|HMIS|Hospital|202505161200||ORU^R01|MSG00001|P|2.3
# PID|1||123457^^^Hospital^MR||Alexis^Uwimana||19800101|M|||
# OBR|1||OBR124||RPR^Rapid Plasma Reagin|||202505160920|||||||||123457^Doctor^Yves
# OBR|2||OBR124||HIV^Human Immunodeficiency Virus|||202505160920|||||||||123457^Doctor^Yves
# OBR|3||OBR124||CRP^C-Reactive Protein|||202505160920|||||||||123457^Doctor^Yves


# OBX|1|NM|RPR^Rapid Plasma Reagin||5.9|10^9/L|5.0-15.0|N|||F
# OBX|2|NM|HIV^Human Immunodeficiency Hirus||10.0|g/dL|15.0-19.0|N|||F
# OBX|2|NM|CRP^C-Reactive Protein||20.0|g/dL|10.0-25.0|N|||F"""

# # Split message into segments
# segments = hl7_message.strip().split('\n')

# for segment in segments:
#     fields = segment.split('|')
#     if fields[0] == 'PID':
#         print("Patient ID:", fields[3])
#         print("Patient Name:", fields[5].replace("^", " "))
#     elif fields[0] == 'OBR':
#         print("\nTest Ordered:", fields[4])
#     elif fields[0] == 'OBX':
#         test_name = fields[3].split('^')[1]
#         result = fields[5]
#         unit = fields[6]
#         reference = fields[7]
#         print(f"Result: {test_name} = {result} {unit} (Ref: {reference})")

with open('sample_message.hl7', 'r') as file:
    hl7_message = file.read()
