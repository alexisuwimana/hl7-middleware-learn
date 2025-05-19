from flask import Flask, render_template, request
import os
import json

app = Flask(__name__)
# LOG_DIR = '../week5/logs'
LOG_DIR = os.path.join(os.path.dirname(__file__), '..', 'week_5', 'logs')


def load_parsed_results():
    results = []
    for file in os.listdir(LOG_DIR):
        if file.startswith('parsed_') and file.endswith('.json'):
            with open(os.path.join(LOG_DIR, file)) as f:
                data = json.load(f)
                data['timestamp'] = file.replace(
                    'parsed_', '').replace('.json', '')
                results.append(data)
    return results


def filter_results(results, query):
    if not query:
        return results
    query = query.lower()
    filtered = []
    for r in results:
        if query in r['patient']['name'].lower() or \
           query in r['patient']['id'].lower() or \
           any(query in test['test'].lower() for test in r['results']):
            filtered.append(r)
    return filtered


@app.route('/')
def index():
    q = request.args.get('q', '').strip()
    results = load_parsed_results()
    filtered = filter_results(results, q)
    return render_template('index.html', messages=filtered, query=q)


if __name__ == '__main__':
    app.run(debug=True)
