cad = masc = fem = maior18 = menor20 = 0
print('\n')
while True:
    print('-' * 30)
    nome = str(input('Digite seu nome: ')).strip().upper()
    idade = int(input('Idade: '))
    sexo = ' '
    while sexo not in 'MF':
        sexo = str(input('\033[1;38mSexo [\033[1;34mM\033[1;38m/\033[1;31mF\033[1;38m]: \033[m')).strip().upper()[0]
    cont = ' '
    cad += 1
    if idade >= 18:
        maior18 += 1
    if sexo == 'F':
        fem += 1
    if idade < 20 and sexo == 'F':
        menor20 += 1
    if sexo == 'M':
        masc += 1
    while cont not in 'SN':
        cont = str(input('Deseja continuar? [\033[1;36mS\033[1;38m/\033[1;31mN\033[1;38m]: \033[m')).strip().upper()
    if cont == 'N':
        print('\nCADASTROS FINALIZADOS!')
        break
print(f'\nDAS {cad} PESSOAS CADASTRADAS:')
print(f'{maior18} TEM MAIS DE 18 ANOS.')
print(f'{masc} SÃO HOMENS.')
print(f'{fem} SÃO MULHERES, SENDO QUE {menor20} DELAS TEM MENOS DE 20 ANOS .')