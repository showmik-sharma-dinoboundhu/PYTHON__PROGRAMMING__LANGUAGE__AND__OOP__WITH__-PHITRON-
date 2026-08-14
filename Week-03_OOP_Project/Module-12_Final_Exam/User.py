from abc import ABC, abstractmethod

class User(ABC):
    def __init__(self, name, email, address, account) -> None:
        self.name = name
        self.email = email
        self.address = address
        self.account = account
        self.transection_history = []


class Main_Account(User):
    def __init__(self, name, email, address, account) -> None:
        super().__init__(name, email, address, account)
        self.__current_balance = 0
        self.__savings = 0

    @property
    def savings(self):
        return self.__savings

    @savings.setter
    def savings(self, amount):
        self.__savings = amount


class Deposit(Main_Account):
    def __init__(self, name, email, address, account, amount) -> None:
        super().__init__(name, email, address, account)
        self.__amount = amount


class Withdraw(Main_Account):
    def __init__(self, name, email, address, account, amount) -> None:
        super().__init__(name, email, address, account)
        if amount < self.__current_balance:
            self.__current_balance -= amount
            print(f"Available balance is: {self.__current_balance}")
        else:
            print(f"Insufficient Balance!! Withdraw can't possible")

class Loan(Main_Account):
    def __init__(self, name, email, address, account, loan_cnt = 0) -> None:
        super().__init__(name, email, address, account)
        self.loan_cnt = loan_cnt

    def take_loan(self, amount):
        if self.loan_cnt > 2:
            print("Sorry Your Available Loan Process Done!!")
        else:
            self.__current_balance += amount
            print(f"Current Balance With Loan Amount is : {self.__current_balance}")

class Transfer_Money(Main_Account):
    def anothers_account(self, another_account, amount):
        self.another_account = another_account

        # Account Check:
        if not another_account:
            print("Account Doesn't Exist!!")

        # Amount Check:
        if amount <= 0:
            print("Invaild Amount!!")

        # Transter Money:
        self.__current_balance -= amount
        another_account += amount
        print(f"Your {amount} money transered successfully!!")


class Transection_History(Main_Account):
    def transection_times(self):
        if not self.transection_history:
            print("No Transection")
        for transection in self.transection_history:
            print(transection)


