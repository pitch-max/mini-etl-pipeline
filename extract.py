import pandas as pd

# STEP 1: Extract data (read CSV)
df = pd.read_csv("sales_data.csv")

# STEP 2: Show data
print("RAW DATA FROM CSV:")
print(df)