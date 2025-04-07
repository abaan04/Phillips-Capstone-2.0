import pandas as pd

# Load your filtered CSV data
file_path = r"C:\Users\Abaan2\OneDrive - UW\Documents\Capstone\UW - Philips\LJ-X Scans\cleaned_LJ-X8080.csv"
df = pd.read_csv(file_path, index_col=0)

# Filter columns with at least 10 non-null (valid) values
valid_columns = df.columns[df.notna().sum() >= 10]

# Check if any valid column was found
if not valid_columns.empty:
    first_valid_column = df[valid_columns[0]]
    print(f"First column with at least 10 data points: {valid_columns[0]}")
    print(first_valid_column)
else:
    print("No columns with at least 10 valid data points were found.")

