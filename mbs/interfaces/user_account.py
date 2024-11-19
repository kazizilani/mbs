#imports the menu input validator
from utils.IO import IO

from interfaces.account import Account

class UserAccount(Account):
    def __init__(self, user):
        self.user = user
        self.accounts = self.user["accounts"]
        self.__total_balance = 0
        self.__withdraw_account_number = 0
        self.account_balance = 0
        #self.daily_limit = 0
        self.daily_total_transaction = 0
        super().__init__()
        
    
    #displays the balances of user's accounts takes from the aurgument
    def CheckBalance(self):
        print("Account Balance")
        for account in self.accounts:
            self.__total_balance += int(account["balance"])
            print(f"+ {account["account-title"]}: {account["balance"]}")
        print(f"= Total Balance: {self.__total_balance}")
    
    #withdraw
    def CashOut(self):
        print("Withdraw")
        for i,account in enumerate(self.accounts):
            print(f"{i}. {account["account-title"]}: {account["balance"]}")
        
        self.__withdraw_account_number = int(IO(0,1,"Select Withdraw Account").ask_input())
        self.account_balance = self.accounts[self.__withdraw_account_number]["balance"]
        amount = int(input("Enter Withdrawal Amount: "))
        self.daily_limit = self.user["accounts"][self.__withdraw_account_number]["daily-transaction-limit"]

        #self.daily_total_transaction += amount

        #withdraws and updates balance
        updated_balance = super().set_balance('w', self.account_balance, amount, self.daily_limit)

        print(f"New Balance: {updated_balance}")

        transaction_record = {
            "transaction-type": "withdraw",
            "amount": amount
        }
        
        #returns account number & updated balance
        return [self.__withdraw_account_number, updated_balance, transaction_record]
       
        

    def SendMoney(self):
        print("Send Money")
        for i,account in enumerate(self.accounts):
            print(f"{i}. {account["account-title"]}: {account["balance"]}")
        
        self.__withdraw_account_number = int(IO(0,1,"Select Withdraw Account").ask_input())
        self.account_balance = self.accounts[self.__withdraw_account_number]["balance"]
        self.daily_limit = self.user["accounts"][self.__withdraw_account_number]["daily-transaction-limit"]
        amount = int(input("Enter Send Amount: "))
        rcvr = str(input("Enter A Reciever: "))
        
        #self.daily_total_transaction += amount
        
        #return updated balance
        updated_balance = super().set_balance('s', self.account_balance, amount, self.daily_limit, rcvr)
        print(f"New Balance: {updated_balance}")
        

        transaction_record = {
            "transaction-type": "transfer",
            "amount": amount
        }
       
        return [self.__withdraw_account_number, updated_balance, transaction_record]

    def Deposit(self):
        print("Deposit Money")
        for i,account in enumerate(self.accounts):
            print(f"{i}. {account["account-title"]}: {account["balance"]}")
        self.__withdraw_account_number = int(IO(0,1,"Select Deposit Account").ask_input())
        self.account_balance = self.accounts[self.__withdraw_account_number]["balance"]
        amount = int(input("Enter Deposit Amount: "))
        updated_balance = super().set_balance('d', self.account_balance, amount, 1000000)
        transaction_record =  {
            "transaction-type": "deposit",
            "amount": amount
        }
        print(f"New Balance: {updated_balance}")
        
        return [self.__withdraw_account_number, updated_balance, transaction_record]
        
    def TransactionHistory(self, transactions):
        print("Recent Transaction(s)")
        print("Type \t \tAmount\n")
        for transaction in transactions:
            print(f"{transaction["transaction-type"]} \t {transaction["amount"]}")

       
   
        

        

        
        