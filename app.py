from flask import Flask, request, jsonify,session
import pandas as pd
import os
from utils import ModelTrainer

app = Flask(__name__)

# Random secret key
app.secret_key = 'intern123'

# Path to save the uploaded dataset
UPLOAD_FOLDER = 'data/'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

# Upload only csv file 
ALLOWED_EXTENSIONS = {'csv'}

# Initialize ModelTrainer object globally
model_trainer = ModelTrainer()

# Function to check if filename is csv
def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS


# Simple for index
@app.route('/')
def home():
    return "Hello World"


# Upload Endpoint
@app.route('/upload', methods=["POST"])
def upload_csv_file():
    if 'file' not in request.files:
        return jsonify({"Error": "No file provided"}), 400
    
    file = request.files['file']

    if file.filename == '':
        return jsonify({"Error": "No selected file"}), 400
    
    if file and allowed_file(file.filename):
        file_path = os.path.join(app.config['UPLOAD_FOLDER'], file.filename)
        # File may be big
        file.save(file_path)
        session['filename'] = file.filename
        return jsonify({"Message": "Uploaded Successful and File Saved"})


# Train Endpoint
@app.route('/train', methods=["POST"])
def train_model():
    filename = session.get('filename', None)
    if filename:
        file_path = os.path.join(app.config['UPLOAD_FOLDER'], filename)
        try:
            data = pd.read_csv(file_path)
            train_message = model_trainer.train(data)  # Train using the ModelTrainer
            return jsonify(train_message)
        except Exception as e:
            return jsonify({"Error": "Failed to process CSV file", "message": str(e)}), 500
    else:
        return jsonify({"Error": "File is not available in requested path"}), 500


# Predict Endpoint
@app.route('/predict', methods=["POST"])
def test_model():
    input_data = request.get_json()

    # Extract features
    machine_id = input_data.get('Machine_ID')
    coolant_temperature = input_data.get('Coolant_Temperature')
    cutting_kn = input_data.get('Cutting(kN)')

    if machine_id is None or coolant_temperature is None or cutting_kn is None:
        return jsonify({"Error": "Missing required fields"}), 400

    # Prepare features for prediction
    feature_columns = ['Machine_ID', 'Coolant_Temperature', 'Cutting(kN)']
    features = pd.DataFrame([[machine_id, coolant_temperature, cutting_kn]],columns=feature_columns)

    try:
        # features = features[0].reshape(-1,1)
        prediction = model_trainer.predict(features)
        pred_val = prediction[0]
        downtime = "Yes" if pred_val == 1 else "No"
        confidence = model_trainer.gbc.predict_proba(features)[0][pred_val]
        confidence = round(confidence,4)
        return jsonify({"Downtime":downtime, "Confidence": confidence})
    except ValueError as e:
        return jsonify({"Error": str(e)}), 400

if __name__ == '__main__':
    os.makedirs(UPLOAD_FOLDER, exist_ok=True)
    app.run(debug=True)