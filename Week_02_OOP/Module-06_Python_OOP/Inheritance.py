# Base class --> parent class --> common attributes + functionality class
# Derived class --> child class --> Uncommon attributes + functionality class

class Gadget:
    def __init__(self,brand,price,color,origin) -> None:
        self.brand = brand
        self.price = price
        self.color = color
        self.origin = origin

        def running(self):
            return f"Running Laptop: {self.brand}"



class Laptop:
    def __init__(self,memory,SSD) -> None:
        self.memory = memory
        self.SSD = SSD

    def coding(self):
        return f"Learning Python and Practicing"


class Phone(Gadget):
    def __init__(self,brand,origin,color,price,dual_sim) -> None:
        self.dual_sim = dual_sim
        super().__init__(brand,origin,color,price)

    def __repr__(self) -> str:
        return f"My phone: {self.brand} {self.origin} {self.color} {self.price} {self.dual_sim}."


class Camera:
    def __init__(self,pixel,lens):
        self.pixel = pixel
        self.lens = lens

    def changeLens(self):
        return f"I am going to change the {self.lens}"

        
#Inheritance:
myPhone = Phone("Realme","China","Fresh Green",12000,True)
print(myPhone)
# print(myPhone.brand,myPhone.origin,myPhone.price,myPhone.color)