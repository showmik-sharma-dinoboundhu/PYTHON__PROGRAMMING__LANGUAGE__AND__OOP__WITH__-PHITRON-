class Fish:
    def __init__(self,name,catagory,weight,price,egg) -> None:
        self._name = name
        self._catagory = catagory
        self._weight = weight
        self._price = price
        self.__egg = egg

    @property
    def egg(self):
        return self.__egg

    @egg.setter
    def egg(self,big):
        if big == "Big Egg":
            self.__egg = big
            print("YES!!")
        else:
            print("NO!!")
     




Rui = Fish("Rui Maach","Big","1 KG to Start",280,"YES")
print(Rui._name)
print(Rui.egg)
Rui.egg = "Big Egg"
print(Rui.egg)
