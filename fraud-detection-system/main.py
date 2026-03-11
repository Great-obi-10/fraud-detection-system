from fastapi import FastAPI
from pydantic import BaseModel
import pandas as pd
import pickle
import os
from utils.preprocess import preprocess_input

# Initialize FastAPI app
app = FastAPI(title="Fraud Detection API")

# Define request schema
class Transaction(BaseModel):
    amount: float
    time: int
    merchant: str
    location: str

# Load model and scaler
MODEL_PATH = "models/trained_model.pkl"
if not os.path.exists(MODEL_PATH):
    raise FileNotFoundError("Trained model not found. Run model training first.")

with open(MODEL_PATH, "rb") as f:
    data = pickle.load(f)
    model = data["model"]
    scaler = data["scaler"]

@app.get("/")
def root():
    return {"message": "Fraud Detection API is running."}

@app.post("/predict")
def predict(transaction: Transaction):
    # Convert input to dataframe
    df = pd.DataFrame([transaction.dict()])
    
    # Preprocess
    X = preprocess_input(df, scaler=scaler)
    
    # Predict
    pred = model.predict(X)[0]
    pred_label = "Fraud" if pred == 1 else "Normal"
    
    return {"prediction": int(pred), "label": pred_label}