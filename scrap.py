import requests
from bs4 import BeautifulSoup
from time import sleep
import boto3
import json



class Bookscrap:
    def __init__(self):
        self.base_url = "http://books.toscrape.com/catalogue/page-{}.html"
        self.all_books = []

    def scrap_books(self):

        for n in range(1,51):
            self.scrap_url = self.base_url.format(n)
            print(f"scrapping page {n} of website")
            # sleep(1)
            self.response = requests.get(self.scrap_url)


            self.soup = BeautifulSoup(self.response.text, "html.parser")


            self.books = self.soup.find_all(class_ = "product_pod")

            for self.book in self.books:

                self.all_books.append({
                    # 'title': book.find('img', alt = True),
                    'title': self.book.find('img')['alt'].lower(),
                    "price": self.book.find(class_ = "price_color").get_text(),
                    "availability": self.book.find(class_ = "instock").get_text()

                }
                )

            # sleep(1)
        return self.all_books

    


    # print(soup.body)

    def search(self):
        self.to_search = input("what is the title of the item you would like to search: ").lower()
        for self.book in self.all_books:
            if self.book['title'] == self.to_search:
                print(self.book['title'])
                print(f"the price of the book if {self.book['price']}")
                print(f"the item is currently {self.book['availability']}")
        


    def delete(self):
        self.counter = 0
        self.to_search = input("what is the title of the item you would like to  delete: ").lower()
        for self.book in self.all_books:
            if self.book['title'] == self.to_search:
                self.book.clear()
                print("the book listing has been removed")
            else:
                self.counter +=1



    def update_price(self):
        self.counter = 0
        self.search = input("what is the item would you like to update: ").lower() 
        for self.book in self.all_books:
            if self.book['title'] == self.search:
                print(f"the current price of the item is {self.book['price']}")
                self.new_price = input("what is the new price of the item: ")
                self.book['price'] = self.new_price
                print (self.all_books[self.counter])
            else:
                self.counter += 1

    def update_title(self):
        self.counter = 0
        self.search = input("what is the item would you like to update: ").lower() 
        for self.book in self.all_books:
            if self.book['title'] == self.search:
                print(f"the current title of the item is {self.book['title']}")
                self.new_title = input("what is the new title of the item: ")
                self.book['title'] = self.new_title
                print (self.all_books[self.counter])
            else:
                self.counter += 1


    def update_availabilty(self):
        self.counter = 0
        self.search = input("what is the item would you like to update: ").lower() 
        for self.book in self.all_books:
            if self.book['title'] == self.search:
                print(f"the current availability of the item is {self.book['availability']}")
                self.new_availability = input("what is the new availability of the item: ")
                self.book['availability'] = self.new_availability
                print (self.all_books[self.counter])
            else:
                self.counter += 1


    def save(self):
        with open('app.json', "w") as fp:
            json.dump(self.all_books, fp)





# books = scrap_books()
# print(len(all_books))


# search(books)
# # delete(books)
# update_price(books)
# update_availabilty(books)
# update_title(books)

# save(books)


d1 = Bookscrap()
d1.scrap_books()
# d1.search()
# d1.update_title()
# d1.update_availabilty()
# d1.update_price()
d1.delete()
d1.save()