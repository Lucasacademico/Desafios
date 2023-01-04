
'''
    Faça um programa que leia um valor inteiro e mostre na tela
    seu sucessor e antecessor
'''

x = int(input('Digite um valor inteiro: '))
sucessor = x + 1
antecessor = x - 1
print('Antecessor: {}'.format(antecessor))
print('Sucessor: {}'.format(sucessor))

print()

# Outro método
x = int(input('Digite um valor inteiro: '))
print('Antecessor: {}'.format(x-1))
print('Sucessor: {}'.format(x+1))