
from flask import Flask, request, jsonify
import os
from text_extraction import extract_text

app = Flask(__name__)

UPLOAD_FOLDER = 'uploads'
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

@app.route('/upload', methods=['POST'])
def upload_file():
    if 'file' not in request.files:
        return jsonify({'error': 'No file part'}), 400
    file = request.files['file']
    if file.filename == '':
        return jsonify({'error': 'No selected file'}), 400
    if file:
        filepath = os.path.join(UPLOAD_FOLDER, file.filename)
        file.save(filepath)
        text = extract_text(filepath)
        return jsonify({'text': text})

@app.route('/delete', methods=['DELETE'])
def delete_files():
    for filename in os.listdir(UPLOAD_FOLDER):
        file_path = os.path.join(UPLOAD_FOLDER, filename)
        os.remove(file_path)
    return jsonify({'message': 'Files deleted'})

if __name__ == '__main__':
    app.run(debug=True)
