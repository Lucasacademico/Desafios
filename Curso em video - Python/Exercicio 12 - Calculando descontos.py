'''
    Faça um algoritmo que leia o preço de um produto e mostre seu
    novo preço. com 5% de desconto.
'''

valor_prod = float(input('Digite o preço do produto: '))
desconto = (valor_prod*5)/100
print('O produto com valor de R${} foi aplicado desconto de 5%, '
      'logo o valor ficou em R${}'.format(valor_prod, valor_prod - desconto))