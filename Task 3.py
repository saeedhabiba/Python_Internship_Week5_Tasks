import math

def calculate_area(radius):
    return math.pi * radius * radius

#taking input from user
radius = float(input("Enter the radius of the circle: "))
print("Area of the circle is:", calculate_area(radius))