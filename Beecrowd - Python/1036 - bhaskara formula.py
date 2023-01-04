'''
Input Samples	    Output Samples
10.0 20.1 5.1       R1 = -0.29788
                    R2 = -1.71212

0.0 20.0 5.0        Impossivel calcular

10.3 203.0 5.0      R1 = -0.02466
                    R2 = -19.68408

10.0 3.0 5.0        Impossivel calcular
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





