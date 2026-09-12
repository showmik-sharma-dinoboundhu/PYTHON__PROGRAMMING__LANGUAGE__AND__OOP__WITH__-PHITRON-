def Full_name(first,last):
    name = f'{first} {last}'
    return name

Name = Full_name('Alu','Kodu')
print(Name)

def surname(first,last,title,additional_name):  
    names = f'{title} {first} {last}'
    # for key, value in additional_name.items():
        # print(key,value)
    print(additional_name)
    return names
Names = surname(first='showmik',last='sharma',title='Mohajon',additional_name="Devdut, Devgon, Dinoboundu, Dingon")
print(Names)

def A_lot(n1,n2):
    sum = n1 + n2
    min = n1 - n2
    mul = n1 * n2
    div = n1 / n2
    mod = n1 % n2
    return [sum,min,mul,div,mod]
    # return sum,min,mul,div,mod
total = A_lot(100,20)
print(total)