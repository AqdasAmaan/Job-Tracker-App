from flask import Flask, jsonify
from flask_cors import CORS
from db import get_db_connection

app = Flask(__name__)
CORS(app)

@app.route('/')
def home():
    return {'message': 'Job Tracker API running'}

@app.route('/jobs')
def jobs():
    conn = get_db_connection()
    jobs = conn.execute('SELECT * FROM Jobs').fetchall()
    
    conn.close()

    return jsonify([dict(row) for row in jobs])

if __name__ == '__main__':
    app.run(debug=True)