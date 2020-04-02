#Faça um programa que mostre na tela uma contagem regressiva para o estouro de fogos de artificio, indo de 10 ate 0.
#Com uma pausa de 1 segundo entre eles.

from time import sleep

for count in range(10,-1, -1):
    print(count)
    sleep(1)
print('BOOWWW')
