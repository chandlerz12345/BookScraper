import requests
from bs4 import BeautifulSoup
from time import sleep


base_url = "http://books.toscrape.com/"


all_books = []

response = requests.get(base_url)
soup = BeautifulSoup(response.text, 'html.parser')


books = soup.find_all(class_ = "product_pod")

for book in books:
    
    all_books.append({
        'title': "asasassasas",
        "price": book.find(class_ = "price_color").get_text(),
        "availability": book.find(class_ = "instock").get_text()

    }
    )



print(all_books)
# print(soup.body)