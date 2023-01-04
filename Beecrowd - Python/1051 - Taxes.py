
sal = float(input())
if sal >= 0 and sal <= 2000:
    print("Isento")
elif sal > 2000 and sal <= 3000:
    resto = sal - 2000 
    resultado = resto * 0.08
    print('R$ {:.2f}'.format(resultado))
elif sal > 3000 and sal <= 4500:
    resto = sal - 3000
    imposto = resto * 0.18
    resultado = imposto + 1000*0.08
    print('R$ {:.2f}'.format(resultado))
elif sal > 4500:
    resto = sal - 4500
    imposto = resto * 0.28
    resultado = imposto + (1000*0.08) + (1500*0.18)
    print('R$ {:.2f}'.format(resultado))