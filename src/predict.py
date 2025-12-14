import joblib
import os

# Load model and encoders
MODEL_PATH = os.path.join("src", "models")

model = joblib.load(os.path.join(MODEL_PATH, "medicine_model.pkl"))
disease_encoder = joblib.load(os.path.join(MODEL_PATH, "disease_encoder.pkl"))
medicine_encoder = joblib.load(os.path.join(MODEL_PATH, "medicine_encoder.pkl"))

# Dosage mapping (simple lookup for now)
DOSAGE_MAP = {
    "Paracetamol": "2 times a day",
    "Cetirizine": "1 time a day",
    "Ambroxol": "2 times a day",
    "Ibuprofen": "1 time a day",
    "Dicycloverine": "2 times a day"
}

def predict_medicine(disease_name: str):
    try:
        disease_encoded = disease_encoder.transform([disease_name])
    except ValueError:
        return {
            "error": "Disease not found in training data"
        }

    medicine_encoded = model.predict([[disease_encoded[0]]])
    medicine = medicine_encoder.inverse_transform(medicine_encoded)[0]

    dosage = DOSAGE_MAP.get(medicine, "Consult a doctor")

    return {
        "disease": disease_name,
        "medicine": medicine,
        "dosage": dosage
    }
