import socket


def start_server():
    HOST = 'localhost'
    PORT = 5000

    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.bind((HOST, PORT))
        s.listen()
        print(f"🟢 Middleware Listening on {HOST}:{PORT}")

        conn, addr = s.accept()
        with conn:
            print(f"🔌 Connection from {addr}")
            data = conn.recv(4096).decode()

            print("\n📥 Received HL7 Message:")
            print(data)

            # Simple parsing
            lines = data.strip().split('\n')
            for line in lines:
                parts = line.split('|')
                if parts[0] == "PID":
                    print("👤 Patient ID:", parts[3])
                    print("👤 Name:", parts[5].replace('^', ' '))
                elif parts[0] == "OBX":
                    test = parts[3].split('^')[1]
                    result = parts[5]
                    unit = parts[6]
                    print(f"🧪 {test}: {result} {unit}")


if __name__ == '__main__':
    start_server()
