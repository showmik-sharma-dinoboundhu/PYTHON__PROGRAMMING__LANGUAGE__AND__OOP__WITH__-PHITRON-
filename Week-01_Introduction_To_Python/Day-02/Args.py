def defaultt(*args):
    print(args)
    sum = 0
    for i in args:
        sum += i
    print(sum)
    return defaultt
Total = defaultt(10,30,20,40,50,60)
print("Totally :",Total)