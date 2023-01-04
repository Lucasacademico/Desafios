'''
    Faça um programa que leia um número inteiro qualquer e mostre na
    sua tela a sua tabuada.
'''

valor = int(input('Digite o valor da tabuada: '))
result = 0
for i in range(1, 11):
    result = valor * i
    print('{} x {} = {}'.format(valor, i, result))
