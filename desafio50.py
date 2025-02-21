s = 0
count = 0
for c in range (1,7):
    n = int(input(f'Digite {c} numero inteiro: '))
    if n % 2 ==0:
        s = n+c
        count = count+1
print(f'O somatorio dos valores pares fornecidos e: {s}\nA quantidade dos valores pares fornecidos e: {count}.')