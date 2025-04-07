import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D


# Load the data
file_path = r"C:\Users\Abaan2\OneDrive - UW\Documents\Capstone\UW - Philips\LJ-X Scans\filtered_LJ-X8080_filtered.csv"
df = pd.read_csv(file_path)

# Convert DataFrame to a NumPy array (if needed)
height_matrix = df.to_numpy()

# Plot the heatmap
plt.figure(figsize=(10, 8))
sns.heatmap(height_matrix, cmap="viridis", annot=False)  # 'viridis' is great for elevation
plt.title("Height Map of Scan Data")
plt.xlabel("X Coordinate")
plt.ylabel("Y Coordinate")
plt.show()

import pandas as pd

# Load your filtered data
file_path = r"C:\Users\Abaan2\OneDrive - UW\Documents\Capstone\UW - Philips\LJ-X Scans\cleaned_LJ-X8080.csv"
df = pd.read_csv(file_path, index_col=0)

# Filter columns that have at least 10 non-null (valid) values
valid_columns = df.columns[df.notna().sum() >= 10]

# Get the first column with at least 10 valid data points
first_valid_column = df[valid_columns[0]]

# Print the first column with at least 10 valid data points
print(first_valid_column)
