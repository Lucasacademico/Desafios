'''
Read a value of floating point with two decimal places. This represents a monetary value. After this, calculate 
the smallest possible number of notes and coins on which the value can be decomposed. The considered notes are of 
100, 50, 20, 10, 5, 2. The possible coins are of 1, 0.50, 0.25, 0.10, 0.05 and 0.01. Print the message “NOTAS:” 
followed by the list of notes and the message “MOEDAS:” followed by the list of coins.

Input
The input file contains a value of floating point N (0 ≤ N ≤ 1000000.00).

Output
Print the minimum quantity of banknotes and coins necessary to change the initial value, as the given example.
'''

reais, centavos = input().split('.')
centavos = float(centavos)/100
reais = float(reais)
dinheiro = reais + centavos

notas = [100, 50, 20, 10, 5, 2]
print('NOTAS:')
for n in notas:
    print('{:.0f} nota(s) de R$ {:.2f}'.format((dinheiro//n), n))
    dinheiro = dinheiro % n

moedas = [1, 0.50, 0.25, 0.10, 0.05, 0.01]
print('MOEDAS:')
for m in moedas:
    print('{:.0f} moeda(s) de R$ {:.2f}'.format((dinheiro//m), m))
    dinheiro = (dinheiro % m) + 0.001
