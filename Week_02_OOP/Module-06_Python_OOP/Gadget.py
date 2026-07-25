class Laptop:
    def __init__(self,brand,price,color,memory) -> None:
        self.brand = brand
        self.color = color
        self.memory = memory
        self.price = price

    def runing(self,brand):
        return f"Running Laptop: {brand}"

    def coding(self):
        return f"Learning Python and Practicing"


class Phone:
    def __init__(self,brand,color,dual_sim,price) -> None:
        self.brand = brand
        self.color = color
        self.dual_sim = dual_sim
        self.price = price

    def using(self):
        return f"Right now my running phone is: {self.brand}"


class Camera:
    def __init__(self,brand,price,color,pixel,lens):
        self.brand = brand
        self.price = price
        self.color = color
        self.pixel = pixel
        self.lens = lens

    def run(self):
        return f"I am using this {self.brand} camera for a while"

    def changeLens(self):
        return f"I am going to change the {self.lens}"
        
