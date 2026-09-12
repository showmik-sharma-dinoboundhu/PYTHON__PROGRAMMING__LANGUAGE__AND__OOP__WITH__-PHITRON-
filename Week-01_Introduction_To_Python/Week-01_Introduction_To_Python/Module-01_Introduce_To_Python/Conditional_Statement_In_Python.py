a = 10
b = 6
if a > b:
    print("a is bigger than b")

else:
    print("b is bigger than a") 

c = input()
d = input()
if c > d:
    print("c is bigger than d")

elif c == d:
    print("Equal")

else:
    print("d is bigger than c")


Boss = False
if Boss is True:
    print("Here you go sir")
else:
    print("Come after lunch break")


# Nested Conditions:
Bosses = True
coin = "Head"
if Bosses == True:
    print("Boss you're joss")
    if coin == "Tail":
        print("I will bat first")
    else:
        print("You will bowl first")
        if(Bosses == True and coin == "Head"):
            print("Do something else")
        elif(Bosses != True or coin == "Head"):
            print("Good bye")


else:
    print("Boss you're fusss")
    