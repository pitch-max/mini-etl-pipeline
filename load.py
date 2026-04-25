import os
import pandas as pd
from google.cloud import bigquery

# ✅ FORCE credentials (IMPORTANT FIX)
os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = r"C:\Users\chand\mini-etl-pipeline\service-account.json"

# Load CSV
df = pd.read_csv("sales_data.csv")

# Transform (cleaning)
df["amount"] = df["amount"].fillna(0)
df["city"] = df["city"].fillna("Unknown")

# BigQuery client
client = bigquery.Client()

# Table path
table_id = "mini-etl-project-493720.etl_dataset.sales_table"

print("Uploading data to BigQuery...")

# Load data
job = client.load_table_from_dataframe(df, table_id)
job.result()

print("Data loaded successfully!")