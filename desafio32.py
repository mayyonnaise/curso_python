ano = int( input('digite um ano qualquer: '))
var = ano % 4
#print('o resultado foi {}'.format(var))
if var == 0:
    print('o ano é bissexto!')
else:
    print('o ano é um ano normal!')