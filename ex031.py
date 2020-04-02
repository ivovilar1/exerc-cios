viagem = float(input('Qual a distancia da viagem?'))
if viagem <= 200:
    print('Voce esta querendo fazer uma viagem de {:.2f} km'.format(viagem))
    preço = viagem * 0.50
    print('o Valor para essa viagem é de R${:.2f}'.format(preço))
else:
    print('Voce esta querendo fazer uma viagem de {:2.f} km'.format(viagem))
    preço = viagem * 0.45
    print('o valor para essa viagem é de R${:.2f}'.format(preço))
print('Obrigado por escolher nossa empresa!')