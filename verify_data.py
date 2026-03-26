import pandas as pd

# Load the cleaned dataset
df = pd.read_csv('train_cleaned.csv')

# Verification
print("--- Cleaning Verification ---")
print(f"Duplicates: {df.duplicated().sum()}")
print(f"Null Values:\n{df.isnull().sum()}")
print("\n--- Column Data Types ---")
print(df.dtypes)
print("\n--- Date Sample ---")
print(df[['Order Date', 'Ship Date']].head())
