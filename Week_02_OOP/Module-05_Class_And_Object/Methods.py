def call():
    print("I was calling someone")
    return "call done" 


class phone():
    price = 12000
    color = "Fresh Green"
    brand = "Realme"
    charger = "Type-B"
    Features = ['camera','speaker','flashlight','movie']

    def call(self):
        print("Calling one person")

    def send_sms(self,phone,sms):
        text = f"sending msg to: {phone} and message :{sms}"
        return text

my_Phone = phone()
result = my_Phone.send_sms(2342134, "I love you")
print(result)

print(my_Phone,my_Phone.brand,my_Phone.charger,my_Phone.color,my_Phone.Features)



