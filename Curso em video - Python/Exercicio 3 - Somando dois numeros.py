'''
    Crie um programa que leia dois números e
    mostre a soma entre elas
'''

x = input('Digite um numero: ')
y = input('Digite outro numero: ')
soma = int(x) + int(y)
print('{} + {} = {}'.format(x, y, soma))

# Outro método
x = int(input('Digite um numero: '))
y = int(input('Digite outro numero: '))
print('{} + {} = {}'.format(x, y, (x+y)))