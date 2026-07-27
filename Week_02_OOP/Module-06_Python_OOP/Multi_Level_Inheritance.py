# Multi-level inheritance: Grandpa --> parents --> child (Vehicles --> Bus --> ACBus)

class Vehical:
    def __init__(self,name,price) -> None:
        self.name = name
        self.price = price

    def __repr__(self) -> str:
        return f"{self.name},{self.price}"

    def move(self):
        pass

class Bus(Vehical):
    def __init__(self, name, price,seat) -> None:
        self.seat = seat
        super().__init__(name, price)

    def __repr__(self) -> str:
        return super().__repr__()


class Truck(Vehical):
    def __init__(self, name, price,weight) -> None:
        self.weight = weight
        super().__init__(name, price)


class PickUPTrack(Truck):
    def __init__(self, name, price, weight) -> None:
        super().__init__(name, price, weight)


class ACBus(Bus):
    def __init__(self, name, price, seat, temp) -> None:
        self.temp = temp
        super().__init__(name, price, seat)

    def __repr__(self) -> str:
        print(f"{self.seat}")
        return super().__repr__()


Greenline = ACBus("Green Line",500000,24,16)
print(Greenline)