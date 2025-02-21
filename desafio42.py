a = int(input('Primeiro segmento: '))
b = int(input('segundo segmento: '))
c = int(input('terceiro segmento: '))

primeiro = a + b
segundo = a + c
terceiro = b + c

if primeiro > c and segundo > b and terceiro > a:
    print()
    if a == b == c:
        print('Os segmento acima podem formar um TRANGULO Equilatero')
    elif a == b or a == c or b == c:
        print('Os segmento acima podem formar um TRANGULO Isosceles')
    elif a != b != c:
        print('Os segmento acima podem formar um TRANGULO Escaleno')
else:
    print('Os segmentos nao podem formar um trangulo')