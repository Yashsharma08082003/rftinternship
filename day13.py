import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Sample student marks data
data = {
    'Marks': [45, 56, 67, 78, 89, 90, 65, 74, 82, 55,
              68, 72, 84, 91, 63, 58, 77, 80, 69, 95]
}

# Create DataFrame
df = pd.DataFrame(data)

# Print basic information
print("Student Marks:")
print(df)

# Calculate skewness
skewness = df['Marks'].skew()
print("\nSkewness:", skewness)

# Plot histogram with KDE curve
plt.figure(figsize=(8,5))

sns.histplot(
    data=df,
    x='Marks',
    bins=8,
    kde=True
)

plt.title("Distribution Analysis of Student Marks")
plt.xlabel("Marks")
plt.ylabel("Frequency")

plt.show()

# Identify distribution type
if skewness > 0:
    print("Data is Positively Skewed")
elif skewness < 0:
    print("Data is Negatively Skewed")
else:
    print("Data is Symmetric")