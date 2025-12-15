import sys
import os

# Add project root to PYTHONPATH
ROOT_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
sys.path.append(ROOT_DIR)

from flask import Flask, request, jsonify
from src.predict import predict_medicine

# ✅ VERSION IDENTIFIER (USED TO VERIFY AUTO DEPLOY)
APP_VERSION = "v2"

app = Flask(__name__)

# ✅ ROOT ROUTE
@app.route("/", methods=["GET"])
def home():
    return jsonify({
        "message": "MedCare MLOps API is running successfully",
        "version": APP_VERSION,
        "available_endpoints": {
            "health_check": "/health",
            "prediction": "/predict (POST)"
        }
    })

# ✅ HEALTH CHECK (THIS IS YOUR DEPLOYMENT PROOF)
@app.route("/health", methods=["GET"])
def health():
    return jsonify({
        "status": "UP",
        "version": APP_VERSION
    }), 200

# ✅ PREDICTION API
@app.route("/predict", methods=["POST"])
def predict():
    data = request.get_json()

    if not data or "disease" not in data:
        return jsonify({"error": "Please provide disease name"}), 400

    result = predict_medicine(data["disease"])
    return jsonify(result), 200

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
