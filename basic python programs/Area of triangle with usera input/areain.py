#Program to find area of trianlge with user input

# To find area of triangle first we need to find semi-perimeter of triangle

import cmath 
a = float(input("Enter the value of first side "))
b = float(input("Enter the value of second side "))
c = float(input("Enter the value of third side "))
# Here float is used because you can input both int value and float Value

s = (a+b+c)/2  # Formula for finding semi-perimeter
print('Semi-primeter of triangle is',s)


# To find area of triangle we ha to find sq. root of -(s*(s-a)*(s-b)*(s-c))

area = cmath.sqrt(s*(s-a)*(s-b)*(s-c))
print("Area of triangle is " ,area)
