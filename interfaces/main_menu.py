#imports the menu input validator
from utils.IO import IO

from interfaces.login import Login

class MainMenu:
    def __init__(self):
        self.__response = None
        self.__exit_request = False
    
    def MenuController(self):
        # keeps the program running till user does not exit
        while not self.__exit_request:
            print("1. Login")
            print("2. Exit")
            
            # returns a valid response and handle input errors
            self.__response = int(str(IO(1,2).ask_input()))

            #instantiates the login interface
            #invokes login controller method
            if self.__response == 1:
                Login().LoginController()

            #sets the exit request == True to exit the loop
            #prints goodbye as message
            else:
                self.__exit_request = True
                print("👋 Goodbye!")
           

