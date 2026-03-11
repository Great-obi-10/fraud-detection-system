import pandas as pd
from models.model import train_and_save_model

# Load dataset
df = pd.read_csv("data/transactions.csv")

# Train model
train_and_save_model(df)