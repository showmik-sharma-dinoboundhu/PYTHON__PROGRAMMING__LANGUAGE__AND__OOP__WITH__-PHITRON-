class Shopping:
    cart = []   #This is class attribute or Static attribute
    origin = "Chaina"


    def __init__(self,name,location) -> None:
        self.name = name            #instance attributes
        self.location = location    #instance attributes


    def purchase(self,item,price,amount):
        remaining = amount - price
        print(f"Buying {item} for price {price} and remaining {remaining}")


Basundhara = Shopping("Basu", "No popular")
Basundhara.purchase("Lungi", 500, 2000)
# Shopping.purchase

