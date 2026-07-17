num = int(input())
rev = int(str(num)[:: -1])
# print(rev)

if num == rev:
    print(rev,"\nYES")
else:
   print(rev,"\nNO")
