#imports the menu input validator
from utils.IO import IO

from interfaces.account import Account

class UserAccount(Account):
    def __init__(self, user):
        self.user = user
        self.accounts = self.user["accounts"]
        self.__total_balance = 0
        self.__withdraw_account_number = 0
        self.transactions = [self.accounts[0]["transaction-history"], self.accounts[1]["transaction-history"]]
        super().__init__(self.accounts[0])
        self.account_balance = self.accounts[self.__withdraw_account_number]["balance"]
    
    def CheckBalance(self):
        print("Account Balance")
        for account in self.accounts:
            self.__total_balance += int(account["balance"])
            print(f"+ {account["account-title"]}: {account["balance"]}")
        print(f"= Total Balance: {self.__total_balance}")
    
    def CashOut(self):
        print("Withdraw")
        for i,account in enumerate(self.accounts):
            print(f"{i}. {account["account-title"]}: {account["balance"]}")
        
        self.__withdraw_account_number = IO(0,1,"Select Withdraw Account").ask_input()
        
        amount = int(input("Enter Withdrawal Amount: "))

        updated_balance = super().set_balance('w', self.account_balance, amount)

       
        print(f"New Balance: {updated_balance}")

    def SendMoney(self):
        print("Send Money")
        for i,account in enumerate(self.accounts):
            print(f"{i}. {account["account-title"]}: {account["balance"]}")
        
        self.__withdraw_account_number = IO(0,1,"Select Withdraw Account").ask_input()
        
        amount = int(input("Enter Send Amount: "))
        rcvr = str(input("Enter A Reciever: "))

        updated_balance = super().set_balance('s', self.account_balance,amount, rcvr)

        print(f"New Balance: {updated_balance}")

    def TransactionHistory(self):
        print("Recent Transaction(s)")
        print("Type \t \tAmount\n")
        for transactions in self.transactions:
            for transaction in transactions:
                print(f"{transaction["transaction-type"]} \t {transaction["amount"]}")

       
    def Deposit(self):
        amount = int(input("Enter Deposit Amount: "))
        super().set_balance('d', self.account_balance, amount)
        

        

        
        