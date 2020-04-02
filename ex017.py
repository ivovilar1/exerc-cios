import math
co = float(input('Qual é o comprimento do cateto oposto?'))
ca = float(input('Qual é o comprimento do cateto adjacente?'))
hip = math.hypot(co,ca)
print('A hipotenusa vai medir {:.2f}'.format(hip))
