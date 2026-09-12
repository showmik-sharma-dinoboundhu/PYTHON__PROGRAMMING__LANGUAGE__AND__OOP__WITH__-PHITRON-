num = [10,3,20,5,2,4,78,56]
person_1 = ["Kala Chan", "Kalidaha", 56, "Businessman"]

person = {"Name" : "Showmik Sharma", "Address" : "Kalidaha", "Age" : 22, "Job" : "Student"}
print(person)
print(person_1)
print(person["Job"])
print(person.keys())
print(person.values())

person["lagugage"] = "Python"
print(person)

# Specail Dictonary Looping:
for i in person.items():
    print(i)

if "Age" in person:
    print("Exist")
else:
    print("Not Exist")