class phone:
    manufractured = "Chaina"

    def __init__(self,owner,brand,price):
        self.owner = owner
        self.brand = brand
        self.price = price

    
    def send_sms(self,phone,sms):
        text = f"I am going send my phone num: {phone} and this sms I am forwarding: {sms}"
        return text

myPhone = phone("Showmik", "Realme", 12000)
print(myPhone.brand,myPhone.owner,myPhone.price)

print(myPhone.send_sms(phone=35445934,sms="Hi!! I am comming...."))

herPhone = phone("She", "Iphone", 120000)
print(herPhone.owner,herPhone.brand,herPhone.price)

dadPhone = phone("Papa", "is using Nokai 108 cuz of you", 5000)
print(dadPhone.owner,dadPhone.brand,dadPhone.price)

