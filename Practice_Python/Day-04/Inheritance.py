class Gadget:
    def __init__(self,brand,price,color,origin) -> None:
        self.brand= brand
        self.price = price
        self.color = color
        self.origin = origin

    def runing(self):
        return f"I am using this {self.brand} for a while"


class Laptop(Gadget):
    def __init__(self,brand,price,color,origin,memory,ssd) -> None:
        self.memory = memory
        self.ssd = ssd
        super().__init__(brand,price,color,origin)

    def __repr__(self) -> str:
        return f"I am going to buy: {self.brand} with Taka {self.price} and mix with  {self.memory} and {self.ssd} and it's {self.origin}"


class Phone:
    def __init__(self,dual_sim,call) -> None:
        self.dual_sim = dual_sim
        self.call = call


class Camera:
    def __init__(self,pixel,lens) -> None:
        self.pixel = pixel
        self.lens = lens


myLaptop = Laptop("Lenevo IdeaPad S145",52500,"Black","Chain",256,8)
print(myLaptop)