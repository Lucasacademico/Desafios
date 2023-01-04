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