class Person:
    def __init__(self,name,age,height,weight) -> None:
        self.name = name
        self.age = age
        self.height = height
        self.weight = weight

    def eat(self):
        print("Vat, Mangso, Polau, Korma")

    def GYM(self):
        raise NotImplementedError


class Cricketer(Person):
    def __init__(self, name, age, height, weight,team) -> None:
        self.team = team
        super().__init__(name, age, height, weight)

    #This is called override where child overRide on parent
    def eat(self):
        print("Vegitable")

    def GYM(self):
        print("IT's workable")



sakib = Cricketer("Sakib Al Hasan", 38, 68, 91, "BD")
sakib.eat()
sakib.GYM()