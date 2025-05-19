import socket
import requests


def parse_hl7(hl7_msg):
    lines = hl7_msg.strip().split('\n')
    patient_info = {}
    tests = []

    for line in lines:
        parts = line.split('|')
        if parts[0] == "PID":
            patient_info["id"] = parts[3]
            patient_info["name"] = parts[5].replace('^', ' ')
        elif parts[0] == "OBX":
            test_name = parts[3].split('^')[1]
            result = parts[5]
            unit = parts[6]
            tests.append({
                "test": test_name,
                "value": result,
                "unit": unit
            })

    return {
        "patient": patient_info,
        "results": tests
    }


def start_server():
    HOST = 'localhost'
    PORT = 5000

    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.bind((HOST, PORT))
        s.listen()
        print(f"🟢 Listening on {HOST}:{PORT}")

        conn, addr = s.accept()
        with conn:
            print(f"🔌 Connected to {addr}")
            data = conn.recv(4096).decode()
            print("📥 HL7 Received:\n", data)

            json_data = parse_hl7(data)

            print("📤 Sending to HMIS...")
            response = requests.post(
                "http://localhost:5001/api/lab-result", json=json_data)
            print("🔁 Response from HMIS:", response.json())


if __name__ == '__main__':
    start_server()
