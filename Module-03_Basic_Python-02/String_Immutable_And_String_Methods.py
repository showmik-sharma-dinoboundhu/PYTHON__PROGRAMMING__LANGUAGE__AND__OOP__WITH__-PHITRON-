name_1 = 'Showmik Sharma'
name_2 = "Showmik Sharma"
name_3 = """ 
Showmik Sharma
New Programmer
"""
name_4 = 'Showmik\'s a new programmer here' #Escape
print(name_3,"\n",name_1,"\n",name_4,"\n",name_2)


for char in name_2:
    print(char)

print("\n")

print(name_1[3])
print("\n")

print(name_4[0:7])
print("\n")

print(name_3[::-1])

if "Dinoboundhu" in name_1:
    print("Exist")
else:
    print("Showmik Sharma Dinoboundhu")

print(name_1.upper()) #uppare case
print(name_2.lower()) #lower case
print(name_4.title()) #title
print(name_1.swapcase()) #swap tha character
print(name_2.capitalize()) #Capitalized
print(name_3.count('Showmik')) #count how many 
print(name_1.index('Showmik')) #index