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
