num = int(input('Informe um numero: '))
u = num // 1 % 10
d = num // 10 % 10
c = num // 100 % 10
m = num // 1000 %10
print('Unidade é: {}'.format(u))
print('Dezena é: {}'.format(d))
print('Centena é: {}'.format(c))
print('Milhar é: {}'.format(m))
