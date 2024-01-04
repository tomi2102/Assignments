#Write a Python program to check if a specified element appears in a tuple of tuples.
# Original list:
# (('Red', 'White', 'Blue'), ('Green', 'Pink', 'Purple'), ('Orange', 'Yellow', 'Lime'))
# Check if White presenet in said tuple of tuples!
# True
# Check if White presenet in said tuple of tuples!
# True
# Check if Olive presenet in said tuple of tuples!
# False
# please use reduce and lambda function.
from functools import reduce

random_tuple = (('Red', 'White', 'Blue'), ('Green', 'Pink', 'Purple'), ('Orange', 'Yellow', 'Lime'))
colours =('Red', 'White', 'Blue')
print("White" in colours)
check = map (lambda x:"White" in x, random_tuple)
print(list(check))