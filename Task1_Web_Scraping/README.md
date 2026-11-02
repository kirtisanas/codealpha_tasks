# Task 1: Web Scraping – Books to Scrape

## Project Overview
This project uses Python to collect book information from the practice website [Books to Scrape](https://books.toscrape.com/).

The extracted information is stored in a CSV file for further analysis.

## Tools and Technologies
- Python
- Requests – to send HTTP requests
- BeautifulSoup – to extract information from HTML
- Pandas – to organize and save the data
- VS Code – development environment

## Information Collected
- Book Title
- Price
- Rating
- Availability

## Project Structure
```text
Task1_Web_Scraping/
├── data/
│   └── scraped_books.csv
├── screenshots/
├── web_scraping.py
└── README.md
```

## How It Works
1. Connects to the Books to Scrape website.
2. Visits the website's pages.
3. Extracts book titles, prices, ratings, and availability.
4. Stores the extracted information in a Pandas DataFrame.
5. Exports the data into a CSV file.

## How to Run
Install the required libraries:

```bash
python -m pip install requests beautifulsoup4 pandas
```

Run the Python script:

```bash
python web_scraping.py
```

## Output
The scraped book information is saved as `scraped_books.csv` inside the `data` folder.

## Disclaimer
This project uses Books to Scrape, a practice website created for learning web scraping.


