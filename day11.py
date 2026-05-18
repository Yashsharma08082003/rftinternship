import matplotlib.pyplot as plt

# Dataset
dates = ["MON", "TUE", "WED", "THU", "FRI"]
sales = [200, 250, 300, 280, 350]

# Find highest and lowest sales
highest_sale = max(sales)
lowest_sale = min(sales)

highest_day = dates[sales.index(highest_sale)]
lowest_day = dates[sales.index(lowest_sale)]

# Create line plot
plt.plot(dates, sales, marker='o', linewidth=2)

# Highlight highest and lowest points
plt.scatter(highest_day, highest_sale, color='green', s=100, label='Highest Sale')
plt.scatter(lowest_day, lowest_sale, color='red', s=100, label='Lowest Sale')

# Add labels and title
plt.title("Weekly Sales Trend")
plt.xlabel("Days")
plt.ylabel("Sales")

# Add values near points
for i in range(len(dates)):
    plt.text(dates[i], sales[i] + 5, str(sales[i]), ha='center')

# Show legend
plt.legend()

# Display graph
plt.grid(True)
plt.show()