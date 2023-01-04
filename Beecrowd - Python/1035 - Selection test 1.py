'''
Read 4 integer values A, B, C and D. Then if B is greater than C and D is greater than A and if the 
sum of C and D is greater than the sum of A and B and if C and D were positives values and if A is 
even, write the message “Valores aceitos” (Accepted values). Otherwise, write the message “Valores 
nao aceitos” (Values not accepted).

Input
Four integer numbers A, B, C and D.

Output
Show the corresponding message after the validation of the values​​.
'''

a, b, c, d = input().split(' ')
a = int(a)
b = int(b)
c = int(c)
d = int(d)

# b > c 
# d > a
# and c + d > a + b 
# and int(c e d)
# and a % 2 = 0

if((c > 0) and (d > 0) and (a % 2==0) and (b > c) and (d > a) and (c+d > a+b)  ):
    print('Valores aceitos')
else:
    print('Valores nao aceitos')
