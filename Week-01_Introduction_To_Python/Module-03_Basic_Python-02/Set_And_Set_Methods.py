num = [10,3,20,5,2,4,78,56]
print(num)
num_set = set(num)
print(num_set)
num_set.add(48)
print(num_set)
num_set.remove(3)
print(num_set)
for i in num_set:
    print(i)

if 9 in num_set:
    print("9 Exist")
elif 56 in num_set:
    print("56 Exist")
else:
    print("No one Exist")

A = {1,3,5,7}
B = {1,2,3,4,5} 
print(A & B) #A∩B
print(A | B) #AUB