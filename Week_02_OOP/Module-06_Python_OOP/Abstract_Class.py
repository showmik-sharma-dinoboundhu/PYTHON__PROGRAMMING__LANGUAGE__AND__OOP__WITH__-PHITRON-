# From Abstract Base Class:

from abc import ABC, abstractmethod
class Animal(ABC):
    @abstractmethod     #enforce all derived class to have a eat method
    def eat(self):
        print("I need Food")

    @abstractmethod
    def move(self):
        print("I move away all over the forest.")

class Monkey(Animal):
    def __init__(self,name) -> None:
        self.catagory = "Monkey"
        self.name = name
        super().__init__()

    def eat(self):
        print("Hi Nana !! eating banana..")

    def move(self):
        print("Hanging on the branches")
      

Tiger = Monkey("Tuuuuu")
Tiger.eat()
Tiger.move()


