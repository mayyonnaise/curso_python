frase = str(input('Digite uma frase: ')).upper().replace(' ','').strip()
frase2 = frase[::-1]
 
print(f'O inverso da frase {frase} corresponde a {frase2}')
if frase == frase2:
    print('Temos um palindromo')
else:
    print('Temos uma frase normal')