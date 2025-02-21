def escreva(txt):
    t = len(txt) + 4
    print('~' * t)
    print(f'{txt:^{t}}')
    print('~' * t)


escreva('Gustavo Guanabara')
escreva('Curso de python no youtube')
escreva('CeV')