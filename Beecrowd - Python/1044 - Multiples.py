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