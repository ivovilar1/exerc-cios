print('-='*30)
print('Analisador de triangulos')
print('-='*30)

r1 = float(input('Digite o primeiro segmento :'))
r2 = float(input('Digite o segundo segmento :'))
r3 = float(input('Digite o terceiro segmento :'))
if r1 < r2 + r3 and r2 < r1 + r3 and r3 < r1 + r2:
    print('Os segmentos acima podem formar um triangulo')
else:
    print('Os segmentos acima nao podem formar um triangulo')
