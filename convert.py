import pandas as pd

# Load Excel file
df = pd.read_excel("Contact_export.xlsx")

# Add extra columns
df['_website'] = 'brothers'
df['group_id'] = '6'

# Save as CSV
df.to_csv("output.csv", index=False)

print("✅ Excel converted to CSV with new columns.")
