#imports the menu input validator
from utils.IO import IO

from interfaces.user_account import UserAccount


class UserMenu:
    def __init__(self, user):
        #information about the account
        self.__user = user
        self.__accounts = self.__user["accounts"]
        self.__transactions = [*self.__accounts[0]["transaction-history"], *self.__accounts[1]["transaction-history"]]

        #response from the user
        self.response = None
        
    
    def UserMenuController(self):
       while True:
            print("1. Check Balance")
            print("2. Withdraw Money")
            print("3. Send Money")
            print("4. Deposit")
            print("5. Recent Transactions")
            print("6. Logout")

            # returns a valid response and handle input errors
            self.response = int(str(IO(1,6).ask_input()))

            #check balance
            if self.response == 1:
                UserAccount(self.__user).CheckBalance()

            #withdraw money
            elif self.response == 2:
                index, balance, transaction_record = UserAccount(self.__user).CashOut()
                self.__user["accounts"][index]["balance"] = balance
                self.__user["accounts"][index]["transaction-history"].insert(0,transaction_record)
                self.__transactions.insert(0, transaction_record)
            #send money
            elif self.response == 3:
                index, balance, transaction_record = UserAccount(self.__user).SendMoney()
                self.__user["accounts"][index]["balance"] = balance
                self.__user["accounts"][index]["transaction-history"].insert(0,transaction_record)
                self.__transactions.insert(0, transaction_record)

            #desposit money
            elif self.response == 4:
                index, balance, transaction_record = UserAccount(self.__user).Deposit()
                self.__user["accounts"][index]["balance"] = balance
                self.__user["accounts"][index]["transaction-history"].insert(0,transaction_record)
                self.__transactions.insert(0, transaction_record)
            
            #check latest transactions
            elif self.response ==5:
                UserAccount(self.__user).TransactionHistory(self.__transactions)
            
            #logout
            else:
                print(f"👋 Goodbye, {self.__user["name"]}!")
                break
            



