Num = [10,55,65,77,85,105,15,45,87,66,88,58,90,34,14,26]
odd = []
even = []
cnt = 0
Cnt_O = 0
Cnt_E = 0
for num in Num:
    cnt += 1
    if(num % 2 != 0 and num % 5 == 0):
        odd.append(num)
        Cnt_O += 1
    elif(num % 2 == 0):
        even.append(num)
        Cnt_E += 1

print("Total Num: ",cnt)
print("First Option :",odd,Cnt_O)
print(even,Cnt_E)

#Optional:
Odd_Num = [num for num in Num if(num % 2 != 0 and num % 5 == 0)]
print("Second Option :",Odd_Num)

