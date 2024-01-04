def addition(*number):
    sum = 0
    for x in number:
        sum = sum + x
    return sum







def max_value(*number):
    maximum_value = max(number)
    return maximum_value




def average(*number):
    sum = 0
    for x in number:
        sum = sum + x
    divisor = len(number)
    mean = sum / divisor
    return mean