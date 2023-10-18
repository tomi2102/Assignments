
#test=["abcdefgh","abcefgh"]
#test=["abcedefgh","abcefgh","abcentfx"] #test array
#test=["w3r","w3resource"]
#test=["Python","PHP", "Perl"]
test=["Python","PHP", "Java"]
index1= 0 #index for letter in string array
index2= 0 #index for item in array
value1=len(test) # length of the array
value2= len(test[0])+1 # length of the first array item
mini = ("")

for index1 in range(0,value2-1):
    for index2 in range(0,value1):
        if test[0][index1] == test[index2][index1]:
            same = True
            index2 +=1
            
        else:
            same = False
            break
    if same:
        mini = mini + test[0][index1]
    else:
        break
    index1 += 1
if mini == "":
    print("There is no common prefix")
    print(same)
else:
    print(mini)