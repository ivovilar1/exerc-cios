from random import randint
from time import sleep
itens = ('Pedra', 'Papel', 'Tesoura')
computador = randint(0, 2)
print(''' Suas opções:
[ 0 ] PEDRA
[ 1 ] PAPEL
[ 2 ] TESOURA''')
jogador = int(input('Qual é a sua jogada?'))
print('JO')
sleep(1)
print('KEN')
sleep(1)
print('PO')
sleep(1)
print('-=' * 11)
print('Computador jogou{}'.format(itens[computador]))
print('Jogador jogou {}'.format(itens[jogador]))
print('-=' * 11)
if computador == 0:
    if jogador == 0:
        print('EMPATE')
    elif jogador == 1:
        print('Jogador VENCEU')
    elif jogador == 2:
        print('Computador VENCEU')
    else:
        print('Jogada invalida')
elif computador == 1:
    if jogador == 0:
        print('Computador VENCEU')
    elif jogador == 1:
        print('EMPATE')
    elif jogador == 2:
        print('Jogador VENCEU')
    else:
        print('Jogada invalida')
elif computador == 2:
    if jogador == 0:
        print('Jogador VENCEU')
    elif jogador == 1:
        print('Computador VENCEU')
    elif jogador == 2:
        print('EMPATE')
    else:
        print('Jogada invalida')