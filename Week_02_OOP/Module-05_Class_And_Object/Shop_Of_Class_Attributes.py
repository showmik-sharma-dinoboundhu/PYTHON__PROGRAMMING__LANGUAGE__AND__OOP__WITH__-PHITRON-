class Shop:
    cart = []       #Cart is a class atributes

    def __init__(self,buyer):
        self.buyer = buyer

    def add_to_cart(self,item):
        self.cart.append(item)

showmik = Shop("Showmik")
showmik.add_to_cart("Shoes")
showmik.add_to_cart("Phone")
print(showmik.cart)

Devgon = Shop("Devgon")
Devgon.add_to_cart("Cap")
Devgon.add_to_cart("Watch")
print(Devgon.cart)

