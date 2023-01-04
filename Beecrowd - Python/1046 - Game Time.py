'''
Read the start time and end time of a game, in hours. Then calculate the duration of the game, knowing 
that the game can begin in a day and finish in another day, with a maximum duration of 24 hours. The 
message must be printed in portuguese “O JOGO DUROU X HORA(S)” that means “THE GAME LASTED X HOUR(S)”

Input
Two integer numbers representing the start and end time of a game.

Output
Print the duration of the game as in the sample output.
'''

a, b = map(int, input().split())
tempo = 0
if a < b:
    tempo = b - a
    print(f'O JOGO DUROU {tempo} HORA(S)')
else:
    tempo = b + 24 - a
    print(f'O JOGO DUROU {tempo} HORA(S)')
