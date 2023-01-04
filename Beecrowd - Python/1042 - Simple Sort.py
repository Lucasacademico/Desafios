'''
Read three integers and sort them in ascending order. After, print these values in ascending order, a 
blank line and then the values in the sequence as they were readed.

Input
The input contains three integer numbers.

Output
Present the output as requested above.
'''

a, b, c = map(float, input().split())
if((a + b > c) and(b + c > a) and (a + c > b)):
    p = a + b + c
    print(f'Perimetro = {p:.1f}')
else:
    tp = ((a+b)*c)/2
    print(f'Area = {tp:.1f}')
