class Calculator:
    Brand = "Casio Fx 991 es Plus"

    def add(self,n1,n2):
        r = n1 + n2
        return r
    
    def sub(self,n1,n2):
        r = n1 - n2
        return r
    
    def mul(self,n1,n2):
        r = n1 * n2
        return r
    
    def div(self,n1,n2):
        r = int(n2 / n1)
        return r
    
    def mod(self,n1,n2):
        r = n2 % n1
        return r

myCalculator = Calculator()
a_a = myCalculator.add(10,20)
a_s = myCalculator.sub(30,10)
a_m = myCalculator.mul(5,2)
a_d = myCalculator.div(2,10)
a_ml = myCalculator.mod(2,5)

print(myCalculator.Brand)
print(a_a,a_s,a_m,a_d,a_ml)