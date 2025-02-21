def maior(*num):
    print('-=-' * 15)
    print('Analisando os valores passados...')
    cont = 0
    for c in num:
        cont += 1
    if cont > 0:
        m = max(num)
    else:
        m = 0
    print(f'{num} Foram informados {cont} valores ao todo.')
    print(f'O maior valor informado foi {m}.')


maior(2, 9, 4, 5, 7, 1)
maior(4, 7, 0)
maior(1, 2)
maior(6)
maior()