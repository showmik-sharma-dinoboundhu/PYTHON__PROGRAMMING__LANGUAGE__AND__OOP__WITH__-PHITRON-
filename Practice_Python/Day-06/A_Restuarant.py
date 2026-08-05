from abc import ABC, abstractmethod

class User(ABC):
    def __init__(self, name, phone, email, add) -> None:
        self.name = name
        self.phone = phone
        self.email = email
        self.address = add

class Customer(User):
    def __init__(self, name, money, phone, email, add) -> None:
        self.wallet = money
        self.__order = None
        super().__init__(name, phone, email, add)

    @property
    def order(self):
        return self.order

    @order.setter
    def order(self, order):
        self.__order = order

    def place_of_Order(self, order):
        self.order = order
        return(f"{self.name} in the order")

    def place_order(self, order):
        self.order = order
        return(f"{self.name} for the man")

    def eat_food(self, order):
        return(f"{self.name} with items of{order.items}")

    def pay_for_order(self, order):
        pass

    def give_tips(self, tips_amount):
        pass

    def give_review(self, stars):
        pass


class Employee(User):
    def __init__(self, name, salary, starting_date, department, phone, email, add) -> None:
           super().__init__(name, phone, email, add)
           self.salary = salary
           self.starting_date = starting_date
           self.department = department
           self.starting_date = starting_date
           self.department = department


class Chef(Employee):
    def __init__(self, name, salary, starting_date, department, phone, email, add, cooking_item) -> None:
        super().__init__(name, salary, starting_date, department, phone, email, add)
        self.cooking_item = cooking_item


class Server(Employee):
    def __init__(self, name, salary, starting_date, department, phone, email, add) -> None:
        super().__init__(name, salary, starting_date, department, phone, email, add)
        self.tips = 0

    def take_order(self, order):
        pass

    def transfer_order(self, order):
        pass

    def serve_order(self, order):
        pass

    def receive_tips(self, amount):
        self.tips += amount


class Manager(Employee):
    def __init__(self, name, salary, starting_date, department, phone, email, add) -> None:
        super().__init__(name, salary, starting_date, department, phone, email, add)



        