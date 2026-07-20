# Normal Function:
print("Normal :")

def double(x):
    return x * 2
d_r = double(44)
print(d_r)

def square(x):
    return x*x
s_r = square(10)
print(s_r)

def add(x,y,z):
    return x+y+z
a_r = add(100,60,80)
print(a_r)





# Advance Lamda Funtion:
print("Advance-Lamda :")

Ad_Double = lambda num : num * 2
Ad_d = Ad_Double(55)
print(Ad_d)

Ad_Square = lambda num : num * num
Ad_s = Ad_Square(12)
print(Ad_s)

Ad_add = lambda a,b,c,d : a + b + c + d
Ad_a = Ad_add(180,260,200,360)
print(Ad_a)

num = [10,3,20,5,2,4,78,56]
# arr_num = map(double,num)
arr_num = map(lambda x : x*2, num)
arr_s_n = map(lambda x : x ** 2, num)

print(num)
print(list(arr_num))
print(list(arr_s_n))


actors = [
    {"Name" : "Sabila Nur", "Age" : 31},
    {"Name" : "Mumtahina", "Age" : 35},
    {"Name" : "Mehjabin", "Age" : 35},
    {"Name" : "Safa kabir", "Age" : 31},
    {"Name" : "Tasniya Farin", "Age" : 31},
    {"Name" : "Bidya Saha Mim", "Age" : 33}
]

juniors = filter(lambda actor : actor["Age"] < 32, actors)
print(list(juniors))

