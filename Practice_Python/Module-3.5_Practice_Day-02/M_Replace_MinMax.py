l = int(input())
ar = list(map(int,input().split()))

mx = max(ar)
mn = min(ar)

if ar < ar[: : -1]:
    mx_i = ar.index(mx)
    mn_i = ar.index(mn)
    ar[mn_i], ar[mx_i] = ar[mx_i], ar[mn_i]



print(*ar)
    