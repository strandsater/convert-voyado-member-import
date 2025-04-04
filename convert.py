import pandas as pd

# Load CSV file with UTF-8 encoding
df = pd.read_csv("Contact_export.csv", sep=None, engine="python", encoding='Latin1')

# Strip leading/trailing spaces from column names to avoid mismatches
df.columns = df.columns.str.strip()

# Print column names to check if everything is read correctly
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

# Save as CSV with UTF-8 encoding and ; separator
df.to_csv("output.csv", sep=';', index=False, encoding='Latin1')

print("✅ Columns renamed and saved to CSV with special characters handled.")
