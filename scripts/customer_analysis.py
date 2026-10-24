
import pandas as pd
import matplotlib.pyplot as plt
from pathlib import Path

# Locate project folder
project_folder = Path(__file__).resolve().parent.parent

# Load datasets
orders = pd.read_csv(
    project_folder / "data" / "cleaned_orders.csv"
)

customers = pd.read_csv(
    project_folder / "data" / "olist_customers_dataset.csv"
)

# Combine orders with customer information
merged_data = pd.merge(
    orders,
    customers,
    on="customer_id",
    how="inner",
    validate="many_to_one"
)

print("--- MERGED DATASET ---")
print("Total orders after merging:", len(merged_data))

# Count orders by customer state
state_orders = (
    merged_data["customer_state"]
    .value_counts()
    .head(10)
)

print("\n--- TOP 10 STATES BY ORDERS ---")
print(state_orders)

# Create horizontal bar chart
plt.figure(figsize=(10, 6))

state_orders.sort_values().plot(
    kind="barh",
    color="steelblue"
)

plt.title("Top 10 Brazilian States by Order Count")
plt.xlabel("Number of Orders")
plt.ylabel("Customer State")
plt.tight_layout()

# Save chart
chart_path = (
    project_folder / "reports" /
    "top_10_states.png"
)

plt.savefig(chart_path, dpi=300, bbox_inches="tight")

print("\nCustomer analysis chart saved!")

plt.show()
