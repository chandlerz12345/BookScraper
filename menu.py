import sys 
import scrap

class Menu:
 
 ''' Displays a list of choices on the terminal for  the user to run '''
 
 
 
 def __init__(self):
 
 
      
      self.scraping = Bookscrap()
      self.saving = AWSConnect()
 

      self.choices = {
 
           "1" : self.scraping.scrap_books,
 
           "2" : self.scraping.update_title,
 
           "3" : self.scraping.update_availabilty,

           "4" : self.scraping.update_price,

           "5" : self.scraping.delete,
           
           "6" : self.scraping.save_json,
           
           "7" : self.saving.save2s3,
 
           "Q" : self.quit
 
 
 
        }
 
 
 
 def display_menu(self):
 
       print(""" 
            **************************
             Welcome to Young Scrapers!
             How can we help you?  
 
 
             1. Scrape Site
 
             2. Update title
             
             3. Update availability
 
             4. Update price

             5. Delete book

             6. Save to JSON
             
             7. Upload to S3
 
             Q. Quit program
 
             """)
 
 
 def run(self):
 
     ''' Display menu and respond to user choices '''
 
     while True:
 
           self.display_menu()
 
           choice = input("Enter an option: " )
 
           action = self.choices.get(choice)
 
           if action:
 
                action()
 
           else:
 
              print("{0} is not a valid choice".format(choice))

 def quit(self):

      choice = input("Do you want to save your session? y/n \n\n")
      if("y" in choice.lower()):
        self.task_manager.save() 
 
      ''' quit or terminate the program '''
 
      print("Thank you for visiting the warehouse today! \n")
 
      sys.exit(0)