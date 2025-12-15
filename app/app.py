import sys
import os

# Add project root to PYTHONPATH
ROOT_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
sys.path.append(ROOT_DIR)

from flask import Flask, request, jsonify
from src.predict import predict_medicine

app = Flask(__name__)

# ✅ ROOT ROUTE (FIXES 404 ISSUE)
@app.route("/", methods=["GET"])
def home():
    return jsonify({
        "message": "MedCare MLOps API is running successfully",
        "available_endpoints": {
            "health_check": "/health",
            "prediction": "/predict (POST)"
        }
    })

@app.route("/health", methods=["GET"])
def health():
    return jsonify({
        "status": "UP",
        "version": "v2-cd-test",
        "message": "GitHub → Azure auto-deploy working 🚀"
    }), 200


@app.route("/predict", methods=["POST"])
def predict():
    data = request.get_json()

    if not data or "disease" not in data:
        return jsonify({"error": "Please provide disease name"}), 400

    result = predict_medicine(data["disease"])
    return jsonify(result), 200

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
