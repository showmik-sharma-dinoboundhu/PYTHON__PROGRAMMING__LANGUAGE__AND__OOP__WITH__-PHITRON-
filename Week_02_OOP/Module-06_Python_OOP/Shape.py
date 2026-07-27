from math import pi

class Shape:
    def __init__(self,name) -> None:
        self.name = name



class Rectangel(Shape):
    def __init__(self, name, legth, width) -> None:
        self.lenth = legth
        self.width = width
        super().__init__(name)

    def areaRec(self):
        return self.lenth * self.width


class Circle(Shape):
    def __init__(self, name, Radius) -> None:
        self.Radius = Radius
        super().__init__(name)

    def areaCir(self):
        return pi * self.Radius * self.Radius


myRec = Rectangel("REC",10,20)
print(myRec.areaRec())

myCi = Circle("ROU", 20)
print(myCi.areaCir())


