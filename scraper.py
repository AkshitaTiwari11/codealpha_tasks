import requests
from bs4 import BeautifulSoup
import pandas as pd

# 1. Target URL
URL = "http://books.toscrape.com/"

print("Connecting to the website...")
response = requests.get(URL)

if response.status_code == 200:
    print("Successfully connected!")
    soup = BeautifulSoup(response.text, 'html.parser')

    titles = []
    prices = []

    books = soup.find_all('article', class_='product_pod')

    for book in books:
        title = book.h3.a['title']
        price = book.find('p', class_='price_color').text
        clean_price = price.replace('Â£', '$').replace('£', '$')

        titles.append(title)
        prices.append(clean_price)

    data = {'Book Title': titles, 'Price': prices}
    df = pd.DataFrame(data)

    df.to_csv('CodeAlpha_Scraped_Books.csv', index=False, encoding='utf-8-sig')
    print("Success! Data saved to 'CodeAlpha_Scraped_Books.csv'")
    print("\nData Preview:")
    print(df.head())
else:
    print(f"Failed to retrieve the webpage. Status code: {response.status_code}")