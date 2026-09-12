def modarator():
    return(3,4)
print(modarator())

things = 'pen',
Things = "pen","woter botte","pencil","eraser","cutter","charger","lamp","phone","headphone"
print(things)
print(type(things))
print(Things)
print(type(Things))

print(Things[0])
print(Things[-1])
# Slice:
print(Things[1:4])

if "phone" in Things:
    print("YES")
else:
    print("NO")

for i in Things:
    print(i)

print(len(Things))

mega = ([1,3,9], [2,4,6])
print(type(mega))
mega[0][2] = 5
print(mega)