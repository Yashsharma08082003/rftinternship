# MINI EDA DASHBOARD USING SEABORN

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Sample Dataset
data = {
    "Month": ["Jan", "Feb", "Mar", "Apr", "May", "Jun"],
    "Sales": [200, 240, 300, 280, 350, 400],
    "Orders": [20, 25, 30, 28, 35, 40],
    "Profit": [50, 60, 75, 70, 90, 110]
}

# Create DataFrame
df = pd.DataFrame(data)

# Style
sns.set_style("whitegrid")

# Create Figure
fig, axes = plt.subplots(1, 3, figsize=(16, 5))

# ---------------- LINE PLOT ----------------
sns.lineplot(x="Month", y="Sales", data=df, marker='o', ax=axes[0])
axes[0].set_title("Monthly Sales Trend")

# ---------------- BAR PLOT ----------------
sns.barplot(x="Month", y="Profit", data=df, ax=axes[1])
axes[1].set_title("Profit Comparison")

# ---------------- HISTOGRAM ----------------
sns.histplot(df["Orders"], bins=5, kde=True, ax=axes[2])
axes[2].set_title("Orders Distribution")

# Layout
plt.tight_layout()

# Show Dashboard
plt.show()

# ---------------- INSIGHTS ----------------
print("INSIGHTS:")
print("1. Sales increased steadily over the months.")
print("2. Profit reached its maximum in June.")
print("3. Most order values are concentrated between 20 and 40.")
print("4. No strong outliers are present in the data.")