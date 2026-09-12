num = 1
while num <= 20:
    print(num)
    num += 1
    if num == 12:
        break
print("\n")

N = 0
while N <= 40:
    N = N + 1
    if (N % 2 != 0):
        continue
    print(N)