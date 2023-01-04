'''
    Faça um programa que leia algo pelo teclado e mostre na tela
    o seu tipo primitivo e todas as informações sobre ela.

    As coisas que devemos dissecar:
    - tipo primitivo
    - se tem espaço
    - se é numerico
    - se é alfabetico
    - se é alfanumerico
    - se esta maiusculo
    - se esta minusculo
    - se esta capitalizada
'''

a = input('Digite algo no teclado: ')
print('Tipo primitivo: {}'.format(type(a)))
print('Possui só espaço? {}'.format(a.isspace()))
print('É valor numérico? {}'.format(a.isnumeric()))
print('Faz parte do alfabeto? {}'.format(a.isalpha()))
print('É valor alfanumérico? {}'.format(a.isalnum()))
print('O valor esta maiusculo? {}'.format(a.isupper()))
print('O valor esta minusculo? {}'.format(a.islower()))
print('O valor esta em formato titulo? {}'.format(a.istitle()))