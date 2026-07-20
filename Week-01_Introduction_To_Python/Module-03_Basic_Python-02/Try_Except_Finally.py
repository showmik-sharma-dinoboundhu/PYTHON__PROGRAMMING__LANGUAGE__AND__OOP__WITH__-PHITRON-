try:
    result = 48/0
except:
    print("Error Happenned")
finally:
    print("Finally here!")
print('Done')



try:
    result =20//5
except:
    print("error happened")
finally:
    print("finally here")



from math import *
result=ceil(5.00001)
print(result)


num = lambda a:a*a
print(num(2**2))