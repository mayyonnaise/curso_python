print('\n{:#^60}\n'.format('  Tuplas com Times de Futebol  '))

times = ('', 'Flamengo', 'Santos', 'Palmeiras', 'Gremio', 'Atletico Paranaese-PR',
         'São Paulo-SP', 'Internacional', 'Corinthians - SP', 'Fortaleza EC',
         'Goias', 'Bahia', 'Vasco da Gama', 'Atletico MG', 'Fluminese',
         'Botafogo', 'Ceará', 'Cruzeiro', 'CSA', 'Chapecoense', 'Avaí')

simb = ('-=-' * 30)

print(simb)
print('Lista de times do Brasileirão: ', end='')
print(times[0:5], '\n', times[5:11], '\n', times[11:16], '\n', times[16:20])

print(simb)
print('Os 5 Primeiros são: ', end='')
print(times[0:5])

print(simb)
print('Os 4 últimos são: ', end='')
print(times[16:20])

print(simb)
print(f'Os times em ordem alfabetica: {sorted(times)}')

print(simb)
print(f'O Chapecoense está na {times.index("Chapecoense")}° posição.')