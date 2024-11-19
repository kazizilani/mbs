from interfaces.transfer_logic import TransferLogic

class Account(TransferLogic):
    def __init__(self):
        #constructing deposit, withdraw, and send money logic
        super().__init__()
    # returns the account balance
    
    def set_balance(self, transaction_type, balance, amount, daily_limit, *rcvr):
        #d = deposit
        #calls deposit method for deposit
        if transaction_type =="d":

            return super()._deposit(balance, amount)
        
        #w = withdraw
        #calls the withdraw method for withdraw
        elif transaction_type == "w":
            if amount <= daily_limit:
                return super()._withdraw(balance, amount)
            else:
                print("Over Daily Transaction Limit")
                return balance
        elif transaction_type == "s":
            if amount <= daily_limit:
                return super()._send_money(balance, amount, rcvr)
            else:
                print("Over Daily Transaction Limit")
                return balance
        
        else:
            print("Inappropriate Transaction Method")
            return balance