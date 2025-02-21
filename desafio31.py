km = int(input('Digite a distância em KM: '))
if km <=200:
    print(f'Sua viagem custará: R${km*0.50} reais.')
else:
    print(f'Sua viagem custará: R${km*0.45} reais.')