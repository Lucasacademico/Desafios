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
