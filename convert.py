import pandas as pd
import os

# Get the folder where the script is located
script_dir = os.path.dirname(os.path.abspath(__file__))

# Look for the first CSV file in the script's directory
input_file = None
for file in os.listdir(script_dir):
    if file.endswith(".csv"):
        input_file = os.path.join(script_dir, file)
        break

if not input_file:
    print("❌ No CSV input file found in the script folder.")
    exit(1)

# Output file in the same directory
output_file = os.path.join(script_dir, "output.csv")

# Load CSV file (auto-detect separator), handle special encoding
df = pd.read_csv(input_file, sep=None, engine="python", encoding='Latin1')

# Clean column names
df.columns = df.columns.str.strip()

# Print column names
print("Column names:", df.columns)

# Add extra columns
df['_website'] = 'brothers'
df['group_id'] = '6'

# Rename columns (ensure names match the source)
df = df.rename(columns={
    'ï»¿FÃ¶rnamn': 'firstname',
    'Efternamn': 'lastname',
    'E-post': 'email'
})

# Save output CSV
df.to_csv(output_file, sep=';', index=False, encoding='Latin1')

print("✅ CSV processed and saved to:", output_file)
