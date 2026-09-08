class Shop:
    cart = []

    def __init__(self,buyer):
        self.buyer = buyer

    def add_to_cart(self,items):
        self.cart.append(items)
    

showmik = Shop("Showmik")
showmik.add_to_cart("Scale")
showmik.add_to_cart("Eraser,Pencil,Cutter,Board,Pen")
showmik.add_to_cart("Deo,Body-Cream")
print(showmik.cart)

Dinoboundhu = Shop("Dino")
Dinoboundhu.add_to_cart("Cup")
Dinoboundhu.add_to_cart("Oil")
Dinoboundhu.add_to_cart("Hexisol Hand Rub")
print(Dinoboundhu.cart)