import matplotlib.pyplot as plt
import pandas as pd
from pathlib import Path

project_folder = Path(__file__).resolve().parent.parent

# Load cleaned orders
df = pd.read_csv(
    project_folder / "data" / "cleaned_orders.csv"
)

# Convert delivery dates
df["order_delivered_customer_date"] = pd.to_datetime(
    df["order_delivered_customer_date"]
)

df["order_estimated_delivery_date"] = pd.to_datetime(
    df["order_estimated_delivery_date"]
)

# Select delivered orders with valid dates
delivered = df[
    (df["order_status"] == "delivered")
    & df["order_delivered_customer_date"].notna()
    & df["order_estimated_delivery_date"].notna()
].copy()

# Compare calendar delivery dates
delivered["is_late"] = (
    delivered["order_delivered_customer_date"].dt.normalize()
    > delivered["order_estimated_delivery_date"].dt.normalize()
)

total_delivered = len(delivered)
late_orders = delivered["is_late"].sum()

late_percentage = (late_orders / total_delivered) * 100

print("\n--- DELIVERY PERFORMANCE ---")
print("Delivered orders analyzed:", total_delivered)
print("Late deliveries:", late_orders)
print(f"Late delivery percentage: {late_percentage:.2f}%")

# Calculate on-time deliveries
on_time_orders = total_delivered - late_orders

# Create pie chart
plt.figure(figsize=(8, 8))

plt.pie(
    [on_time_orders, late_orders],
    labels=["On Time / Early", "Late"],
    autopct="%1.2f%%",
    startangle=90,
    colors=["#22c55e", "#ef4444"]
)

plt.title("E-Commerce Delivery Performance")

# Save chart
chart_path = (
    project_folder / "reports" /
    "delivery_performance.png"
)

plt.savefig(chart_path, dpi=300, bbox_inches="tight")

print("\nDelivery performance chart saved!")

plt.show()
