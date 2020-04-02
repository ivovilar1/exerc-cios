import math
angulo = float(input('Digite um angulo:'))
s = math.sin(math.radians(angulo))
c = math.cos(math.radians(angulo))
t = math.tan(math.radians(angulo))
print('O angulo de {} tem o seno de {:.2f}'.format(angulo, s))
print('O angulo de {} tem o cosseno de{:.2f}'.format(angulo, c))
print('O angulo de {} tem a tangente de {:.2f}'.format(angulo, t))