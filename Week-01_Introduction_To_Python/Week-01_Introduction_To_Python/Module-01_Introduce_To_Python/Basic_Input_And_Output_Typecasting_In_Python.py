print("Now I need money")
input("What is the amout of money you lend from me: ")


# Smart way:
Money = input("Give me some money: ")
print("Here is your money",Money)

# Begging way:
First_Money = input("Dosto kichu taka de: ")
print("Taka ney dhor",First_Money)

Second_Money = input("Excuse me! Can I get back my mone?")
print("Ei nao tmr tk: ",Second_Money)

Total = (First_Money + Second_Money)
print(Total);
# class string tai sum hoy nai.

Int_1 = int(First_Money)
Int_2 = int(Second_Money)
Sum = Int_1 + Int_2
print(Sum)

print(type(Money),type(First_Money),type(Second_Money),type(Total))

print("Very common, Hello World!")