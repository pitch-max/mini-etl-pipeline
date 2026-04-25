import pandas as pd
from google.cloud import bigquery

df = pd.read_csv("data/clean_api_data.csv")

print("Uploading data to BigQuery...")

PROJECT_ID = "mini-api-etl-project-494420"

client = bigquery.Client(project=PROJECT_ID)

table_id = f"mini-api-etl-project-494420.api_pipeline.users_cleaned"

job_config = bigquery.LoadJobConfig(
    write_disposition="WRITE_TRUNCATE"
)

job = client.load_table_from_dataframe(
    df,
    table_id,
    job_config=job_config
)

job.result()

print("Data loaded successfully!")