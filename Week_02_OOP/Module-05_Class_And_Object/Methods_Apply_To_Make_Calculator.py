class Calculator:
    brand = "Casio 991 es Plus"

    def add(self,num1,num2):
        result = num1 + num2
        return result
    
    def sub(self,num1,num2):
        result = num1 - num2
        return result
    
    def mul(self,num1,num2):
        result = num1 * num2
        return result
    
    def div(self,n1,n2):
        r = int(n1 / n2)
        return r
    
    def mod(self,n1,n2):
        r = int(n1 % n2)
        return r
    
    
my_calculator = Calculator()
ans_add = my_calculator.add(10,20)
ans_sub = my_calculator.sub(40,20)
ans_mul = my_calculator.mul(5,2)
a_div = my_calculator.div(10,2)
a_m = my_calculator.mod(5,2)

print(my_calculator.brand)
print(ans_add)
print(ans_sub)
print(ans_mul)
print(a_div)
print(a_m)
    