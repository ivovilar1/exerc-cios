numero = int(input('Me diga um numero qualquer :'))
resultado = numero % 2    # o resto de qualquer divisao de um numero par é sempre 0 e de um numero impar é 1
if resultado == 0:
    print('o numero {} é par'.format(numero))
else:
    print(' o numero é impar'.format(numero))
