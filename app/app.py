import sys
import os

# Add project root to PYTHONPATH
ROOT_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
sys.path.append(ROOT_DIR)

from flask import Flask, request, jsonify
from src.predict import predict_medicine

app = Flask(__name__)

APP_VERSION = "v3"   # 👈 version marker for auto-deploy verification

@app.route("/", methods=["GET"])
def home():
    return jsonify({
        "message": "MedCare MLOps API running",
        "version": APP_VERSION,
        "endpoints": {
            "health": "/health",
            "predict": "/predict (POST)"
        }
    })

@app.route("/health", methods=["GET"])
def health():
    return jsonify({
        "status": "UP",
        "version": "2.0",
        "message": "MedCare API v2 deployed successfully"
    }), 200


@app.route("/predict", methods=["POST"])
def predict():
    data = request.get_json()
    if not data or "disease" not in data:
        return jsonify({"error": "Please provide disease name"}), 400

    result = predict_medicine(data["disease"])
    return jsonify(result), 200
