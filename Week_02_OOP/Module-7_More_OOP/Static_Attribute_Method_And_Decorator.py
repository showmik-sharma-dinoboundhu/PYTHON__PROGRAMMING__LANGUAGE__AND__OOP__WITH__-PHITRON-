class Shopping:
    #This is class attribute or Static attribute
    cart = []                   
    origin = "Chaina"


    def __init__(self,name,location) -> None:
        self.name = name            #instance attributes
        self.location = location    #instance attributes

    def purchase(self,item,price,amount):
        remaining = amount - price
        print(f"Buying {item} for price {price} and remaining {remaining}")

    #Static Method:
    @staticmethod
    def multiply(a,b):
        result = (a*b)
        print(result)

    #Static decorator:
    @classmethod
    def Hudai_Dekhi(self,item):
        print("Hudai dekhi kintu kinmu na just ac er hawa khaite asci",item)


Basundhara = Shopping("Basu", "No popular")
# Basundhara.purchase("Lungi", 500, 2000)
Basundhara.Hudai_Dekhi("lungi")
# Shopping.purchase
Shopping.Hudai_Dekhi("Lungi")

Shopping.multiply(10,30)
Basundhara.multiply(6,8)

