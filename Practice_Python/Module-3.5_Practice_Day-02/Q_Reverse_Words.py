l = input()

words = l.split()

for word in words :
    print(word[::-1],end = " ")

