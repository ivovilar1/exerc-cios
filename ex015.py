km = float(input('Quantos km o carro percorreu?'))
dia = int(input('Quantos dias o carro ficou alugado?'))
alugueldia = dia * 60
aluguelkm = km *0.15
aluguel = aluguelkm + alugueldia

print('O total a pagar pelo aluguel do carro é: R${:.2f}'.format(aluguel))
