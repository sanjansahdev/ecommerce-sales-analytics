
import pandas as pd
import matplotlib.pyplot as plt
from pathlib import Path

# Locate the main project folder
project_folder = Path(__file__).resolve().parent.parent

# Load datasets
order_items = pd.read_csv(
    project_folder / "data" / "olist_order_items_dataset.csv"
)

products = pd.read_csv(
    project_folder / "data" / "olist_products_dataset.csv"
)

translations = pd.read_csv(
    project_folder / "data" / "product_category_name_translation.csv"
)

# Join order items with product information
merged_data = pd.merge(
    order_items,
    products,
    on="product_id",
    how="left",
    validate="many_to_one"
)

# Join category translations
merged_data = pd.merge(
    merged_data,
    translations,
    on="product_category_name",
    how="left",
    validate="many_to_one"
)

# Count items sold by category
top_categories = (
    merged_data["product_category_name_english"]
    .fillna("Unknown")
    .value_counts()
    .head(10)
)

print("\n--- TOP 10 PRODUCT CATEGORIES ---")
print(top_categories)

# Create horizontal bar chart
plt.figure(figsize=(11, 6))

top_categories.sort_values().plot(
    kind="barh",
    color="teal"
)

plt.title("Top 10 Product Categories by Items Sold")
plt.xlabel("Number of Items Sold")
plt.ylabel("Product Category")
plt.tight_layout()

# Save the chart
chart_path = (
    project_folder / "reports" /
    "top_product_categories.png"
)

plt.savefig(chart_path, dpi=300, bbox_inches="tight")

print("\nProduct category chart saved successfully!")

plt.show()
