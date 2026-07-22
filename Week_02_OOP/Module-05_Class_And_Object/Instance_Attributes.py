class Shop:
    Shoppingmall = "Jamuna"

    def __init__(self,buyer):
        self.buyer = buyer
        self.cart = []      #cart is an instance attributes

    def add_to_cart(self,items):
        self.cart.append(items)

showmik = Shop("Showmik")
showmik.add_to_cart("Shoes")
showmik.add_to_cart("Phone")
print(showmik.cart)

Devdut = Shop("Dev")
Devdut.add_to_cart("Cap")
Devdut.add_to_cart("Watch")
print(Devdut.cart)

Devgon = Shop("Dev")
Devgon.add_to_cart("Glass")
print(Devgon.cart)


