import sys
import os
from flask import Flask, request, jsonify
from src.predict import predict_medicine

# 🔥 CHANGE VERSION HERE EACH TEST
APP_VERSION = "v3"

app = Flask(__name__)

@app.route("/", methods=["GET"])
def home():
    return jsonify({
        "service": "MedCare MLOps API",
        "status": "RUNNING",
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
        "version": APP_VERSION
    })

@app.route("/predict", methods=["POST"])
def predict():
    data = request.get_json()
    if not data or "disease" not in data:
        return jsonify({"error": "Please provide disease name"}), 400

    result = predict_medicine(data["disease"])
    result["version"] = APP_VERSION
    return jsonify(result), 200

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
