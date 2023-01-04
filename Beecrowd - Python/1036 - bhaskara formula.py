'''
Read 3 floating-point numbers. After, print the roots of bhaskara’s formula. If it's impossible to 
calculate the roots because a division by zero or a square root of a negative number, presents the 
message “Impossivel calcular”.

Input
Read 3 floating-point numbers (double) A, B and C.

Output
Print the result with 5 digits after the decimal point or the message if it is impossible to calculate.
'''

import math
a, b, c = input().split()
a = float(a)
b = float(b)
c = float(c)

delta = (b**2) - 4 * a *c

if(a > 0 and delta >= 0) :
    x = (-b + math.sqrt(delta))
    y = (-b - math.sqrt(delta))
    z = 2*a
    r1 = (x)/(z)
    r2 = (y)/(z)
    print('R1 = {:.5F}'.format(r1))
    print('R2 = {:.5F}'.format(r2))
else:  
    print('Impossivel calcular')





