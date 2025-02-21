from datetime import date
ano = date.today().year
data = int ( input ( ' Digite o ano que você nasceu: ' ) )
calculo = ano - data

print ( f' Você tem {calculo} anos ' )

if calculo <= 9:
    print ( ' Você se encaixa na categoria MIRIM ' )

elif calculo <= 14:
    print ( ' Você se encaixa na categoria INFANTIL ' )

elif calculo <= 19:
    print ( ' Você se encaixa na categoria JUNIOR ' )

elif calculo <= 20:
    print ( ' Você se encaixa na categoria SÊNIOR ' )

else:
    print ( ' Você se encaixa na categoria MASTER ' )