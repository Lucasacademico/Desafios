'''
The company ABC decided to give a salary increase to its employees, according to the following table:


Salary	                Readjustment Rate
0  -400.00              15%
400.01 - 800.00         12%
800.01 - 1200.00        10%
1200.01 - 2000.00       7%
Above 2000.00           4%

Read the employee's salary, calculate and print the new employee's salary, as well the money earned and 
the increase percentual obtained by the employee, with corresponding messages in Portuguese, as the below example.
Input
The input contains only a floating-point number, with 2 digits after the decimal point.

Output
Print 3 messages followed by the corresponding numbers (see example) informing the new salary, the among 
of money earned (both must be shown with 2 decimal places) and the percentual obtained by the employee. Note:

Novo salario:  means "New Salary"
Reajuste ganho: means "Money earned"
Em percentual: means "In percentage"
'''

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
