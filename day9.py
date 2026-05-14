import pandas as pd

# Sample dataset
data = {
    "Name": ["Yash", "Aman", "Riya", "Neha", "Rahul"],
    "Age": [22, 35, 27, 29, 31],
    "Salary": [60000, 45000, 75000, 52000, 48000]
}

# Create DataFrame
df = pd.DataFrame(data)

print("Original Dataset:\n")
print(df)

# Apply multiple conditions
filtered_data = df[(df["Salary"] > 50000) & (df["Age"] < 30)]

print("\nFiltered Results:\n")
print(filtered_data)

# Save filtered data to new CSV file
filtered_data.to_csv("filtered_data.csv", index=False)

print("\nFiltered data saved successfully as 'filtered_data.csv'")