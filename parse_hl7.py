hl7_message = """MSH|^~\\&|LIS|LabDept|HMIS|Hospital|202505161200||ORU^R01|MSG00001|P|2.3
PID|1||123456^^^Hospital^MR||Doe^John||19800101|M|||
OBR|1||OBR123||CBC^Complete Blood Count|||202505160900|||||||||123456^Doctor^Alice
OBX|1|NM|WBC^White Blood Cells||5.6|10^9/L|4.0-10.0|N|||F
OBX|2|NM|HGB^Hemoglobin||14.2|g/dL|13.0-17.0|N|||F"""

# Split message into segments
segments = hl7_message.strip().split('\n')

for segment in segments:
    fields = segment.split('|')
    if fields[0] == 'PID':
        print("Patient ID:", fields[3])
        print("Patient Name:", fields[5].replace("^", " "))
    elif fields[0] == 'OBR':
        print("\nTest Ordered:", fields[4])
    elif fields[0] == 'OBX':
        test_name = fields[3].split('^')[1]
        result = fields[5]
        unit = fields[6]
        reference = fields[7]
        print(f"Result: {test_name} = {result} {unit} (Ref: {reference})")
