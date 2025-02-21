casa =float(input('Valor do imóvel: R$'))
salario =float(input('Valor do salário: R$'))
anos =int(input('Em quantos anos deseja pagar: '))
parcela = casa / (anos * 12)
if parcela > salario * 0.30:
    print('Para pagar uma casa no valor de R${:.2f} em {} anos, o valor da parcela é R${:.2f} mais juros.'.format(casa, anos, parcela))
    print('Empréstimo NEGADO!')
else:
    print('Para pagar uma casa no valor de R${:.2f} em {} anos, o valor da parcela é R${:.2f} mais juros.'.format(casa, anos, parcela))
    print('Empréstimo APROVADO!')