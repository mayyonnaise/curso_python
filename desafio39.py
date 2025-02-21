print("Alistamento militar!")
nascimento = int(input("Digite seu ano de nascimento:  "))
ano_atual = 2025 - nascimento
idade = ano_atual - nascimento
alistamento = 18
objetivo = 18 - idade
saldo = ano_atual + objetivo
print("Quem nasceu em {} tem {} anos em 2025 ".format(nascimento, ano_atual))
if ano_atual == 18:
  print("Você tem exatamente {}, precisa fazer o alistamento! ".format(ano_atual))
elif ano_atual > 18:
    print("Você ja deveria ter se alistado a {} ano. ".format(ano_atual - alistamento))
elif ano_atual < 18:
  print("Você é menor de idade!")
  print("Seu alistamento será em: {} ".format(saldo))