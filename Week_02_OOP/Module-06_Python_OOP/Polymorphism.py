# Poly --> Many (Multiple)
# Morph --> Shape

class Animal:
    def __init__(self,name) -> None:
        self.name = name

    def makeSound(self):
        print("Making Sound")


class cat(Animal):
    def __init__(self, name) -> None:
        super().__init__(name)

    def makeSound(self):
        print("Meeooowww")

class Dog(Animal):
    def __init__(self, name) -> None:
        super().__init__(name)

    def makeSound(self):
        print("Gheuu GHeuu")

class Goat(Animal):
    def __init__(self, name) -> None:
        super().__init__(name)

    def makeSound(self):
        print("bheeh bhehheh")

Don = cat("Real Don")
Don.makeSound()

Shepard = Dog("Local Shepard")
Shepard.makeSound()

Lo = Goat("Loooo")
Lo.makeSound()

animals = [Don, Shepard, Lo]
for i in animals:
    i.makeSound()