n = int(input())
ar = list(map(int,input().split()))
if ar == ar[: : -1]:
    print("YES")
else:
    print("NO")