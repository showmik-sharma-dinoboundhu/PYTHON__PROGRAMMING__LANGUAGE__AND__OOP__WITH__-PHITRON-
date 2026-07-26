class Vehical:
    def __init__(self,name,wheels,price) -> None:
        self.name = name
        self.wheels = wheels
        self.price = price

    def __repr__(self) -> str:
        return f"My Truck is {self.name}.It has {self.wheels} wheels and it's price {self.price} taka BD"

    def move(self):
        pass

class Truck(Vehical):
    def __init__(self, name, wheels, price,weight) -> None:
        self.weight = weight
        super().__init__(name, wheels, price)

    def __repr__(self) -> str:
        return super().__repr__()

class PickUpTruck(Truck):
    def __init__(self, name, wheels, price, weight,size) -> None:
        self.size = size
        super().__init__(name, wheels, price, weight)

    def __repr__(self) -> str:
        print(f"My Truck Weight is {self.weight} Ton and it's size {self.size} foot")
        return super().__repr__()


class Bus(Vehical):
    def __init__(self, name, wheels, price,seat) -> None:
        self.seat = seat
        super().__init__(name, wheels, price)


class ACBus(Bus):
    def __init__(self, name, wheels, price, seat,temp) -> None:
        self.temp = temp
        super().__init__(name, wheels, price, seat)


myPickup = PickUpTruck("Cargo Truck",6,100000,20,56)
print(myPickup)