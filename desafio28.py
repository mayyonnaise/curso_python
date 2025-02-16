from random import randint
from time import sleep
computador = randint(0, 5)
print('-=-' * 20)
print('vou pensar em um número entre 0 e 5. Tente adivinhar...')
jogador = int(input('em que numero eu pensei? '))
print('PROCESSANDO...')
sleep(3)
if jogador == computador:
    print('PARABÉNS! Você conseguiu me vencer!')
else:
    print('GANHEI! eu pensei no número {} e não no {}!'.format(computador, jogador))