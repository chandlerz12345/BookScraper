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
        # sleep(1)
        response = requests.get(scrap_url)


        soup = BeautifulSoup(response.text, "html.parser")


        books = soup.find_all(class_ = "product_pod")

        for book in books:

            all_books.append({
                # 'title': book.find('img', alt = True),
                'title': book.find('img')['alt'].lower(),
                "price": book.find(class_ = "price_color").get_text(),
                "availability": book.find(class_ = "instock").get_text()

            }
            )

        # sleep(1)
    return all_books

 


# print(soup.body)

def search(books):
    to_search = input("what is the title of the item you would like to search: ").lower()
    for book in books:
        if book['title'] == to_search:
            print(book['title'])
            print(f"the price of the book if {book['price']}")
            print(f"the item is currently {book['availability']}")
      


def delete(books):
    to_search = input("what is the title of the item you would like to  delete: ").lower()
    for book in books:
        if book['title'] == to_search:
            book.clear()
            print("the book listing has been removes")



def update_price(books):
    counter = 0
    search = input("what is the item would you like to update: ").lower() 
    for book in books:
        if book['title'] == search:
            print(f"the current price of the item is {book['price']}")
            new_price = input("what is the new price of the item: ")
            book['price'] = new_price
            print (books[counter])
        else:
            counter += 1

def update_title(books):
    counter = 0
    search = input("what is the item would you like to update: ").lower() 
    for book in books:
        if book['title'] == search:
            print(f"the current title of the item is {book['title']}")
            new_title = input("what is the new title of the item: ")
            book['title'] = new_title
            print (books[counter])
        else:
            counter += 1


def update_availabilty(books):
    counter = 0
    search = input("what is the item would you like to update: ").lower() 
    for book in books:
        if book['title'] == search:
            print(f"the current availability of the item is {book['availability']}")
            new_availability = input("what is the new availability of the item: ")
            book['availability'] = new_availability
            print (books[counter])
        else:
            counter += 1


def save(books):
    with open('app.json', "w") as fp:
        json.dump(books, fp)





books = scrap_books()
print(len(all_books))


search(books)
# delete(books)
update_price(books)
update_availabilty(books)
update_title(books)

save(books)