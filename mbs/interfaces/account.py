from interfaces.transfer_logic import TransferLogic

class Account(TransferLogic):
    def __init__(self, account):
        self._account_type = account["account-type"]
        self.__balance = account["balance"]
        self.__daily_t_limit =account["daily-transaction-limit"]

        #constructing deposit, withdraw, and send money logic
        super().__init__()
    # returns the account balance
    def get_balance(self):
        return self.__balance
    
    
    def set_balance(self, transaction_type, balance, amount, *rcvr):
        #d = deposit
        #calls deposit method for deposit
        if transaction_type =="d":
            return super()._deposit(balance, amount)
        
        #w = withdraw
        #calls the withdraw method for withdraw
        elif transaction_type == "w":
            if amount <= self.__daily_t_limit:
                return super()._withdraw(balance, amount)
            else:
                print("Over Daily Transaction Limit")

        elif transaction_type == "s":
            if amount <= self.__daily_t_limit:
                return super()._send_money(balance, amount, rcvr)
            else:
                print("Over Daily Transaction Limit")
        
        else:
            print("Inappropriate Transaction Method")