import pandas as pd
import matplotlib.pyplot as plt

# Creating Movie Dataset
data = {
    "Movie Name": [
        "Inception", "Avengers Endgame", "Interstellar",
        "Joker", "Titanic", "Avatar", "3 Idiots",
        "Dangal", "Bahubali", "KGF 2"
    ],
    
    "Rating": [8.8, 8.4, 8.6, 8.5, 7.9, 7.8, 8.4, 8.3, 8.0, 8.2],
    
    "Genre": [
        "Sci-Fi", "Action", "Sci-Fi",
        "Drama", "Romance", "Sci-Fi",
        "Comedy", "Sports", "Action", "Action"
    ],
    
    "Revenue": [
        829, 2798, 677,
        1074, 2187, 2923,
        400, 330, 650, 1200
    ]
}

# Convert dictionary into DataFrame
df = pd.DataFrame(data)

# Display Dataset
print("MOVIE DATASET\n")
print(df)

# Highest Rated Movies
print("\nHighest Rated Movies:\n")
highest_rated = df.sort_values(by="Rating", ascending=False)
print(highest_rated[["Movie Name", "Rating"]])

# Most Profitable Genres
print("\nMost Profitable Genres:\n")
genre_profit = df.groupby("Genre")["Revenue"].sum()
print(genre_profit)

# Correlation between Rating & Revenue
correlation = df["Rating"].corr(df["Revenue"])
print("\nCorrelation between Rating and Revenue:")
print(correlation)

# Top 5 Movies
print("\nTop 5 Movies by Revenue:\n")
top5 = df.sort_values(by="Revenue", ascending=False).head(5)
print(top5[["Movie Name", "Revenue"]])

# Visualization 1: Genre vs Revenue
genre_profit.plot(kind="bar", figsize=(8,5))
plt.title("Genre vs Revenue")
plt.xlabel("Genre")
plt.ylabel("Revenue")
plt.xticks(rotation=45)
plt.show()

# Visualization 2: Rating Distribution
plt.figure(figsize=(8,5))
plt.hist(df["Rating"], bins=5)
plt.title("Rating Distribution")
plt.xlabel("Ratings")
plt.ylabel("Frequency")

plt.show()