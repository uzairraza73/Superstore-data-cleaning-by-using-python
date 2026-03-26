import pandas as pd

# Load the dataset
df = pd.read_csv('train.csv')

# Basic Info
print("--- Missing Values ---")
print(df.isnull().sum())

print("\n--- Duplicates ---")
print(df.duplicated().sum())

print("\n--- Data Types ---")
print(df.dtypes)

print("\n--- Postal Code Null Check ---")
print(df[df['Postal Code'].isnull()])
