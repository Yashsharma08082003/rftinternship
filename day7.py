import pandas as pd

# Creating DataFrame
data = {
    "Name": ["AMIT", "RIYA", "JOHN"],
    "Math": [80, 90, 60],
    "Science": [70, 88, 65],
    "English": [85, 92, 70]
}

df = pd.DataFrame(data)

# Calculate average marks per student
df["Average"] = df[["Math", "Science", "English"]].mean(axis=1)

# Find topper
topper = df.loc[df["Average"].idxmax(), "Name"]

# Count students above average
overall_avg = df["Average"].mean()
above_avg_count = (df["Average"] > overall_avg).sum()

# Add grade column
def grade(avg):
    if avg >= 90:
        return "A+"
    elif avg >= 75:
        return "A"
    elif avg >= 60:
        return "B"
    else:
        return "C"

df["Grade"] = df["Average"].apply(grade)

# Subject-wise average
subject_avg = df[["Math", "Science", "English"]].mean()

# Output
print("Student Performance Dashboard\n")

print(df)

print("\nTopper:", topper)

print("\nNumber of Students Above Average:", above_avg_count)

print("\nSubject-wise Average:")
print(subject_avg)