import pandas as pd

# Load the dataset
df = pd.read_csv('train.csv')

# 1. Remove duplicates
df.drop_duplicates(inplace=True)

# 2. Handle missing values (Postal Code is often null in this dataset)
df['Postal Code'] = df['Postal Code'].fillna(0).astype(int)

# 3. Correct formatting issues (Dates)
df['Order Date'] = pd.to_datetime(df['Order Date'], dayfirst=True)
df['Ship Date'] = pd.to_datetime(df['Ship Date'], dayfirst=True)

# Save the cleaned dataset
df.to_csv('train_cleaned.csv', index=False)

print("Data cleaning complete. Saved to train_cleaned.csv")
print(f"Total rows: {len(df)}")
print(f"Null values remaining:\n{df.isnull().sum().sum()}")
