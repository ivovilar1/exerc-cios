import random
from time import sleep

#computador = randint(0,5) melhor usar assim quando os numeros foram muito grandes ao inves de botar
#em uma variavel lista.





print('Vou pensar um numero entre 0 e 5. Tente adivinhar...')
numero = int(input('Em que numero eu pensei? '))
lista = [0, 1, 2, 3, 4, 5]
escolhido = random.choice(lista)
print('PROCESSANDO.....')
sleep(3)
if numero == escolhido:
    print('Voce conseguiu me vencer')
else:
    print('Ganhei!!!! eu escolhi o numero {} e nao o numero {}'.format(escolhido, numero))

