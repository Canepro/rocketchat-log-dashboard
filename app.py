from flask import Flask, jsonify, send_from_directory
from datetime import datetime, timedelta
import random

app = Flask(__name__, static_folder='static', static_url_path='')

@app.get('/api/logs')
def logs():
    now = datetime.utcnow()
    points = []
    for i in range(60):
        t = now - timedelta(minutes=59 - i)
        points.append({
            't': t.isoformat() + 'Z',
            'value': random.randint(0, 50)
        })
    return jsonify(points)

@app.get('/')
def index():
    return send_from_directory('static', 'index.html')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8000)