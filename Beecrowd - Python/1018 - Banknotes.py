'''
In this problem you have to read an integer value and calculate the smallest possible 
number of banknotes in which the value may be decomposed. The possible banknotes are 100, 
50, 20, 10, 5, 2 e 1. Print the read value and the list of banknotes.

Input
The input file contains an integer value N (0 < N < 1000000).

Output
Print the read number and the minimum quantity of each necessary banknotes in Portuguese 
language, as the given example. Do not forget to print the end of line after each line, 
otherwise you will receive “Presentation Error”.
'''


n = int(input())
print(n) #576

print("{} nota(s) de R$ 100,00".format(int(n/100)))#5

aux = (n%100) #76
print("{} nota(s) de R$ 50,00".format(int(aux/50)))#1

aux = (aux%50) #26
print("{} nota(s) de R$ 20,00".format(int(aux/20)))#1

aux = (aux%20) #6
print("{} nota(s) de R$ 10,00".format(int(aux/10)))#0

aux = (aux%10) #0
print("{} nota(s) de R$ 5,00".format(int(aux/5)))#1

aux = (aux%5) #1
print("{} nota(s) de R$ 2,00".format(int(aux/2)))#0

aux = (aux%2) #0
print("{} nota(s) de R$ 1,00".format(int(aux/1)))#1