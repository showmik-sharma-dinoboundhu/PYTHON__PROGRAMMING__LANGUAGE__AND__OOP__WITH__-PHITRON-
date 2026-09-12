a = 10
b = 20
sum = a+b
print(sum)
print(type(a),type(b),type(sum))

A = 100
B = 200
sub = (B - A)
print(sub)
print(type(A),type(B),type(sub))

# Multiplication:
c = 20.5
d = 40.2
Mult = (c*d)
print(Mult)
print(type(c),type(d),type(Mult))

# Divisor:
C = 50
D = 8
Div = (C/D)
print(Div)
print(type(C),type(D),type(Div))

# Floor Divison:
e = 50
f = 8
Floor = (e // f)
print(Floor)
print(type(e),type(f),type(Floor))

# Modulas:
E = 40 
F = 7
Mod = (E % F)
print(Mod)
print(type(E),type(F),type(Mod))


# convert string to num:
SS = input("Give me my money: ")
print("Here is your money",SS)
SS_int = int(SS)
print(type(SS),type(SS_int))

SSD = input("Where is my other money?")
print("Here is your money: ",SSD)
SSD_int = int(SSD)
print(type(SSD),type(SSD_int))

print(SSD_int + SS_int, SS_int - SSD_int, SSD_int * SS_int, SS_int / SSD_int, SS_int % SSD_int)
