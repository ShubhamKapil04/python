# Program to find area of triangle

# To find area of triangle first we need to find semi-perimeter of triangle

import math 
a = 5
b = 6
c = 7

s = (a+b+c)/2  # Formula for finding semi-perimeter
print('Semi-primeter of triangle is',s)


# To find area of triangle we ha to find sq. root of -(s*(s-a)*(s-b)*(s-c))

area = math.sqrt(s*(s-a)*(s-b)*(s-c))
print("Area of triangle is " ,area)
