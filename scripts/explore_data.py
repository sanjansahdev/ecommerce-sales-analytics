
import pandas as pd
from pathlib import Path

# Find the main project folder
project_folder = Path(__file__).resolve().parent.parent

# Locate our dataset
file_path = project_folder / "data" / "olist_orders_dataset.csv"

# Load the dataset
df = pd.read_csv(file_path)

# Show the first 5 rows
print("\n--- FIRST 5 ROWS ---")
print(df.head().to_string())

# Find the total number of rows and columns
print("\n--- DATASET SIZE ---")
print("Total rows:", df.shape[0])
print("Total columns:", df.shape[1])

# Display column names
print("\n--- COLUMN NAMES ---")
print(df.columns.tolist())

# Check missing values
print("\n--- MISSING VALUES ---")
print(df.isnull().sum())

# Count orders by status
print("\n--- ORDER STATUS ---")
print(df["order_status"].value_counts())
