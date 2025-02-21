p1 = int(input('Primeiro Termo: '))
r1 = int(input('Razão: '))

for pa in range(1, 11):
    print(end=f'{p1 + (pa-1)*r1} -> ')
print('ACABOU!')