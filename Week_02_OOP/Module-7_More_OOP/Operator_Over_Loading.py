print (45 + 18 + 7)
print("Sakib " + "Al " + "Hasan")
print([12, 98] + [5,6,7,8,9,10])
print("\n")

#But But But this operator can't work in a class. 

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

    def __add__(self, other):
        return self.age + other.age

    def __mul__(self, other):
        return self.weight * other.weight

    def __truediv__(self, other):
        return self.height / other.height
    
    def __len__(self):
        return self.height

    def __gt__(self, other):
        return self.age > other.age
    



Sakib = Cricketer("Sakib Al Hasan", 38, 68, 91, "BD")
Mushi = Cricketer("Mushfiqure Rahim",38,65,72,"BD")

print(Sakib + Mushi)
print(Sakib * Mushi)
print(Sakib / Mushi)
print(len(Sakib))
print(Sakib > Mushi)