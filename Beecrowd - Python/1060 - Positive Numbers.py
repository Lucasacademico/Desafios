cont = 0
for i in range(0, 6):
    x = float(input())
    if x > 0:
        cont = cont + 1
print('{} valores positivos'.format(cont))