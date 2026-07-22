class Bank:
    def __init__(self,bal):
        self.balance = bal
        self.minWithdraw = 100
        self.maxWithdraw = 100000

    def get_balance(self):
        return self.balance
    
    def deposit(self,amount):
        if(amount > 0):
            self.balance += amount

    def withdraw(self,amount):
        if amount < self.minWithdraw:
            print(f"Fokira! You can withdra below {self.minWithdraw}")
        elif amount > self.maxWithdraw:
            print(f"Bank fokir hoye jabe. You can't Withdraw more than {self.maxWithdraw}")
        else:
            self.balance -= amount
            print(f"Here is your Money {amount}")
            print(f"Your Balance after withdraw {self.balance}")
        
DBBL = Bank(500)
DBBL.withdraw(25)
DBBL.withdraw(4000000000)
DBBL.withdraw(100)
