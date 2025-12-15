import sys
import os
from datetime import datetime

# Add project root to PYTHONPATH
ROOT_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
sys.path.append(ROOT_DIR)

from flask import Flask, request, jsonify
from src.predict import predict_medicine

app = Flask(__name__)

APP_VERSION = "v3"
DEPLOYED_AT = datetime.utcnow().isoformat()

@app.route("/", methods=["GET"])
def home():
    return jsonify({
        "service": "MedCare MLOps API",
        "version": APP_VERSION,
        "deployed_at": DEPLOYED_AT,
        "endpoints": {
            "health": "/health",
            "predict": "/predict (POST)"
        }
    })

@app.route("/health", methods=["GET"])
def health():
    return jsonify({
        "status": "UP",
        "version": APP_VERSION,
        "deployed_at": DEPLOYED_AT
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
