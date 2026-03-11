Fraud Detection API

A **Fraud Detection API** built with Python, FastAPI, and scikit-learn.  
Send transactions via HTTP POST and get fraud predictions instantly.

## Features
- REST API for fraud detection
- Random Forest classifier trained on transaction data
- Returns `0 = Normal` or `1 = Fraud`
- Modular structure with `utils` and `models`

## Project Structure

fraud-detection-api
├── data/transactions.csv
├── utils/
│ ├── init.py
│ └── preprocess.py
├── models/
│ ├── model.py
│ └── trained_model.pkl
├── main.py
├── requirements.txt
└── README.md


## Installation

```bash
git clone https://github.com/yourusername/fraud-detection-api.git
cd fraud-detection-api
python -m venv .venv
# Activate environment
# Windows
.\.venv\Scripts\activate
# macOS/Linux
source .venv/bin/activate
pip install -r requirements.txt
Train Model
python
>>> import pandas as pd
>>> from models.model import train_and_save_model
>>> df = pd.read_csv("data/transactions.csv")
>>> train_and_save_model(df)
Run API
uvicorn main:app --reload

Open browser at http://127.0.0.1:8000

GET / → test API

POST /predict → send JSON transaction:

{
  "amount": 500,
  "time": 3,
  "merchant": "Target",
  "location": "TX"
}

Response:

{
  "prediction": 1,
  "label": "Fraud"
}