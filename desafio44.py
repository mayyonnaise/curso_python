valor = float(input('Valor: '))
formas_pagamento = ['[1] - à vista dinheiro/cheque','[2] - à vista cartão','[3] - 2x no cartão','[4] - 3x ou mais no cartão']
print('Formas de pagamento:')
print(formas_pagamento[0])
print(formas_pagamento[1])
print(formas_pagamento[2])
print(formas_pagamento[3])
opcao = int(input(''))
parcelas = 0

if opcao == 1:
    valor_final = valor - (valor * 10/100)
elif opcao == 2:
    valor_final = valor - (valor * 5/100)
elif opcao == 3:
    valor_final = valor
    print('Sua compra de R${:.2f} será parcelada em 2x de R${:.2f} SEM JUROS.'.format(valor,valor_final / 2))
elif opcao == 4:
    parcelas = int(input('Parcelas?(3x ou mais):'))
    valor_final = (valor + (valor * 20 / 100))
    print('Sua compra de R${:.2f} será parcelada em {}x de R${:.2f} COM JUROS.'.format(valor,parcelas,valor_final / parcelas))

if opcao in (1,2,3,4):
    print('Para a opção de pagamento {} o valor R${:.2f} fica por R${:.2f}.'.format(formas_pagamento[opcao-1], valor, valor_final))
else:
    print('Opção inválida!')