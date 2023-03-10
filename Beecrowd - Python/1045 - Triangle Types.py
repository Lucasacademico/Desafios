'''
Read 3 double numbers (A, B and C) representing the sides of a triangle and arrange them in decreasing 
order, so that the side A is the biggest of the three sides. Next, determine the type of triangle that 
they can make, based on the following cases always writing an appropriate message:

if A ≥ B + C, write the message: NAO FORMA TRIANGULO
if A2 = B2 + C2, write the message: TRIANGULO RETANGULO
if A2 > B2 + C2, write the message: TRIANGULO OBTUSANGULO
if A2 < B2 + C2, write the message: TRIANGULO ACUTANGULO
if the three sides are the same size, write the message: TRIANGULO EQUILATERO
if only two sides are the same and the third one is different, write the message: TRIANGULO ISOSCELES

Input
The input contains three double numbers, A (0 < A) , B (0 < B) and C (0 < C).

Output
Print all the classifications of the triangle presented in the input.
'''

a, b, c = map(float, input().split())
lista = [a, b, c]
lista.sort(reverse=True)
a = lista[0]
b = lista[1]
c = lista[2]
if (a >= (b + c)):
    print("NAO FORMA TRIANGULO")
elif ((a**2) < (b**2) + (c**2)):
    print("TRIANGULO ACUTANGULO")
    if(a == b and a == c and b == c):
        print("TRIANGULO EQUILATERO")
    elif(a == b or a == c or b == c):
        print("TRIANGULO ISOSCELES")     
elif ((a**2) == (b**2) + (c**2)):
    print("TRIANGULO RETANGULO")
    if(a == b and a == c and b == c):
        print("TRIANGULO EQUILATERO")
    elif(a == b or a == c or b == c):
        print("TRIANGULO ISOSCELES")     
elif ((a**2) > (b**2) + (c**2)):
    print("TRIANGULO OBTUSANGULO")
    if(a == b and a == c and b == c):
        print("TRIANGULO EQUILATERO")
    elif(a == b or a == c or b == c):
        print("TRIANGULO ISOSCELES")     
