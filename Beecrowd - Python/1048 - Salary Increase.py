def calc_sal(sal, x):
    reajuste = sal * (x/100)
    novoSal = sal + reajuste
    percentual = x
    print('Novo salario: {:.2f}'.format(novoSal))
    print('Reajuste ganho: {:.2f}'.format(reajuste))
    print('Em percentual: {} %'.format(percentual))
    
sal = float(input())
if sal >= 0 and sal <= 400.00:
    x = 15
    calc_sal(sal, x)
elif sal >= 400.01 and sal <= 800.00:
    x = 12
    calc_sal(sal, x)
elif sal >= 800.01 and sal <= 1200.00:
    x = 10
    calc_sal(sal, x)
elif sal >= 1200.01 and sal <= 2000.00:
    x = 7
    calc_sal(sal, x)
elif sal > 2000.00:
    x = 4
    calc_sal(sal, x)
