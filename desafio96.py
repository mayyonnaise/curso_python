def area(larg, comp):
    x = larg * comp
    print(f'A área de um terreno de {larg} x {comp} é de {x}m².')

# Programa principal
print('Controle de Terrenos')
print('-*' * 10)
area(larg=float(input('LARGURA: ')), comp=float(input('COMPRIMENTO: ')))