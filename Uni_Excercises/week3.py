# #Excercise 1
# original_phrase = input("Enter any word or phrase to find out if it is a Palindrome ")
# phrase = original_phrase.lower()
# phrase = phrase.replace(" ", "")
# phrase = phrase.replace("'", "")
# phrase = phrase.replace(",", "")
# phrase = phrase.replace(".", "")
# phrase = phrase.replace("!", "")

# length_of_phrase = len(phrase)
# reverse_phrase = ""
# x = length_of_phrase - 1
# while x >=0:
#     reverse_phrase = reverse_phrase + phrase[x]
#     x=x-1
# #print(reverse_phrase) #check if the phrase is reversed
# if phrase == reverse_phrase:
#     print("The phrase '"+original_phrase+"' is a Palindrome.")
# else:
#     print("The phrase '"+original_phrase+"' is not a Palindrome.")





# Excercise 2a
#phrase_from_user = input("Enter a phrase")
phrase_from_user = 'this is a SHORT sentence'
output_phrase = phrase_from_user.replace(" ","")
print(output_phrase)



# Excercise 2b
phrase_length = len(phrase_from_user)
a = phrase_from_user.split()
a_length = len(a) - 1
x = 1
output_phrase1 = a[0].capitalize()
while x <= a_length:
    output_phrase1 = output_phrase1 + a[x].capitalize()
    x = x+1
print(output_phrase1)



# Excercise 2c
phrase_from_user1 = "ThisIsAShortSentence"
phrase_length2 = len(phrase_from_user1)
comprasim = phrase_from_user1.lower()
new_string = ""
for x in range(0,phrase_length2):
    if phrase_from_user1[x] == comprasim[x]:
        new_string = new_string + phrase_from_user1[x]
    else:
        new_string = new_string + " " + phrase_from_user1[x]
output_phrase2 = new_string.split()
print(output_phrase2)



# Excercise 3 -> Not sure.













