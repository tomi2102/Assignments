import math
## Excercise 1a
#weigth converter from stones and ponds to kilograms
# def weight_imperial_to_metric(stones,pounds):
#     stones = int(stones)
#     pounds = int(pounds)
#     pounds = int((stones * 14) + pounds)
#     kilograms = float(pounds/2.205)
#     kilograms = "{:.2f}".format(kilograms)
#     return kilograms
# #print(weight_converter(20,0)) #check the output is correct

# #distance converter from miles and yards to kilometres
# def distance_imperial_to_metric(miles,yards):
#     miles = int(miles)
#     yards = int(yards)
#     yards = int((miles * 1760) + yards)
#     kilometres = float(yards/1094)
#     kilometres = "{:.2f}".format(kilometres)
#     return kilometres
# #print(distance_converter(20,0)) #check the output is correct

# #liquid measurement converter from gallons and pints to litres
# def liquid_measurement_imperial_to_metric(gallons,pints):
#     gallons = int(gallons)
#     pints = int(pints)
#     pints = int((gallons * 8) + pints)
#     litres = float(pints/1.76)
#     litres = "{:.2f}".format(litres)
#     return litres
# #print(liquid_measurement_converter(20,0)) #check the output is correct

## Excercise 1b
# #weigtht converter from kilograms to stones and pounds
# def weight_metric_to_imperial(kilograms: int):
#     pounds = int(kilograms * 2.205)
#     stones = 0
#     while pounds >= 14:
#         pounds = pounds-14
#         stones += 1
#     return stones,pounds
# print(weight_metric_to_imperial(20)) #check the output is correct

# #distance converter from kilometres to miles and yards
# def distance_metric_to_imperial(kilometres: int):
#     yards = int(kilometres * 1094)
#     miles = 0
#     while yards >= 1760:
#         yards = yards-1760
#         miles += 1
#     return miles, yards
# #print(distance_metric_to_imperial(20)) #check the output is correct

# #lquid measuremnet converter from litres to gallons and pints
# def liquid_measurement_metric_to_imperial(litres: int):
#     pints = int(litres * 1.76)
#     gallons = 0
#     while pints >= 8:
#         pints = pints-8
#         gallons += 1
#     return gallons, pints
# #print(liquid_measurement_metric_to_imperial(20)) #check the output is correct


## Excercise 2
# Converter = input("What are trying to convert? for Distance Enter (D) for Weight enter (W) for Liquid Measurement enter (L) ")
# if Converter == "W" or Converter == "w":
#     pick = input("Are you converting to imperial or metric type (I) or (M) respictevely to choose ")
#     if pick == "I" or pick == "i":
#         kilograms = int(input("Enter a value for kilograms"))
#         stones,pounds = weight_metric_to_imperial(kilograms)
#         print("The convertion of ",kilograms,"kg is ", stones,"st and ",pounds,"lb.")

#     elif pick == "M" or pick == "m":
#         stones = int(input("Enter a value for stones"))
#         pounds = int(input("Enter a value for pounds"))
#         kilograms = weight_imperial_to_metric(stones,pounds)
#         print("The convertion of ",stones,"st and ", pounds,"lb is",kilograms,"kg.")

# elif Converter == "D" or Converter == "d":
#     decide = input("Are you converting to imperial or metric type (I) or (M) respictevely to choose ")
#     if decide == "I" or decide == "i":
#         kilometres = int(input("Enter a value for kilometres"))
#         miles,yards = distance_metric_to_imperial(kilometres)
#         print("The convertion of ",kilometres,"km is ", miles,"mi and ",yards,"yd.")
       
    
#     elif decide == "M" or decide == "m":
#         miles = int(input("Enter a value for miles"))
#         yards = int(input("Enter a value for yards"))
#         kilometres = distance_imperial_to_metric(miles,yards)
#         print("The convertion of ",miles,"mi and ", yards,"yd is",kilometres,"km")


# elif Converter == "L" or Converter == "l":
#     choice = input("Are you converting to imperial or metric type (I) or (M) respictevely to choose ")
#     if choice == "I" or choice == "i":
#         litres = int(input("Enter a value for litres"))
#         gallons,pints =liquid_measurement_metric_to_imperial(litres)
#         print("The convertion of ",litres,"l is ",gallons,"gal and ",pints,"pt.")


#     elif choice == "M" or choice == "m":
#         gallons = int(input("Enter a value for gallons"))
#         pints = int(input("Enter a value for pints"))
#         litres = liquid_measurement_imperial_to_metric(gallons,pints)
#         print("The convertion of ",gallons,"gal and ",pints,"pt is",litres,"l")

# else:
#     print("Lol")

## Excercise 3
# def banana_pricer(banana_weight: int):
#     price = float(0)
#     for x in range(0,banana_weight):
#         price = float(price + 3.00)
#     if price < 50:
#         postage = float(4.99)
#         total_cost = float(price + postage)
#     else:
#         postage = 4.99 - 1.50
#         total_cost = "{:.2f}".format(price + postage)
#     return total_cost


# banana_weight = int(input("What is the weight of your bananas kilos "))
# total_cost = banana_pricer(banana_weight)
# print("The cost of buying aand posting",banana_weight,"kilos of banannas is £", total_cost)


## Excercise 4 
# def training_zone_finder(age=0,heart_rate=0):
#     m = 208 - (0.7 * age)
#     if heart_rate >= 0.9 * m:
#         print('Interval training')
#     elif heart_rate >= 0.7 * m:
#         print('Threshold training')
#     elif heart_rate >= 0.5 * m:
#         print('Aerobic training')
#     else:
#         print('Couch potato')

# user_age = int(input('Enter your age: '))
# user_rate = int(input('Enter your current heart rate: '))
# training_zone_finder(user_age, user_rate)

## Excercise 5 
# def area_of_traingle(a=0,b=0,c=0):
#     semi_perimeter = (a + b + c)/2
#     area = pow(semi_perimeter * (semi_perimeter - a) * (semi_perimeter - b) * (semi_perimeter - c),0.5)
#     area = "{:.2f}".format(area)
#     return area
# a = float(input('Enter the length of the first side of the triangle: '))
# b = float(input('Enter the length of the second side of the triangle: '))
# c = float(input('Enter the length of the third side of the triangle: '))
# print('The area of the triangle is', area_of_traingle(a, b, c))