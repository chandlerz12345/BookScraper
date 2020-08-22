from scrap import Bookscrape
from scrap import AWSConnect
import sys
import json

class Menu:

 def __init__(self):

    self.app = Bookscrape()
    
    self.options = {

      "1": self.app.scrape_books,

      "2": self.app.search,

      "3": self.app.delete,

      "4": self.app.update_price,

      "5": self.app.update_title,

      "6": self.app.update_availabilty,

      "Q": self.app.quit

    }
 def display_options(self):
      print(""" 
            ************* MAIN MENU *************
             Welcome to Last Mile Book Store! 

             Please choose one of the options below:
 
             1. Deploy Scrape
 
             2. Search For Item
 
             3. Delete An Item

             4. Update Item Price

             5. Update Item Title 

             6. Upadte Item Availability

             Q. Quit

             *************************************


             *************************************

 
             """)
 def run(self):
    while True:
      self.display_options()
      option = input("Enter an option: ")
      action = self.options.get(option)

      if action:
        action()
      else:
        print("{0} is not a valid option, Please try again".format(option))



if __name__ == "__main__":
  Menu().run()

