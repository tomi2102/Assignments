#########################EXERCISE 1#############################################


# def sum_digits(number):
#     digits = str(number)
#     total = 0
#     for val in digits:
#         total += int(val)
#     return total


# print(sum_digits(1234))
numbers = [1,2,3,4]
sum = 0
addition = [sum := sum + x for x in numbers ]
print(sum)

#########################EXERCISE 2#############################################

# def pairwise_digits(num_a, num_b):
#     number_a = str(num_a)
#     number_b = str(num_b)
#     if len(number_a) > len(number_b):
#         number_a, number_b = number_b, number_a

#     output = ''
#     for index in range(len(number_a)):
#         if number_a[index] == number_b[index]:
#             output += '1'
#         else:
#             output += '0'
#     output += '0'*(len(number_b)-len(number_a))

#     return output
# print(pairwise_digits(5213,9273))


######################### EXERCISE 3 #############################################
#########################    V1: For Loop    ###################################


# def to_base10(binary):
#     decimal = 0
#     binary = str(binary)
#     for index in range(len(binary)):
#         decimal += int(binary[index]) * pow(2, len(binary) - 1 - index)
#     return decimal
# print(to_base10(10010))

# #########################    V2: While Loop  ###################################


# def to_base10b(binary):
#     decimal = 0
#     index = 0
#     binary = str(binary)
#     power = len(binary) - 1
#     while index < len(binary):
#         decimal += int(binary[index]) * pow(2, power)
#         power -= 1
#         index += 1

#     return decimal
# print(to_base10b(1100))

# ######################### EXERCISE 4 ##########################################
# rows = int(input('Enter number of rows: '))

# output = ''
# add_1 = True  # flag to check if we add a 1 (True) or a 0 (False)

# for row in range(rows):
#     # If a row is even, we start with a 1, otherwise with a 0
#     if row % 2 == 0:
#         add_1 = True
#     else:
#         add_1 = False

#     for index in range(row + 1):
#         if add_1:
#             output += '1'
#         else:
#             output += '0'
#         add_1 = not add_1  # change flag from True to False and vice versa

#     output += '\n' 

# print(output)

# ######################### EXERCISE 5 ##########################################
# data = [[1, 2, 3], [2], [1, 2, 3, 4]]


# def sum_lists(list2D):
#     output = []
#     for row in list2D:
#         total = 0
#         for val in row:
#             total += val
#         output.append(total)
#     return (output)


# print(sum_lists(data))
