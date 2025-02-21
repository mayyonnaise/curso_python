matriz = []
numero = []

for c1 in range(0, 3):
    for c2 in range(0, 3):
        numero.append(int(input(f'valor para posição [{c1, c2}]: ')))
    matriz.append(numero[:])
    numero.clear()

print('-'*23, end='')
for c1 in range(0, 3):
    print()
    for c2 in range(0, 3):
        print(f'  [{matriz[c1][c2]:^3}]', end='')
print()
print('-'*23)