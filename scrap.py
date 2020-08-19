import requests
from bs4 import BeautifulSoup
from time import sleep


base_url = "http://books.toscrape.com/catalogue/page-{}.html"


all_books = []

for n in range(1,51):
    scrap_url = base_url.format(n)
    response = requests.get(scrap_url)

    soup = BeautifulSoup(response.text, "html.parser")

    books = soup.find_all(class_ = "product_pod")

    for book in books:

        all_books.append({
            # 'title': book.find('img', alt = True),
            'title': book.find('img')['alt'],
            "price": book.find(class_ = "price_color").get_text(),
            "availability": book.find(class_ = "instock").get_text()

        }
        )

 


print(all_books)
print(len(all_books))
# print(soup.body)