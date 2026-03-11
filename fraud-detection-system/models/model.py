import pickle
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
import pandas as pd


def train_and_save_model(df, model_path="models/trained_model.pkl"):

    df = df.dropna()

    # Convert text columns to numbers
    df = pd.get_dummies(df, columns=["merchant", "location"])

    # Split features and label
    X = df.drop("fraud", axis=1)
    y = df["fraud"]

    # Scale numerical data
    scaler = StandardScaler()
    X_scaled = scaler.fit_transform(X)

    # Train/test split
    X_train, X_test, y_train, y_test = train_test_split(
        X_scaled, y, test_size=0.2, random_state=42
    )

    # Train model
    model = RandomForestClassifier(n_estimators=100)
    model.fit(X_train, y_train)

    # Save model and scaler
    with open(model_path, "wb") as f:
        pickle.dump({"model": model, "scaler": scaler, "columns": X.columns}, f)

    print("Model trained and saved successfully.")