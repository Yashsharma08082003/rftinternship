import pandas as pd
import matplotlib.pyplot as plt

# Create sample dataset
data = {
    "Customer_ID": [101,102,103,104,105,106,107,108,109,110],
    "Age": [22,35,28,45,31,27,50,40,29,38],
    "Spending": [2000,8000,5000,12000,3000,9000,1500,7000,2500,10000],
    "Visits": [5,12,8,15,4,10,2,9,3,14]
}

df = pd.DataFrame(data)

# Save CSV file
df.to_csv("customers.csv", index=False)

print("Customer Dataset:\n")
print(df)

# Create Spending Segments
def segment(spending):
    if spending >= 8000:
        return "High"
    elif spending >= 4000:
        return "Medium"
    else:
        return "Low"

df["Category"] = df["Spending"].apply(segment)

# Identify high-value customers
high_value = df[df["Category"] == "High"]

# Identify low-engagement users
low_engagement = df[df["Visits"] < 5]

print("\nHigh Value Customers:")
print(high_value)

print("\nLow Engagement Customers:")
print(low_engagement)

# Business Strategy Suggestions
print("\nBusiness Strategies:")
print("1. Reward high-value customers with loyalty offers.")
print("2. Give discounts to low-engagement users.")
print("3. Send personalized recommendations.")
print("4. Improve customer retention campaigns.")

# Spending Distribution Chart
plt.figure(figsize=(8,5))
plt.hist(df["Spending"])
plt.xlabel("Spending")
plt.ylabel("Number of Customers")
plt.title("Spending Distribution")
plt.show()

# Customer Category Chart
category_count = df["Category"].value_counts()

plt.figure(figsize=(8,5))
plt.pie(category_count,
        labels=category_count.index,
        autopct='%1.1f%%')

plt.title("Customer Categories")
plt.show()