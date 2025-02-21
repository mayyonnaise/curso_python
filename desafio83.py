expressao = str(input('Digite sua espressao: '))

aberto = expressao.count('(')
fechado = expressao.count(')')

if aberto != fechado:
    print('Expressão INVÁLIDA...')
else:
    print('Expressão VÁLIDA...')