from flask import Flask, request, jsonify

app = Flask(__name__)


@app.route('/api/lab-result', methods=['POST'])
def receive_lab_result():
    data = request.get_json()
    print("✅ Received HL7 JSON at HMIS:")
    print(data)
    return jsonify({"status": "received", "message": "Data processed"}), 200


if __name__ == '__main__':
    app.run(port=5001)
