
'''
Make a program that reads 3 integer values and present the greatest one followed by the 
message "eh o maior". Use the following formula:

AB = (a + b + abs(a - b)) / 2

Input
The input file contains 3 integer values.

Output
Print the greatest of these three values followed by a space and the message “eh o maior”.
'''
a, b, c = input().split()
a = int(a)
b = int(b)
c = int(c)
formula1 = (a + b + abs(a - b))/2
formula2 = (formula1 + c + abs(formula1 - c))/2

print(f'{formula2:.0f} eh o maior')