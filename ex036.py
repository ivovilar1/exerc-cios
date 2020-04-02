casa = float(input('Qual é o valor da casa? R$'))
salario = float(input('Qual o salario do comprador? R$'))
anos = int(input('Quantos anos de financiamento?'))
prestacao = casa / (anos * 12)
minimo = salario * 0.30
print('Para pagar uma casa de R${:.2f} em {} anos'.format(casa, anos), end='')
print(' a prestação sera de R${:.2f}'.format(prestacao))
if salario <= minimo:
    print('Emprestimo nao liberado')
else:
    print('Emprestimo liberado')


