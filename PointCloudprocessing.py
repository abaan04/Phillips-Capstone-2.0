import pandas as pd
import os

# Load the data into a DataFrame from the specified file path
file_path = r"C:\Users\Abaan2\OneDrive - UW\Documents\Capstone\UW - Philips\LJ-X Scans\LJ-X8080.csv"
df = pd.read_csv(file_path)

# Define the range condition for rows and columns
def all_in_range(series):
    return series.astype(float).between(-10001, -9999).all()

# Remove entire rows where all values fall in the range
df = df.loc[~df.apply(all_in_range, axis=1)]

# Remove entire columns where all values fall in the range
df = df.loc[:, ~df.apply(all_in_range, axis=0)]

# Replace individual cell values in the range with NaN
df = df.applymap(lambda x: None if isinstance(x, (int, float)) and -10001 <= x <= -9999 else x)

# Define the output path (same directory as input)
output_path = os.path.join(os.path.dirname(file_path), "cleaned_LJ-X8080.csv")

# Save the cleaned file
df.to_csv(output_path, index=False)

# Print the cleaned file path
print(f"Cleaned file saved at: {output_path}")
