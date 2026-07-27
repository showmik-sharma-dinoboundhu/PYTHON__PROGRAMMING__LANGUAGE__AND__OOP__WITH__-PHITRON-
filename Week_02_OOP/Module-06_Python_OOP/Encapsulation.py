class Bank:
    def __init__(self,name,holder_Name,intial_Deposit) -> None:
        self.name = name
        self.holderName = holder_Name
        self.__balance = intial_Deposit
        self._branch = "Banani 12"

    def deposit(self,amount):
        self.__balance += amount

    def get_balance(self):
        return self.__balance

    def withdraw(self,amount):
        if amount < self.__balance:
            self._branch -= amount
            return amount
        else:
            return f"Fokira tui jmn tor bank account o tmn"


Rafsaan = Bank("Rafsaaan the Choto vai","Rafsaan",10000)
print(Rafsaan)
print(Rafsaan.holderName) 
Rafsaan.holderName = "The boro vai"
print(Rafsaan.holderName) 
print(Rafsaan.name)
# print(Rafsaan.__balance)
Rafsaan.deposit(40000)
print(Rafsaan.get_balance())
print(Rafsaan._branch)
print(dir(Rafsaan))
print(Rafsaan._Bank__balance)