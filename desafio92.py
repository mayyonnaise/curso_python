pessoa = {}
pessoa['Nome'] = str(input('Nome: ')).capitalize().strip()
dataNascimento = int(input('Digite o ano de nascimento: '))
idade = 2025 - dataNascimento
pessoa['Idade'] = idade
pessoa['Gênero'] = str(input('Digite o gênero: ')).upper().strip()
pessoa['CTPS'] = str(input('N° da Carteira de Trabalho (Digite "0" se não possuir): '))
if pessoa['CTPS'] != 0:
    anoContracao = int(input('Digite o ano da primeira contratação: ' ))
    if pessoa['Gênero'] == 'F':
        aposentadoria = (anoContracao + 30) - dataNascimento
    else:
        aposentadoria = (anoContracao + 35) - dataNascimento
    pessoa['Aposentadoria'] = aposentadoria
for k, l in pessoa.items():
    print(f'O valor {k} é: {l} ')