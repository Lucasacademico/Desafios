'''
    Escreva um programa que leia um programa em metros e o exiba convertido em
    centimetros e milimetros
'''

m = float(input('Digite um valor em metros: '))
cm = m * 100
mm = m * 1000
print('Valor em centimetro: {}'.format(cm))
print('Valor em milimetros: {}'.format(mm))