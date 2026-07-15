def double_it(num):
    result = num * 2
    print(result)
    return result
double_it(100)

def sum_it(num1,num2):
    sum = num1 + num2
    print(sum)
    return sum_it
total = sum_it(50,80)

final = double_it(total)
print("Final value",final)
    