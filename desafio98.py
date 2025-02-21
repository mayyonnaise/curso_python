from time import sleep


def linha():
    print('='*43)


def msg1(a1, a2, a3):
    print(f'Contagem de {a1} até {a2} em {a3}.')


def para(x, y, z):
    for contador1 in range(x, y, z):
        print(contador1, end=' ')
        sleep(0.4)


def contador(a, b, c):
    if a < b:
        if c == 0:
            msg1(a, b, '1')
            para(a, b+1, 1)
            print('FIM!')
            linha()
        else:
            msg1(a, b, c)
            para(a, b + 1, c)
            print('FIM!')
            linha()
    elif a > b:
        if c == 0:
            msg1(a, b, '1')
            para(a, b - 1, -1)
            print('FIM!')
            linha()
        elif c < 0:
            msg1(a, b, abs(c))
            para(a, b - 1, c)
            print('FIM!')
            linha()
        else:
            msg1(a, b, abs(c))
            para(a, b - 1, -c)
            print('FIM!')
            linha()


linha()
inicio = 0
fim = 10
passo = 0
contador(inicio, fim, passo)

inicio = 10
fim = 0
passo = 0
contador(inicio, fim, passo)

print('Agora é sua vez de personalizar a contagem!')
inicio = int(input('Início: '))
fim = int(input('Fim: '))
passo = int(input('Passo: '))
linha()
contador(inicio, fim, passo)