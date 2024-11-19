#import the user data [in key-value pair format]
from db.UserData import User

#import the user menu 
from interfaces.user_menu import UserMenu

#storing the data in the environment
user = User

class Login:
    def __init__(self):
        #authentication credentials
        #limiting access to only withn the class
        self.__username = None
        self.__password = None
        self.__login_status = False
        self.__user_exists = False

    def LoginController(self):
        #keeps asking for username if user does not exists
        while not self.__user_exists:
            self.__username = input("Username: ")
            #if username exists, then sets user exits to true
            #ends the perpetual loop
            if user["username"] == self.__username:
                self.__user_exists = True
            else: 
                 print("⭕ User Does Not Exists")
        
        #if user exists, repeatedly ask for password
        if self.__user_exists:
            while not self.__login_status:
                self.__password = input("Password: ")

                if self.__password == user["password"]:
                    self.__login_status = True

                    #welcomes user by name
                    print(f"👋 Welcome, {user["name"]}!")
                
                else:
                        print("⭕ Wrong Password")

        #display the user menu till logged out    
        while self.__login_status:
            #instantiate user menu class
            #invoke user menu controller method
            print(self.__login_status)
            is_logged_out = UserMenu(user).UserMenuController()
            print(self.__login_status)
            #breaks the loop when user logs out
            self.__login_status = is_logged_out
            
                    