import requests
from bs4 import BeautifulSoup
from time import sleep
import boto3
import json


base_url = "http://books.toscrape.com/catalogue/page-{}.html"


all_books = []

def scrap_books():

    for n in range(1,51):
        scrap_url = base_url.format(n)
        print(f"scrapping page {n} of website")
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

        # sleep(1)
    return all_books

 


# print(soup.body)


books = scrap_books()
print(len(all_books))

print(books[1])

def save(books):
    with open('app.json', "w") as fp:
        json.dump(books, fp)

save(books)


