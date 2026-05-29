import pandas as pd
import matplotlib.pyplot as plt

# -----------------------------
# STEP 1: CREATE DATASET
# -----------------------------

data = {
    "Product": ["Laptop", "Phone", "Tablet", "Headphones", "Smartwatch"],
    "Sales": [50000, 40000, 25000, 15000, 20000],
    "Profit": [10000, 8000, 5000, 3000, 4000],
    "Region": ["North", "South", "East", "West", "North"]
}

df = pd.DataFrame(data)

# Save dataset into CSV file
df.to_csv("sales_data.csv", index=False)

print("Dataset Created Successfully!\n")

# -----------------------------
# STEP 2: LOAD DATASET
# -----------------------------

df = pd.read_csv("sales_data.csv")

print("Sales Dataset:\n")
print(df)

# -----------------------------
# STEP 3: DATA CLEANING
# -----------------------------

# Check missing values
print("\nMissing Values:\n")
print(df.isnull().sum())

# Check duplicate rows
print("\nDuplicate Rows:", df.duplicated().sum())

# -----------------------------
# STEP 4: DATA ANALYSIS
# -----------------------------

print("\nTotal Sales:", df["Sales"].sum())
print("Average Profit:", df["Profit"].mean())

# Highest selling product
highest_sales = df.loc[df["Sales"].idxmax()]
print("\nHighest Selling Product:")
print(highest_sales)

# -----------------------------
# STEP 5: DATA VISUALIZATION
# -----------------------------

# Bar Chart for Sales
plt.figure(figsize=(8,5))
plt.bar(df["Product"], df["Sales"])
plt.title("Product Sales Analysis")
plt.xlabel("Products")
plt.ylabel("Sales")
plt.show()

# Pie Chart for Profit Distribution
plt.figure(figsize=(6,6))
plt.pie(df["Profit"], labels=df["Product"], autopct='%1.1f%%')
plt.title("Profit Distribution")
plt.show()

# -----------------------------
# STEP 6: INSIGHTS
# -----------------------------

print("\nINSIGHTS:")
print("1. Laptop has the highest sales.")
print("2. Headphones generated the lowest profit.")
print("3. North region appears multiple times, showing strong market presence.")
print("4. Sales and profit are positively related.")

# -----------------------------
# STEP 7: FINAL SUMMARY
# -----------------------------

print("\nPROJECT SUMMARY:")
print("This capstone project demonstrates data cleaning,")
print("analysis, visualization, and insight generation")
print("using Python and Pandas.")