import requests
from bs4 import BeautifulSoup

# URL of FlixPatrol Netflix Trending Page
URL = "https://flixpatrol.com/top10/netflix/"

# Set headers to mimic a browser request
HEADERS = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.0.0 Safari/537.36"
}

# Fetch the webpage content
response = requests.get(URL, headers=HEADERS)

# Check if request was successful
if response.status_code == 200:
    print("Successfully fetched the webpage!")

    # Parse the HTML content using BeautifulSoup
    soup = BeautifulSoup(response.text, "html.parser")

    # Find all trending movies/shows
    trending_items = soup.find_all("a", class_="hover:underline")  # Check if this class is correct in Inspect Element

    # Extract and display names
    print("\nTrending on Netflix:")
    for index, item in enumerate(trending_items[:10], start=1):  # Limiting to top 10
        print(f"{index}. {item.text.strip()}")
else:
    print(f"Failed to fetch data. Status code: {response.status_code}")
import csv

# Define the CSV file name
filename = "netflix_trending.csv"

# Open the CSV file and write data
with open(filename, mode="w", newline="", encoding="utf-8") as file:
    writer = csv.writer(file)
    
    # Write header
    writer.writerow(["Rank", "Show/Movie Name"])
    
    # Write data
    for index, item in enumerate(trending_items[:10], start=1):  # Top 10
        writer.writerow([index, item.text.strip()])

print(f"\nData saved successfully in {filename} ✅")
