
import pandas as pd
from pathlib import Path

# Find the project folder
project_folder = Path(__file__).resolve().parent.parent

# Load the dataset
file_path = project_folder / "data" / "olist_orders_dataset.csv"

df = pd.read_csv(file_path)

print("--- ORIGINAL DATASET ---")
print("Rows:", len(df))

# Check duplicate orders
duplicates = df["order_id"].duplicated().sum()
print("\nDuplicate Order IDs:", duplicates)

# Check missing values
print("\n--- MISSING VALUES ---")
print(df.isnull().sum())

# Convert date columns
date_columns = [
    "order_purchase_timestamp",
    "order_approved_at",
    "order_delivered_carrier_date",
    "order_delivered_customer_date",
    "order_estimated_delivery_date"
]

for column in date_columns:
    df[column] = pd.to_datetime(
        df[column],
        errors="coerce"
    )

# Remove duplicate Order IDs, if any
df = df.drop_duplicates(subset=["order_id"])

print("\n--- AFTER CLEANING ---")
print("Total rows:", len(df))
print("Duplicate Order IDs:", df["order_id"].duplicated().sum())

# Save cleaned dataset
output_path = project_folder / "data" / "cleaned_orders.csv"

df.to_csv(output_path, index=False)

print("\nCleaned dataset saved successfully!")
