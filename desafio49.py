Num = int(input('Digite o número que você deseja saber a tabuada: '))

print(('----------------------------'))
for Tabuada in range (1, 11 ):
    resultado = Tabuada * Num
    print(Tabuada , '*', Num,'=', resultado )
print(('----------------------------'))