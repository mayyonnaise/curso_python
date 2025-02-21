numero = int(input('Digite um Numero inteiro: '))
contador = 0
lista = []
#Programa Principal:
for v in range(1, numero+1):
    if numero % v == 0:
        lista.append(v)
        contador += 1

if contador <= 2:
    print(f'é Numero Primo, pois o Numero {numero} é divisivel somente por {lista}')
elif contador > 2:
    print(f'Não é Numero primo, pois o Numero {numero} foi divisivel {len(lista)} vezes {lista}')