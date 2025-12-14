import pandas as pd
from sklearn.preprocessing import LabelEncoder
from sklearn.naive_bayes import MultinomialNB
import joblib
import os

# Load dataset
data_path = os.path.join("data", "diseases.csv")
df = pd.read_csv(data_path)

# Encode inputs
disease_encoder = LabelEncoder()
medicine_encoder = LabelEncoder()

df["disease_encoded"] = disease_encoder.fit_transform(df["disease"])
df["medicine_encoded"] = medicine_encoder.fit_transform(df["medicine"])

X = df[["disease_encoded"]]
y = df["medicine_encoded"]

# Train model
model = MultinomialNB()
model.fit(X, y)

# Save model and encoders
os.makedirs("src/models", exist_ok=True)

joblib.dump(model, "src/models/medicine_model.pkl")
joblib.dump(disease_encoder, "src/models/disease_encoder.pkl")
joblib.dump(medicine_encoder, "src/models/medicine_encoder.pkl")

print("✅ Model training completed and files saved.")
