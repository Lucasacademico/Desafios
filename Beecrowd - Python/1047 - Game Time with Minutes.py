'''
Read the start time and end time of a game, in hours and minutes (initial hour, initial minute, final 
hour, final minute). Then print the duration of the game, knowing that the game can begin in a day and 
finish in another day,

Obs.: With a maximum game time of 24 hours and the minimum game time of 1 minute.

Input
Four integer numbers representing the start and end time of the game.

Output
Print the duration of the game in hours and minutes, in this format: “O JOGO DUROU XXX HORA(S) E YYY MINUTO(S)” . 
Which means: the game lasted XXX hour(s) and YYY minutes.
'''

hi, mi, hf, mf = list(map(int, input().split()))
dif = ((hf*60+mf) - (hi*60+mi))
if dif <= 0:
    dif+=24*60
    hora = dif//60
    minuto = dif%60
    print("O JOGO DUROU {} HORA(S) E {} MINUTO(S)".format(hora, minuto))
else:
    hora = dif//60
    minuto = dif%60
    print("O JOGO DUROU {} HORA(S) E {} MINUTO(S)".format(hora, minuto))
