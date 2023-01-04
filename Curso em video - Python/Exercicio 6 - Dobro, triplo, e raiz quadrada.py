'''
    Crie um algoritmo que leia um numero e mostre seu dobro, triplo
    e raiz quadrada
'''

import math
x = float(input('Digite um valor numérico: '))
dobro = x * 2
triplo = x * 3
raiz_q = math.sqrt(x)
print('Dobro: {}'.format(dobro))
print('Triplo: {}'.format(triplo))
print('Raiz Quadrada: {}'.format(raiz_q))