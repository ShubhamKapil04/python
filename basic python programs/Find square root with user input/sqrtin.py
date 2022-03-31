#program for finding square root with user input

#to solve math problems we use 'import math'- for posite number and 'import cmath'- for complex number


import math #for positive numbers
x = input('enter the value')

root = int(x)
print(math.sqrt(root))


import cmath #for complex numbers
y= input('enter the value')
root = complex(y)
print(cmath.sqrt(root))