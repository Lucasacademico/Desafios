a, b = map(int, input().split())
tempo = 0
if a < b:
    tempo = b - a
    print(f'O JOGO DUROU {tempo} HORA(S)')
else:
    tempo = b + 24 - a
    print(f'O JOGO DUROU {tempo} HORA(S)')