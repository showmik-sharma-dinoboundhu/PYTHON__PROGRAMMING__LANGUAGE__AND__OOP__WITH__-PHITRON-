class user:
    def __init__(self,name,age,money) -> None:
        self._name = name
        self._age = age
        self.__money = money

    #Getter without any Setter is randmoly attribute
    @property
    def age(self):
        return self._age

    #Getter
    @property
    def salary(self):
        return self.__money

    #Setter
    @salary.setter
    def salary(self,value):
        if value < 0:
            return "Salary can't be negative"
        self.__money += value
    

samsu = user("kopa",21,12000)

# print(samsu.__money)
# print(samsu.age())
print(samsu.age)
# print(samsu.salary())
print(samsu.salary)
samsu.salary= 45000
print(samsu.salary)