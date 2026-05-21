import matplotlib.pyplot as plt

# Dataset
categories = ["FOOD", "TRAVEL", "SHOPPING"]
expenses = [500, 300, 200]

# Highlight highest category
explode = [0.1 if x == max(expenses) else 0 for x in expenses]

# Create pie chart
plt.pie(
    expenses,
    labels=categories,
    autopct='%1.1f%%',   # percentage labels
    explode=explode,     # highlight highest category
    shadow=True,
    startangle=90
)

plt.title("Expense Category Breakdown")
plt.axis('equal')  # Makes pie chart circular

plt.show()