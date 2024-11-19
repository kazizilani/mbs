#imports the menu input validator
from utils.IO import IO

from interfaces.user_account import UserAccount


class UserMenu:
    def __init__(self, user):
        self.user = user
        self.response = None
    
    def UserMenuController(self):
        print("1. Check Balance")
        print("2. Withdraw Money")
        print("3. Send Money")
        print("4. Deposit")
        print("5. Recent Transactions")
        print("6. Logout")

        # returns a valid response and handle input errors
        self.response = int(str(IO(1,5).ask_input()))

        #check balance
        if self.response == 1:
            UserAccount(self.user).CheckBalance()

        #withdraw money
        elif self.response == 2:
            UserAccount(self.user).CashOut()
        
        #send money
        elif self.response == 3:
            UserAccount(self.user).SendMoney()

        #desposit money
        elif self.response == 4:
            UserAccount(self.user).Deposit()
        
        #check latest transactions
        elif self.response ==5:
            UserAccount(self.user).TransactionHistory()
        
        #logout
        else:
             print(f"👋 Goodbye, {self.user["name"]}!")
        



