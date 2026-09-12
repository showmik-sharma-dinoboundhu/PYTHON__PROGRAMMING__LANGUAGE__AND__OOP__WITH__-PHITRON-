num = 1
while num <= 10:
    print(num)
    num += 1
    if(num == 6):    
        break
print("\n")


N = 1
while N <= 10:
    N = N + 1
    if(N % 2 != 0): 
        continue
    print(N)