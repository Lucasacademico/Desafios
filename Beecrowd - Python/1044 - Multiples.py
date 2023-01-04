'''
Read two nteger values (A and B). After, the program should print the message "Sao Multiplos" 
(are multiples) or "Nao sao Multiplos" (aren’t multiples), corresponding to the read values.

Input
The input has two integer numbers.

Output
Print the relative message to the input as stated above.
'''

a, b = map(int, input().split())
if(b > a):
    if(b % a == 0):
        print('Sao Multiplos')
    elif(b % a != 0):
        print('Nao sao Multiplos')
elif(a > b):
    if(a % b == 0):
        print('Sao Multiplos')
    elif(a % b != 0):
        print('Nao sao Multiplos')
