import pandas as pd
import os
import sys

# Take input file path from command-line argument
if len(sys.argv) < 2:
    print("❌ No input file provided.")
    sys.exit(1)

input_file = sys.argv[1]
output_file = os.path.join("output_files", "output.csv")

# Load CSV file (auto-detect separator), handle special encoding
df = pd.read_csv(input_file, sep=None, engine="python", encoding='Latin1')

# Clean column names
df.columns = df.columns.str.strip()

# Print column names
print("Column names:", df.columns)

# Add extra columns
df['_website'] = 'brothers'
df['group_id'] = '6'

# Rename columns (ensure that 'Förnamn' is exactly correct)
df = df.rename(columns={
    'ï»¿FÃ¶rnamn': 'firstname',
    'Efternamn': 'lastname',
    'E-post': 'email'
})

# Save output CSV
df.to_csv(output_file, sep=';', index=False, encoding='Latin1')

print("✅ CSV processed and saved", output_file)
