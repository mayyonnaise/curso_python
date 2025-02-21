# Dicionário de cores
cores = {
    'branco': '\033[1;39m',
    'fim': '\033[m',
    'ciano': '\033[1;36m',
    'azul': '\033[1;34m',
    'roxo': '\033[1;35m',
    'vermelho': '\033[1;31m',
    'verde': '\033[1;32m',
    'amarelo': '\033[38;5;226m',
    'cinza': '\033[1;37m',
    'rosa': '\033[95m'
}

s = 0 #Somatorio vale 0
print('{} Calcule  soma dos numeros IMPARES multiplos de 3 entre 1 e 500! {}' .format(cores['azul'], cores['fim']))

for number in range(1, 500, 2):
    if number % 3 == 0:
     s += number
print(' ')
print('A soma dos Números impares multiplos de 3 é de: {}'.format(s))