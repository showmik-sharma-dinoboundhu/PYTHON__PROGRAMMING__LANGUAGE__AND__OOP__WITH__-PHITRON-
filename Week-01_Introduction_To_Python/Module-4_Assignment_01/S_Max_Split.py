s = input()

bal = 0
cur = ""
ans = []

for ch in s:
    cur += ch
    if ch == "L":
        bal += 1
    else:
        bal -= 1
    if bal == 0:
        ans.append(cur)
        cur = ""

print(len(ans))
for x in ans:
    print(x)