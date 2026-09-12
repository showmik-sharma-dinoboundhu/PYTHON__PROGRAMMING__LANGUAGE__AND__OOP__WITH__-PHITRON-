""" C or C++ we use for loop array declair then input then output like-for(int i=0;i<=20;i++) """
""" Pythone """

Numbers = [2,4,6,8,10,12,14,16,18,20]
sum = 0
for num in Numbers:
    print(num)
    sum = sum + num
    if(sum > 20):
        print("Bigger value than 20")

print("\n")
print(sum)
    

# String:
text = "Pagle Haowa"
for char in text :
    print(char)
print("\n")

# Range:
print(range(1,10))
for i in range(0,10):
    print(i)
print("\n")

for j in range(0,10,2):
    print(j)

friends = ["Showmik","Devdut","Devgon","Dinoboundhu","Dingon"]
for friend in friends:
    print(friend)