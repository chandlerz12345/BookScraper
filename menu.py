import sys # importing the sys library from Python to quit menu 

class Menu:
 
 ''' Displays a list of choices on the terminal for  the user to run '''
 
 
 
 def __init__(self):
 
 
      #instantiate a new task manager object
      self.task_manager = TaskManager() 
 
      #defines the actions the user can perform
      #notice how for choices 1-5 we call the functions we defined in our TaskManager class
      self.choices = {
 
           "1" : self.task_manager.show_tasks,
 
           "2" : self.task_manager.create_task,
 
           "3" : self.task_manager.search_task,

           "4" : self.task_manager.update_task,

           "5" : self.task_manager.delete_task,
 
           "Q" : self.quit
 
 
 
        }
 
 
 
 def display_menu(self):
 
       print(""" 
            **************************
             Welcome to Task Manager!
             How can we help you?  
 
 
             1. Show tasks
 
             2. Create task
 
             3. Search tasks

             4. Update tasks

             5. Delete task
 
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
        self.task_manager.save() # saving our session to a file 
 
      ''' quit or terminate the program '''
 
      print("Thank you for visiting the warehouse today! \n")
 
      sys.exit(0) # we use the sys library to call exit and stop app