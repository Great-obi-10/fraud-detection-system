Fraud Detection System API

A Machine Learning–powered Fraud Detection API built with FastAPI that predicts whether a financial transaction is fraudulent or legitimate.

This project demonstrates how to build a full ML pipeline, train a model, and deploy it as an API service that can be accessed through HTTP requests.

Project Overview

Financial fraud is a major issue in modern digital payment systems. This project implements a fraud detection model that analyzes transaction features and predicts whether a transaction is fraudulent.

The system:

Loads transaction data

Preprocesses the dataset

Trains a machine learning model

Saves the trained model

Deploys the model as a REST API

Allows predictions via HTTP requests

Technology Stack

This project uses the following technologies:

Python

FastAPI – API framework

Scikit-learn – ML model training

Pandas – Data processing

Uvicorn – API server

Pickle – Model serialization

Project Structure
fraud-detection-system
│
├── data
│   └── transactions.csv         # Dataset
│
├── utils
│   ├── __init__.py
│   └── preprocess.py            # Data preprocessing functions
│
├── models
│   └── model.py                 # Model training functions
│
├── main.py                      # FastAPI application
│
├── train_model.py               # Script to train the ML model
│
├── model.pkl                    # Saved trained model
│
├── requirements.txt             # Project dependencies
│
└── README.md                    # Documentation
How the System Works

The architecture of the system is shown below:

Dataset
   ↓
Preprocessing
   ↓
Train Machine Learning Model
   ↓
Save Model (.pkl)
   ↓
FastAPI Server
   ↓
POST /predict
   ↓
Fraud Prediction

When a user sends a transaction to the API:

The API receives transaction data

The data is preprocessed

The trained model loads

The model predicts fraud probability

The API returns the result

Installation Guide

Clone the repository:

git clone https://github.com/Great-obi-10/fraud-detection-system.git

Navigate to the project folder:

cd fraud-detection-system

Create a virtual environment:

python -m venv .venv

Activate the environment:

Windows

.venv\Scripts\activate

Install dependencies:

pip install -r requirements.txt
Training the Machine Learning Model

Before running the API, you must train the model.

Run:

python train_model.py

If successful, you will see:

Model trained and saved successfully.

This will generate:

model.pkl

This file contains the trained fraud detection model.

Running the API

Start the server using:

uvicorn main:app --reload

You should see something like:

Uvicorn running on http://127.0.0.1:8000
API Documentation

FastAPI automatically generates interactive API documentation using Swagger UI.

Open in your browser:

http://127.0.0.1:8000/docs

This interface allows you to:

Explore API endpoints

Test the API directly

View request and response formats

API Endpoints
GET /

Root endpoint used to verify that the API is running.

Example response:

{
 "message": "Fraud Detection API Running"
}
POST /predict

This endpoint sends transaction data to the model and returns a prediction.

Example Request
{
 "amount": 200,
 "merchant": "Amazon",
 "location": "USA",
 "time": 14
}
Example Response
{
 "prediction": "Fraud"
}

or

{
 "prediction": "Not Fraud"
}
Testing the API

To test your model:

Open

http://127.0.0.1:8000/docs

Expand POST /predict

Click Try it out

Enter example transaction data

Click Execute

The system will return a fraud prediction.

Real-World Applications

Fraud detection APIs like this are used by major financial platforms including:

PayPal

Stripe

Visa

These systems analyze millions of transactions to detect suspicious activities in real time.

Future Improvements

Possible improvements for this project include:

Adding model accuracy evaluation

Using more advanced models like Random Forest or XGBoost

Adding fraud probability scores

Deploying the API to the cloud

Creating a web dashboard for fraud monitoring

Author

Great Obi

CYBERSECURITY ENGINEER | ML/AI ENGINEER
