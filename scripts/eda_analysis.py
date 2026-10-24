
import pandas as pd
import matplotlib.pyplot as plt
from pathlib import Path

# Locate the project folder
project_folder = Path(__file__).resolve().parent.parent

# Load cleaned orders dataset
file_path = project_folder / "data" / "cleaned_orders.csv"
df = pd.read_csv(file_path)

# Convert purchase timestamp to datetime
df["order_purchase_timestamp"] = pd.to_datetime(
    df["order_purchase_timestamp"]
)

# Create a year-month column
df["order_month"] = (
    df["order_purchase_timestamp"]
    .dt.to_period("M")
)

# Count orders for each month
monthly_orders = (
    df.groupby("order_month")
    .size()
    .sort_index()
)

print("\n--- MONTHLY ORDER COUNTS ---")
print(monthly_orders)

# Plot monthly order trend
plt.figure(figsize=(12, 6))

plt.plot(
    monthly_orders.index.astype(str),
    monthly_orders.values,
    marker="o"
)

plt.title("Monthly E-Commerce Order Trends")
plt.xlabel("Month")
plt.ylabel("Number of Orders")
plt.xticks(rotation=90)
plt.grid(True, alpha=0.3)
plt.tight_layout()

# Display the chart
chart_path = project_folder / "reports" / "monthly_order_trends.png"

plt.savefig(chart_path, dpi=300, bbox_inches="tight")

print("Chart saved successfully!")

plt.show()
