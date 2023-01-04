a, b, c = map(float, input().split())

if((a + b > c) and(b + c > a) and (a + c > b)):
    p = a + b + c
    print(f'Perimetro = {p:.1f}')
else:
    tp = ((a+b)*c)/2
    print(f'Area = {tp:.1f}')