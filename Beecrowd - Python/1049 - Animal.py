'''
Acessar enunciado no site.
'''

tipo = input('')
if tipo == 'vertebrado':
    mamiferoAve = input('')
    if mamiferoAve == 'ave':
        carniOvo = input('')
        if carniOvo == 'carnivoro':
            print('aguia')
        elif carniOvo == 'onivoro':
            print('pomba')
    elif mamiferoAve == 'mamifero':
        oniherbi = input('')
        if oniherbi == 'onivoro':
            print('homem')
        elif oniherbi == 'herbivoro':
            print('vaca')
elif tipo == 'invertebrado':
    anelinseto = input('')
    if anelinseto == 'inseto':
        hemaherbi = input('')
        if hemaherbi == 'hematofago':
            print('pulga')
        elif hemaherbi == 'herbivoro':
            print('lagarta')
    elif anelinseto == 'anelideo':
        hematoni = input('')
        if hematoni == 'hematofago':
            print('sanguessuga')
        elif hematoni == 'onivoro':
            print('minhoca')
