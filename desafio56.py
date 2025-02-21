m=int()
mé=int()
im=int()
n1=str()
for c in range (0,4):
    n = input('Nome: ').strip()
    i = int(input('Idade: '))
    s = input('Sexo: ').strip().lower()
    if s == 'm' and i > im:
        n1 = n.capitalize()
        im = i
    mé+=i
    if s == 'f' and i < 20:
        m += 1
print('O nome do homem mais velho é {} com {} anos'.format(n1, im))
print('A média de idade do grupo é de {} anos'.format(mé/4))
print('Há {} mulheres menores de 20 anos'.format(m))