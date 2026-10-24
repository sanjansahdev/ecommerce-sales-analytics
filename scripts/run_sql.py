
import duckdb
from pathlib import Path

project_folder = Path(__file__).resolve().parent.parent

csv_path = project_folder / "data" / "cleaned_orders.csv"
sql_path = project_folder / "sql" / "kpi_analysis.sql"

# Create a DuckDB connection
con = duckdb.connect()

# Load the CSV as a table
con.read_csv(str(csv_path)).create_view("orders")
# Load purchased items as another SQL view
items_path = project_folder / "data" / "olist_order_items_dataset.csv"

con.read_csv(str(items_path)).create_view("order_items")

# Read SQL queries
sql_text = sql_path.read_text(encoding="utf-8")

# Execute each query
for number, query in enumerate(sql_text.split(";"), start=1):
    if not query.strip():
        continue

    print(f"\n--- SQL QUERY {number} ---")

    result = con.execute(query).df()
    print(result.to_string(index=False))

con.close()
