A, B = map(int, input().split())

found = False

for i in range(A, B + 1):
    lucky = True

    for digit in str(i):
        if digit != '4' and digit != '7':
            lucky = False
            break

    if lucky:
        print(i, end=" ")
        found = True

if not found:
    print(-1)