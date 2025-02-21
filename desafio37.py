numero = int(input('Digite um numero inteiro: '))
print('Escolha um das bases para conversão: ')
print('[ 1 ] Converter para BINÁRIO ')
print('[ 2 ] Converter para OCTAL ')
print('[ 3 ] Converter para HEXADECIMAL ')
n = int(input('sua opção: '))

binario = bin(numero)[2:]
octal = oct(numero)[2:]
hexa = hex(numero)[2:]

if n == 1:
    print('{} convertido para BINARIO é igual a {}'.format(numero, binario))
elif n == 2:
    print('{} convertido para OCTAL é igual a {}'.format(numero, octal))
elif n == 3:
    print('{} convertido para HEXADECIMAL é {}'.format(numero, hexa))