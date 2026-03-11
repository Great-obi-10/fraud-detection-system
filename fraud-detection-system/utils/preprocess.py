import pandas as pd
from sklearn.preprocessing import StandardScaler

def preprocess_input(df, scaler=None):
    """
    Preprocess input dataframe for prediction.
    If scaler is provided, use it to transform features.
    """
    X = df.copy()
    
    if "fraud" in X.columns:
        X = X.drop("fraud", axis=1)
    
    if scaler:
        X_scaled = scaler.transform(X)
    else:
        X_scaled = X.values  # fallback
    
    return X_scaled