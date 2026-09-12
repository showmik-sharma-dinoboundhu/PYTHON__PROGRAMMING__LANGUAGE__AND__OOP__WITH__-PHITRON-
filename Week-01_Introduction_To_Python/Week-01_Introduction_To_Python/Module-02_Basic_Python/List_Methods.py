Num = [10,30,40,20,50,60,70,80]
Num.append(90)
print("Append (90) :",Num)

Num.insert(2,100)
print("Insert (100) :",Num)

Num.remove(40)
print("Remove value :",Num)

#for error Handle to remove:
if 8 in Num:
    Num.remove(8)
if 50 in Num:
    Num.remove(50)
print(Num)

Num.pop()
print("Pop of Last Index :",Num)

Num.index(70)
print("Index Num :",Num)
