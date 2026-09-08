class Shop:
    ShoppingMall = "Jamuna"

    def __init__(self,buyer):
        self.buyer = buyer
        self.cart = []

    def add_to_cart(self,items):
        self.cart.append(items)
    
dev = Shop("Dev")
dev.add_to_cart("Water")
dev.add_to_cart("ToothPaste")
dev.add_to_cart("Brash")
print(dev.cart)

Showmik = Shop("showmik")
Showmik.add_to_cart("HaxiSol Hand Rab")
Showmik.add_to_cart("Deo or Scent or Fregnence")
Showmik.add_to_cart("Cup")
print(Showmik.cart)