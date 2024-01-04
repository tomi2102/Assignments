dict1 = {}
for x in range (0,6):
    name=(input("Enter a name of a student"))
    name = str(name)
    scores=(input("Enter their score"))
    scores = int(scores)
    dict1.update({name:scores})
print(dict1)
dict(sorted(dict1.items))
    