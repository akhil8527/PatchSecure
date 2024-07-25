from flask import Flask, request, jsonify, render_template
import main
import os
import json
from datetime import datetime

app = Flask(__name__)

JSON_FOLDER = rf"{os.environ['USERPROFILE']}\OneDrive - Deloitte (O365D)\Gen AI\Patch Management v1\Reports"

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/Report')
def report():
    return render_template('report.html')

@app.route('/NewScan')
def newScan():
    return render_template('newScan.html')

@app.route('/process', methods=['POST'])
def process():
    results = main.main()
    return jsonify(results)

@app.route('/sidebar-info', methods=['GET'])
def sidebar_info():
    # Generate the sidebar information
    sidebar_data = {
        "host": "example.com",
        "start_time": "2024-05-24T10:00:00Z",
        "end_time": "2024-05-24T18:00:00Z"
    }

    return jsonify(sidebar_data)

@app.route('/api/json-files', methods=['GET'])
def list_json_files():
    files = []
    for filename in os.listdir(JSON_FOLDER):
        if filename.endswith('.json'):
            file_path = os.path.join(JSON_FOLDER, filename)
            last_modified_time = datetime.fromtimestamp(os.path.getmtime(file_path)).strftime('%d %b %Y %H:%M %Z')
            files.append({
                'name': os.path.splitext(filename)[0],  # Remove file extension
                'last_modified': last_modified_time,
                'timestamp': os.path.getmtime(file_path)  # Store the timestamp for sorting
            })
    
    # Sort files by the timestamp in descending order
    files.sort(key=lambda x: x['timestamp'], reverse=True)
    
    # Remove the timestamp before sending the response
    for file in files:
        del file['timestamp']
    
    return jsonify(files)

@app.route('/api/json-files/<filename>', methods=['GET'])
def get_json_file(filename):
    file_path = os.path.join(JSON_FOLDER, filename + '.json')
    if os.path.exists(file_path):
        with open(file_path, 'r') as file:
            data = json.load(file)
        return jsonify(data)
    else:
        return jsonify({"error": "File not found"}), 404
    
if __name__ == '__main__':
    app.run(debug=True)
