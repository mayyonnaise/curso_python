from random import randint

def sorteio(lista):
    print('Sorteando 5 valores da Lista:', end=' ')

    while len(lista) < 5:
        valores = randint(1, 9)

        if valores not in lista: 
            lista.append(valores)
            print(f'{valores}', end=' ')
    print('PRONTO!')

def somaPar(lista): 
    soma = 0
    for n in lista:
        if n % 2 == 0:
            soma += n
    print(f'Somando todos os valores pares de {lista}, temos {soma}')

numeros = []

sorteio(numeros)
somaPar(numeros)
print()