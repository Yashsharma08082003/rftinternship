import pandas as pd

# Create dataset
data = {
    "NAME": ["A", "B", "C", "D"],
    "DEPT": ["IT", "HR", "IT", "HR"],
    "SALARY": [50000, 40000, 60000, 45000]
}
# Convert into DataFrame
df = pd.DataFrame(data)

print("Employee Data:\n")
print(df)

# Average salary per department
avg_salary = df.groupby("DEPT")["SALARY"].mean()

print("\nAverage Salary Per Department:")
print(avg_salary)

# Highest paid employee per department
highest_paid = df.loc[df.groupby("DEPT")["SALARY"].idxmax()]

print("\nHighest Paid Employee Per Department:")
print(highest_paid)

# Count employees per department
emp_count = df.groupby("DEPT")["NAME"].count()

print("\nEmployee Count Per Department:")
print(emp_count)

# Sort departments by average salary
sorted_avg = avg_salary.sort_values(ascending=False)

print("\nDepartments Sorted By Average Salary:")
print(sorted_avg)