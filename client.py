import socket

# Load message from file
with open('message.hl7', 'r') as file:
    hl7_message = file.read()

HOST = 'localhost'
PORT = 5000

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((HOST, PORT))
    s.sendall(hl7_message.encode())
    print("📤 HL7 Message Sent.")
