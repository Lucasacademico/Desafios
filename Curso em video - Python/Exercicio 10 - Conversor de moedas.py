'''
    Crie um programa que leia quanto dinheiro a pessoa tem na carteira
    e mostre quantos dolares ela pode comprar.
'''

real = float(input('Digite o valor atual da sua carteira: '))
dolar = real / 3.27
print('O valor de R${:.2f} foi convertido para U${:.2f}'.format(real, dolar))