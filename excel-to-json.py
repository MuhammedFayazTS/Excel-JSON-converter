import json
import pandas as pd

# Load data from Excel file
df = pd.read_excel("excel-data.xlsx")

# Convert DataFrame to dictionary
# Ensure the first column is Keys and second is English Words
json_data = dict(zip(df["Keys"], df["English Words"]))

# Save dictionary to a JSON file
with open("json_data.json", "w", encoding="utf-8") as f:
    json.dump(json_data, f, ensure_ascii=False, indent=4)

print("JSON file 'json_data.json' has been created successfully.")
