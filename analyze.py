import pandas as pd
import matplotlib.pyplot as plt

# Load the CSV file
df = pd.read_csv("netflix_trending.csv")

# Display the data
print("\nTop Trending Netflix Shows/Movies:\n")
print(df)

# Visualization: Bar Chart
plt.figure(figsize=(10, 5))
plt.barh(df["Show/Movie Name"], df["Rank"], color="skyblue")
plt.xlabel("Rank")
plt.ylabel("Show/Movie Name")
plt.title("Top 10 Trending Netflix Shows/Movies")
plt.gca().invert_yaxis()  # To display rank 1 at the top
plt.show()
