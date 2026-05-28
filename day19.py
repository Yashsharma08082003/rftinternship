import pandas as pd
import matplotlib.pyplot as plt

# Sample dataset
data = {
    "Date": [
        "2025-05-01", "2025-05-02", "2025-05-03",
        "2025-05-04", "2025-05-05", "2025-05-06",
        "2025-05-07", "2025-05-08", "2025-05-09",
        "2025-05-10"
    ],
    "Stock_Price": [100, 102, 101, 105, 108, 107, 111, 115, 113, 118]
}

# Create DataFrame
df = pd.DataFrame(data)

# Convert Date column into datetime
df["Date"] = pd.to_datetime(df["Date"])

# Calculate Moving Average
df["Moving_Average"] = df["Stock_Price"].rolling(window=3).mean()

# Identify Peaks and Drops
highest_price = df["Stock_Price"].max()
lowest_price = df["Stock_Price"].min()

highest_day = df[df["Stock_Price"] == highest_price]
lowest_day = df[df["Stock_Price"] == lowest_price]

print("Highest Stock Price:")
print(highest_day)

print("\nLowest Stock Price:")
print(lowest_day)

# Detect Volatility
df["Volatility"] = df["Stock_Price"].pct_change() * 100

print("\nDataset with Moving Average and Volatility:")
print(df)

# Visualization
plt.figure(figsize=(10, 5))

# Stock Price Trend
plt.plot(df["Date"], df["Stock_Price"],
         marker='o', label="Stock Price")

# Moving Average Line
plt.plot(df["Date"], df["Moving_Average"],
         linestyle='--', label="Moving Average")

# Graph Labels
plt.title("Stock Price Time-Series Analysis")
plt.xlabel("Date")
plt.ylabel("Price")
plt.legend()
plt.grid(True)

# Show Plot
plt.show()