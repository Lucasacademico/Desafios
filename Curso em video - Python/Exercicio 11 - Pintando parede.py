'''
    Faça um programa que leia a largura e a altura de uma parede em
    metros, calcule a sua área e a quantidade de tinta necessária para
    pintá-la. Sabendo que cada litro de tinta, pinta uma área de 2 m²
'''

larg = float(input('Digite a largura da parede: '))
alt = float(input('Digite a altura da parede: '))
metro_quad = larg * alt
quant_tinta = metro_quad / 2
print('Para {:.2f} metros² é necessário {:.2f} litros de tinta'.format(metro_quad, quant_tinta))