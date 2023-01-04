n1, n2, n3, n4 = map(float, input().split())
media = ((n1*2)+(n2*3)+(n3*4)+(n4*1))/10
print('Media: {:.1f}'.format(media))
if media >= 7.0:
    print('Aluno aprovado.')
elif media < 5.0:
    print('Aluno reprovado.')
elif media >= 5.0 and media < 7.0:
    print('Aluno em exame.')
    recup = float(input())
    print('Nota do exame: {:.1f}'.format(recup))
    final = (recup + media)/2
    if(final >= 5.0):
        print('Aluno aprovado.')
        print('Media final: {:.1f}'.format(final))
    else: 
        print('Aluno reprovado.')
        print('Media final: {:.1f}'.format(final))

    '''
    2.0 4.0 7.5 8.0
    6.4

    2.0 6.5 4.0 9.0

    
    9.0 4.0 8.5 9.0
    '''