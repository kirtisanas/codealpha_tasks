
import requests
import pandas as pd
from bs4 import BeautifulSoup
from pathlib import Path
import time

# Website URL
base_url = "https://books.toscrape.com/catalogue/page-{}.html"

book_data = []

# Scrape all 50 pages
for page_number in range(1, 51):

    url = base_url.format(page_number)
    response = requests.get(url, timeout=15)
    response.raise_for_status()

    soup = BeautifulSoup(response.text, "html.parser")
    books = soup.find_all("article", class_="product_pod")

    for book in books:
        title = book.h3.a["title"]

        price = book.find(
            "p", class_="price_color"
        ).text.replace("Â", "")

        rating = book.find(
            "p", class_="star-rating"
        )["class"][1]

        availability = book.find(
            "p", class_="instock availability"
        ).text.strip()

        book_data.append({
            "Title": title,
            "Price": price,
            "Rating": rating,
            "Availability": availability
        })

    print(f"Page {page_number} completed")

    time.sleep(0.3)

# Convert data into DataFrame
df = pd.DataFrame(book_data)

# Save CSV inside this project's data folder
project_folder = Path(__file__).resolve().parent
output_folder = project_folder / "data"
output_folder.mkdir(parents=True, exist_ok=True)

df.to_csv(
    output_folder / "scraped_books.csv",
    index=False,
    encoding="utf-8-sig"
)

print("\nWeb scraping completed successfully!")
print("Total books scraped:", len(df))
print("\nFirst five records:")
print(df.head())
print("\nCSV file saved successfully!")
