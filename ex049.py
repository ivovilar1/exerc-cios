#faça uma tabuada de um numero que o usuario escolher utilizando o laço FOR.

mt = int(input('Digite um numero para ver sua tabuada:'))

for count in range (1,11):
    print('{} x {:2} = {}'.format(mt,count, mt*count))

