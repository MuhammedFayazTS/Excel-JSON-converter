import json
import pandas as pd

# Load JSON data from a file
with open('./json_data.json', 'r', encoding='utf-8') as f:
    json_data = json.load(f)

# Convert JSON to DataFrame
# Add the names of columns needed
df = pd.DataFrame(list(json_data.items()), columns=["Keys", "English Words"])

# Save to Excel
df.to_excel("translated_words.xlsx", index=False)

print("Excel file 'translated_words.xlsx' has been created successfully.")
