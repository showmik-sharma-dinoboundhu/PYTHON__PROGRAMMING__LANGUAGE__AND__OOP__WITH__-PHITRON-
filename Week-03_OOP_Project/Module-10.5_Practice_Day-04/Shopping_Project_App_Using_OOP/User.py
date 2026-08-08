from abc import ABC, abstractmethod

class User(ABC):
    def __init__(self, name, email, NID, address) -> None:
        self.name = name
        self.email = email
        self.NID = NID
        self.address = address


class Customer(User):
    def __init__(self, name, email, NID, address, money) -> None:
        super().__init__(name, email, NID, address)
        self.wallet = money
        self.__order = None
        self.due_amount = 0     # Bcz just oder korche ekhno payment kore nai

    @property
    def Order(self):
        return self.Order

    @Order.setter
    def Order(self, order):
        self.__order = order


class Employee(User):
    def __init__(self, name, email, NID, address, salary, starting_job, department) -> None:
        super().__init__(name, email, NID, address)
        self.salary = salary
        self.due = salary
        self.starting_job = starting_job
        self.department = department

    def receive_salary(self):
        self.due = 0


class Cashier(Employee):
    def __init__(self, name, email, NID, address, salary, starting_job, department, income, buying) -> None:
        super().__init__(name, email, NID, address, salary, starting_job, department)
        self.wallet += income
        self.wallet -= buying


class Delivery(Employee):
    def __init__(self, name, email, NID, address, salary, starting_job, department, delivery_tips = 0) -> None:
        super().__init__(name, email, NID, address, salary, starting_job, department)
        self.delivery_tips = delivery_tips

    def receive_tips(self, amount):
        self.delivery_tips += amount


class Manager(Employee):
    def __init__(self, name, email, NID, address, salary, starting_job, department) -> None:
        super().__init__(name, email, NID, address, salary, starting_job, department)


class Visitor_Boy(Employee):
    def __init__(self, name, email, NID, address, salary, starting_job, department, check_expire_date, check_manufracture_date, help_customer) -> None:
        super().__init__(name, email, NID, address, salary, starting_job, department)
        self.manufracture = check_manufracture_date
        self.expire = check_expire_date
        self.customer_help = self.customer_help

    
        