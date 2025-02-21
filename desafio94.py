dados = {}
galera = []
soma = media = 0 
while True:
    dados.clear()
    # loop inifinito para que o usuário digite apenas letras (NOME).
    while True:
        nome = input('nome: ').title()
        if nome.isalpha():
            dados['nome'] = nome
            break
        else:
            print('Entrada inválida, digite apenas letras.')
    # loop infinito para que o usuário digite apenas M ou F (SEXO).
    while True:
        sexo = input('sexo: [M/F] ').strip().upper()
        if sexo in ('M', 'F'):
            dados['sexo'] = sexo
            break
        else:
            print('Opção inválida. Tente novamente.')
    # aqui faço um loop para o usuário digitar apenas números inteiros (IDADE).
    while True:
        idade = input('idade: ')
        try: 
            idade = int(idade)
            dados['idade'] = idade
            # para fazer a letra B preciso fazer uma váriavel para somar as idades, sai mais fácil que usar o sum()
            soma += dados['idade']
            break

        except ValueError:
            print('Digite apenas números')
    # faço uma copia de cada dicionario para dentro de uma lista
    galera.append(dados.copy())
    # loop infinito para resposta de Sim ou Não 
    while True:
        resp = input('Deseja continuar? [SIM/NÃO]: ').upper().strip()[0]
        # se resp = S ou N ele vai sair desse loop e descer pra linha 45
        if resp in 'SN':
            break
        print('Responda apenas S ou N.')
    # aqui quebro o primeiro loop (linha 10)
    if resp == 'N':
        break
# A
print(f'Foram cadastradas {len(galera)} pessoas.')
# B
media = soma / len(galera)
print(f'A média de idade é {media} anos ')
# C
print('As mulheres cadastradas foram ', end='')
for p in galera:
    if p['sexo'] == "F":
        print(f'{p["nome"]}', end='')
print()
# D
print('Lista das pessoas que estão acima da média', end='')
for p in galera:
    if p['idade'] >= media:
        print(f'{p["nome"]}',end='')