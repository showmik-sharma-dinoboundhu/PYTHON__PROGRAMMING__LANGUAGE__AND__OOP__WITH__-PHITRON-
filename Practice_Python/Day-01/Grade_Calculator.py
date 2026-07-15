Num = int(input())

if(Num <= 100 and Num >= 80):
    print("A+")
elif(Num <= 79 and Num >= 60):
    print("A")
elif(Num <= 59 and Num >= 40):
    print("B")
elif(Num == 40):
    print("Pass")
else:
    print("Fail")

x = 10
y = 2
print(x // y)