n = int(input())
arr = list(map(int, input().split()))
mx = max(arr)
mn = min(arr)
# # print(mx,mn)
for i in arr :   
    mn_i = arr.index(mn)
    mx_i = arr.index(mx)
    arr[mn_i],arr[mx_i] = arr[mx_i],arr[mn_i]

print(*arr)