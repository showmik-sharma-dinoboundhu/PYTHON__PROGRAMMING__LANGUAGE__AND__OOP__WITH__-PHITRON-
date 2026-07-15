na_1 = 'Showmik Sharma'
na_2 = "Showmik Sharma"
na_3 = """Showmik Sharma is my name..
I am here new."""
na_4 = "The one and only programmer here now is Showmik"

print(na_3)
print("\n")

for char in na_1:
    print(char)
print("\n")

print(na_2[4])
print("\n")

print(na_4[::-1])
print("\n")

print(na_1[0:4])
print("\n")

if "Dinoboundhu" in na_1:
    print("Exist")
else:
    print("Not Exist!")
    print("But We can Print: Showmik Sharma Dinoboundhu")
print("\n")

print(na_1.upper())
print(na_1.lower())
print(na_2.capitalize())
print(na_3.count('Showmik'))
print(na_4.swapcase())
print(na_2.index('Showmik'))
print(na_4.title())