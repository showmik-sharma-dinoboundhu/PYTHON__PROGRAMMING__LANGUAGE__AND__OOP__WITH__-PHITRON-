Boss = True
Coin = "Tail"

if Boss == True:
    print("Come Boss I will do it in a minute")
    if Coin == "Head":
        print("I will Bat First")
    else:
        print("You will Bowl First")
        if(Boss == False and Coin == "Head"):
            print("Let's do nothing")
        elif(Boss == True or Coin == "Head"):
            print("Let's do something big")

else:
    print("Come After Lunch")
