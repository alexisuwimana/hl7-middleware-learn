import os
import sys
from middleware import parse_hl7  # ✅ Now this will work!
from storage import save_message, save_parsed_data
import threading
import socket
# ✅ Must come BEFORE importing anything from week_4
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))


def handle_client(conn, addr):
    print(f"🔌 New Connection from {addr}")
    data = conn.recv(4096).decode()
    print("📥 HL7 Message Received:\n", data)

    parsed = parse_hl7(data)

    # Save original and parsed
    save_message(data)
    save_parsed_data(parsed)

    conn.close()


def start_server():
    HOST = 'localhost'
    PORT = 6000
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind((HOST, PORT))
    server.listen(5)
    print(f"🟢 Middleware running on {HOST}:{PORT}")

    while True:
        conn, addr = server.accept()
        thread = threading.Thread(target=handle_client, args=(conn, addr))
        thread.start()
        print(f"🧵 Active Connections: {threading.active_count() - 1}")


if __name__ == "__main__":
    start_server()
