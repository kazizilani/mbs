class TransferLogic:
    #deposits money
    def _deposit(self, balance, amount):
        updated_balance = balance + amount
        return updated_balance
    
    #withdraws money
    def _withdraw(self, balance, amount):
        updated_balance = balance - amount
        return updated_balance
    
    #transfers money
    def _send_money(self, balance, amount, rcvr):
        updated_balance = balance - amount
        print(f"money sent to {rcvr[0]}")
        return updated_balance
        
