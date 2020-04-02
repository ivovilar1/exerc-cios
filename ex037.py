numero = int(input('Digite um numero inteiro:'))
print('Escolha uma das bases para conversao:')
print('[ 1 ] converter para binario')
print('[ 2 ] converter para octal')
print('[ 3 ] converter para hexadecimal')
opcao = int(input('Sua opção: '))
if opcao == 1:
    print('o numero {} convertido para binario é : {}'.format(numero, bin(numero)[2:]))
elif opcao == 2:
    print('o numero {} convertido para octal é : {}'.format(numero, oct(numero)[2:]))
elif opcao == 3:
    print(' o numero {} convertido para hexadecimal é : {}'.format(numero, hex(numero)[2:]))
else:
    print('Numero invalido')

