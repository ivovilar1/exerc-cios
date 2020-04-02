velocidade = float(input('Qual a velocidade do carro ?'))
multa = (velocidade - 80) * 7
if velocidade < 80:
    print('Tenha um bom dia! Diriga com segurança!')
else:
    print('Multado! Voce excedeu o limite de velocidade permitido que é de 80 km/h, \n Voce deve pagar uma multa de R$:{:.2f}'.format(multa))
