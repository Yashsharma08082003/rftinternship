import pandas as pd

# Create data
data = {
    "PRODUCT": ["A", "B", "A", "C"],
    "QUANTITY": [2, 1, 3, 5],
    "PRICE": [100, 200, 100, 50]
}

# Convert into DataFrame
df = pd.DataFrame(data)

# Save data into CSV file
df.to_csv("sales.csv", index=False)

print("CSV file created successfully!")

# Read CSV file
df = pd.read_csv("sales.csv")

# Add TOTAL column
df["TOTAL"] = df["QUANTITY"] * df["PRICE"]

# Calculate sales per product
sales_per_product = df.groupby("PRODUCT")["TOTAL"].sum()

# Total revenue
total_revenue = df["TOTAL"].sum()

# Top-selling product
top_selling_product = sales_per_product.idxmax()

# Sort by revenue
sorted_data = df.sort_values(by="TOTAL", ascending=False)

# Output
print("\nSales Per Product:")
print(sales_per_product)

print("\nTotal Revenue:", total_revenue)

print("\nTop Selling Product:", top_selling_product)

print("\nSorted Data by Revenue:")
print(sorted_data)