# list / Array / collection

#index = 0  1  2  3  4  5  6  7
Numb  = [45, 38, 98, 56, 60, 70, 85, 90]
#index = -8  -7  -6  -5  -4  -3  -2  -1

print(Numb[3],Numb[-3])


# Divide the list: 
# list (start : end)
#It means start from the start index and stops before the end index
print(Numb [2 : 6])


#List (start : end : step)
print(Numb[1 : 8 : 1])
print(Numb[1 : 8 : 2])
print(Numb[8 : 1 : -1])
print(Numb[:])  #short cut to copy a list
print(Numb[4 :])
print(Numb[: 6])
print(Numb[: : -1]) #short cut to reverse