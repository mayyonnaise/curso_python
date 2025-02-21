n1 = float ( input ( ' Digite sua primeira nota: ' ) )
n2 = float ( input ( ' Digite sua segunda nota: ' ) )

media = (n1 + n2)/2
print ( f' Sua média final é de: {media:.1f} ' )

if media < 5.0:
    print ( ' Você foi reprovado, estude mais da próxima vez ' )

elif media >= 7.0:
    print ( ' Você aprovado parabéns!! ' )

else:
    print ( ' Você entrou em recuperação, estude para a próxima prova ' )