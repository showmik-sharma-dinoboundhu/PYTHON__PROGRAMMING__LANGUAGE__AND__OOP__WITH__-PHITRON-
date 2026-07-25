#Sorok pothe biman poribohon like- Ena, Hanif

class Company:
    def __init__(self,name, add) -> None:
        self.name = name
        self.bus = []
        self.routes = []
        self.Counter = []
        self.Supervisor = []

    def __repr__(self) -> str:
        return f"The Bus {self.name} is one of the biggest {self.bus} in BD.It has so many routes, like- {self.routes} with so many {self.Counter} and so many {self.Supervisor}"


class Driver:
    def __init__(self,name, licence,age) -> None:
        self.name = name
        self.licence = licence
        self.age = age

    def __repr__(self) -> str:
        return f"Drive is: {self.name} and his licence {self.licence} with this {self.age} "


class Counter:
    def __init__(self,add,route) -> None:
        self.add = add
        self.route = route


class Passengers:
    def __init__(self,route,bus,time,AC,NON_AC) -> None:
        self.route = route
        self.bus = bus
        self.time = time
        self.AC = AC
        self.NON_AC = NON_AC


class Supervisors:
    def __init__(self,name,age,experince,route) -> None:
        self.name = name
        self.age = age
        self.experince = experince
        self.route = route


LAL_MIA = Driver("Lal mia",3425634,48)
print(LAL_MIA)

ENA_Travels = Company("ENA TRAVELS NTR",3)
print(ENA_Travels)