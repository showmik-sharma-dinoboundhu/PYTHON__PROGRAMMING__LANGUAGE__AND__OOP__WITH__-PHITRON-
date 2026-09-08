person = {"Name" : "Showmik Sharma", "Address" : "Kalidaha", "Age" : 22, "Job" : "Student"}
print(person)
print(person.keys())
print(person.values())
for i in person.items():
    print(i)

numbers = [10,3,20,5,2,4,78,56]
for i,num in enumerate(numbers):
    print(i,num)