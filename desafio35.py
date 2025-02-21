print('-='*20)
print('ANALISADOR DE TRIÂNGULOS')
print('-='*20)
p = float(input('digite o valor do primeiro segmento: '))
s = float(input('digte o valor do segundo segmento: '))
t = float(input('digite o valor do terceiro segmento: '))

if p < s + t and s < p + t and t < p + s:
    print('É possível formar um triângulo')
    if p == s == t:
        print('o triângulo gerado é EQUILÁTERO')
    elif p == s or p == t or s == t:
        print('O triângulo gerado é ISÓCELES')
    else:
        print('o Triângulo é ESCALENO')
else:
    print('Não é possível formar um triângulo')