'''
Using the following table, write a program that reads a code and the amount of an item. After, print the value to pay. 
This is a very simple program with the only intention of practice of selection commands.

        Code	Specification		Price
        1	    Cachorro Quente		R$ 4.00
        2	    X-Salada		    R$ 4.50
        3	    X-Bacon			    R$ 5.00
        4	    Torrada Simples		R$ 2.00
        5	    Refrigerante		R$ 1.50

Input
The input file contains two integer numbers X and Y. X is the product code and Y is the quantity of this item according to the above table.

Output
The output must be a message "Total: R$ " followed by the total value to be paid, with 2 digits after the decimal point.
'''


x, y = input().split()
x = int(x)
y = int(y)
while x:
    if x == 1:
        price = 4.00
        print('Total: R$ {:.2f}'.format(price*y))
        break
    elif x == 2:
        price = 4.50
        print('Total: R$ {:.2f}'.format(price*y))
        break
    elif x == 3:
        price = 5.00
        print('Total: R$ {:.2f}'.format(price*y))
        break
    elif x == 4:
        price = 2.00
        print('Total: R$ {:.2f}'.format(price*y))
        break
    elif x == 5:
        price = 1.50
        print('Total: R$ {:.2f}'.format(price*y))
        break
    else:
        break
