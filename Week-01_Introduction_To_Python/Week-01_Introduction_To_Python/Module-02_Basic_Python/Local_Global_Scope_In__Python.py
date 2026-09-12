# Global veriable:
balance = 20000

# Local Scope Variable:
def buy_Things(item, price):
    Dream_Phone = "Xphone"
    global balance
    print(f"Previous Balance Value: ",balance)
    balance = balance - price
    print(f'Balance After Buying {item}', balance)

buy_things = ("Sunglass",1000)
print("Global Balance After Buying: ",balance)