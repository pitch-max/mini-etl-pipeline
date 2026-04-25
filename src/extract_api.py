import requests
import pandas as pd

# API URL
url = "https://jsonplaceholder.typicode.com/users"

# API Call
response = requests.get(url)

# Convert JSON
data = response.json()

# Convert to DataFrame
df = pd.DataFrame(data)

# Print sample
print("API DATA:")
print(df.head())

# Save raw data
df.to_csv("data/raw_api_data.csv", index=False)

print("Raw API data saved successfully!")