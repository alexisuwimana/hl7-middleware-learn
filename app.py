from flask import Flask, render_template
import os
import json

app = Flask(__name__)

LOG_DIR = os.path.join(os.path.dirname(__file__), '../week_5/logs')


def load_parsed_results():
    results = []
    if not os.path.exists(LOG_DIR):
        return results  # empty list

    for file in sorted(os.listdir(LOG_DIR)):
        if file.endswith('.json'):
            path = os.path.join(LOG_DIR, file)
            with open(path, 'r') as f:
                try:
                    results.append(json.load(f))
                except json.JSONDecodeError:
                    continue
    return results


@app.route('/')
def index():
    messages = load_parsed_results()
    return render_template('dashboard.html', messages=messages)


if __name__ == '__main__':
    app.run(debug=True, port=5000)
