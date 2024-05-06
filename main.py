from random import randint
maquina = randint(0,50)
print(' Estou pensando em um número... Já sei ')
print(' Adivinhe um número de 0 a 50 ')
acertou = False
palpites = 0

while not acertou and palpites < 15:
    usuário = int(input(' Qual seu palpite?? '))
    palpites = palpites + 1
    if usuário == maquina:
        acertou = True
    else:
        if usuário < maquina:
            print ('chegou perto, chute um pouco mais alto {}'.format(palpites))
        elif usuário > maquina:
            print (' passou, chute mais baixo')
print (' Acetou parabuens, você acertou com {} tentativas'.format(palpites))