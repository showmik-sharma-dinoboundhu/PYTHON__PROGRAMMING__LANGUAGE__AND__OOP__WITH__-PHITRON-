def sum(num1,num2):
    result = num1 + num2
    return result
total = sum(88,84)
print("Total =",total)

# Jodi optional value use korte chai mon chaile jog kolrlam na hole koram na-
def Summ(N1,N2,N3 = 0,N4 = 0):
    Result = N1 + N2 + N3 + N4
    return Result
Total = Summ(80,82,88)
print(Total)

# Jodi N Times value hoy: Then we use Args:
def All_sum(*numbers):
    print(numbers)
    sum = 0
    for num in numbers:
        print(num)
        sum += num
    print("Sum =",sum)
    return All_sum

Totall = All_sum(43,45,60,80,39,59)
print(Totall)

# First 2 ta store kore rekhe:
def All_summ(num1,num2,*args):
    print(args)
    sums = 0
    for num in args:
        print(num)
        sums += num
    print("Sums =",sums)
    return All_summ

Totally = All_summ(43,45,60,80,39,59)
print(Totally)

