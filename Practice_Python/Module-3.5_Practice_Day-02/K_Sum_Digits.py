l = int(input())
num = int(input())
total = 0

while num > 0:
    rem = num % 10
    total += rem
    num = num // 10

print(total)