amarelo, ciano = '\033[33m', '\033[36m'
azul, verde = '\033[1;34m', '\033[0;32m'
error, lim = '\033[4;31m', '\033[m'

print(f'{amarelo}={ciano}–' * 28)
print(f'{ciano}{"Lojas Silva":^56}')
print(f'{amarelo}={ciano}–' * 28)

custo_total = 0
mais_1k = 0

while True:
  nome = input(f'\n{azul}Digite o nome do produto:{lim} ')
  preço = float(input(f'{azul}Digite o valor do produto:{lim} R$'))
  custo_total += preço
  if preço > 10**3:
    mais_1k += 1
  if custo_total == preço:
    mais_barato = [nome, preço]
  else:
    if preço < mais_barato[1]:
      mais_barato = [nome, preço]
  
  while True:
    confirm = input(f'{azul}Deseja continuar? [S/N]:{lim} ').upper()[0]
    if confirm in ['S', 'N']:
      break
    else:
      print(f'{error}Dados inválidos! Por favor, tente novamente.')
  if confirm == 'N':
    break
print(f"""{verde}O custo total foi R${custo_total:.2f}
O total de produtos com valor acima de R$1000.00 foi {mais_1k}
O produto mais barato comprado foi {mais_barato[0]}
""", end=lim)