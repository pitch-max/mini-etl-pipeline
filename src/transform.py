import pandas as pd

# Load raw API data
df = pd.read_csv("data/raw_api_data.csv")

print("BEFORE TRANSFORMATION:")
print(df.head())

# ----------------------------
# FLATTEN NESTED DATA
# ----------------------------

df["city"] = df["address"].apply(lambda x: eval(x)["city"] if pd.notna(x) else None)
df["company_name"] = df["company"].apply(lambda x: eval(x)["name"] if pd.notna(x) else None)

# ----------------------------
# CLEAN DATA
# ----------------------------

df = df[["id", "name", "email", "city", "company_name"]]

df = df.fillna("Unknown")

print("\nAFTER TRANSFORMATION:")
print(df.head())

# Save cleaned data
df.to_csv("data/clean_api_data.csv", index=False)

print("\nClean data saved successfully!")