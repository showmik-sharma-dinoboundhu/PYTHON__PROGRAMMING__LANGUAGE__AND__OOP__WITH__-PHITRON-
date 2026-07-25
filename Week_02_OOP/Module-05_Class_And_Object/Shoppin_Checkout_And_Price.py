class Shopping:
    def __init__(self,name):
        self.name = name
        self.cart = []
    
    def add_to_cart(self,item,price,quantity):
        product = {"item" : item, "price" : price, "quantity" : quantity}
        self.cart.append(product)

    def checkOut(self,amount):
        total = 0
        for item in self.cart:
            # print(item)
            total += item["price"] * item["quantity"]
        print("total price",total)

        if amount < total:
            return f"Please provide (total - amount) more"
        else:
            extra = amount - total
            print(f"Here is your {extra} money sir!!")



swapan = Shopping("Alen Swapan")
swapan.add_to_cart("Alu",50,6)
swapan.add_to_cart("Egg",12,24)
swapan.add_to_cart("Rice",50,5)

print(swapan.cart)
swapan.checkOut(18600)
