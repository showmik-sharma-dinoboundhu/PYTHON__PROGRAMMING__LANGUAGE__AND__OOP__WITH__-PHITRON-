from abc import ABC, abstractmethod

class Animal(ABC):
    @abstractmethod
    def eat(self):
        print("I need food")

    @abstractmethod
    def move(self):
        print("That thing is moving")

class Monkey(Animal):
    def __init__(self,name) -> None:
        self.catagory = "Monkey"
        self.name = name
        super().__init__()

    def eat(self):
        print("Hi Kaka come !!")

    def move(self):
        return super().move()


Tiger = Monkey("Tuuu")
Tiger.eat()
Tiger.move()