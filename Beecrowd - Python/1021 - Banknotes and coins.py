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
