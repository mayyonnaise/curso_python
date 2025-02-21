import random
n1=int(input('Pedra=1\nTesoura=2\nPapel=3\n'))
l=[1,2,3]
sorteio=random.choice(l)
if n1==1:
    print('Jogador: Pedra')
elif n1==2:
    print('Jogador: Tesoura')
elif n1==3:
    print('Jogador:  Papel')
if sorteio==1:
    print('CPU: Pedra')
elif sorteio==2:
    print('CPU: Tesoura')
elif sorteio==3:
    print('CPU:  Papel')
if sorteio==1 and n1==3:
    print('Jogador venceu')
elif sorteio == 2 and n1 == 1:
        print('Jogador venceu')
elif sorteio == 3 and n1 == 2:
        print('Jogador venceu')
elif sorteio==n1:
    print('Empate')
else:print('CPU Venceu')