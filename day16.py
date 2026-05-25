import pandas as pd
import matplotlib.pyplot as plt

# Create Dataset
data = {
    "Date":[
        "2025-01-01","2025-01-02","2025-01-03","2025-01-04","2025-01-05",
        "2025-01-06","2025-01-07","2025-01-08","2025-01-09","2025-01-10",
        "2025-02-01","2025-02-02","2025-02-03","2025-02-04","2025-02-05",
        "2025-02-06","2025-02-07","2025-02-08","2025-02-09","2025-02-10",
        "2025-03-01","2025-03-02","2025-03-03","2025-03-04","2025-03-05",
        "2025-03-06","2025-03-07","2025-03-08","2025-03-09","2025-03-10"
    ],

    "Product":[
        "Laptop","Phone","Tablet","Laptop","Phone",
        "Headphones","Smartwatch","Laptop","Tablet","Phone",
        "Laptop","Smartwatch","Headphones","Tablet","Phone",
        "Laptop","Phone","Headphones","Tablet","Smartwatch",
        "Laptop","Phone","Tablet","Headphones","Smartwatch",
        "Laptop","Phone","Tablet","Headphones","Smartwatch"
    ],

    "Region":[
        "North","South","East","West","North",
        "South","East","North","West","South",
        "East","North","West","South","East",
        "North","West","East","North","South",
        "West","North","East","South","West",
        "North","East","South","North","East"
    ],

    "Sales":[
        15000,12000,8000,16000,14000,
        5000,9000,18000,7000,13500,
        17000,9500,4500,8200,13000,
        19000,14500,6000,7500,10000,
        21000,15000,8500,5500,11000,
        22000,15500,9000,6500,12000
    ]
}

df = pd.DataFrame(data)

# Save CSV file automatically
df.to_csv("sales_data.csv", index=False)
print("CSV file created successfully!")

# Data Cleaning
df["Date"] = pd.to_datetime(df["Date"])

# Total Sales Per Product
product_sales = df.groupby("Product")["Sales"].sum()

print("\nTotal Sales Per Product:")
print(product_sales)

# Region Wise Performance
region_sales = df.groupby("Region")["Sales"].sum()

print("\nRegion Wise Performance:")
print(region_sales)

# Sales Trend
sales_trend = df.groupby("Date")["Sales"].sum()

plt.figure(figsize=(10,5))
plt.plot(sales_trend.index,sales_trend.values)
plt.title("Sales Trend")
plt.xlabel("Date")
plt.ylabel("Sales")
plt.xticks(rotation=45)
plt.show()

# Top Products

top_products = product_sales.sort_values(
    ascending=False
).head()

plt.figure(figsize=(8,5))
plt.bar(top_products.index,top_products.values)

plt.title("Top Products")
plt.xlabel("Product")
plt.ylabel("Sales")
plt.xticks(rotation=45)
plt.show()

# Monthly Growth Analysis

df["Month"] = df["Date"].dt.to_period("M")

monthly_sales = df.groupby("Month")["Sales"].sum()

growth = monthly_sales.pct_change()*100

print("\nMonthly Growth:")
print(growth)

# Best Region
best_region = region_sales.idxmax()

print("\nBest Performing Region:",best_region)

# Key Insights
print("\nKey Insights")
print("Highest Selling Product:",product_sales.idxmax())
print("Best Region:",best_region)
print("Total Sales:",df["Sales"].sum())
print("Average Sales:",round(df["Sales"].mean(),2))