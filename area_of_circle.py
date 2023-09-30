import math

def area_of_circile():
    r=input("Enter the radius of the circule you want to calculate")
    r=float(r)
    area=math.pi*(r**2)
    print("r =",r)
    print("area =",area)
area_of_circile()