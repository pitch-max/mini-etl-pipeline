import pandas as pd

# Extract
df = pd.read_csv("sales_data.csv")

print("BEFORE CLEANING:")
print(df)

# -------------------------
# TRANSFORM (CLEAN DATA)
# -------------------------

# 1. Fill missing amount with 0
df["amount"] = df["amount"].fillna(0)

# 2. Fill missing city with "Unknown"
df["city"] = df["city"].fillna("Unknown")

# 3. Convert data type
df["amount"] = df["amount"].astype(float)

print("\nAFTER CLEANING:")
print(df)