salario = float(input('Digite o salario do funcionario : R$ '))
if salario <= 1250:
    aumento = salario * 0.15
    ns = salario + aumento
    print('O funcionario que recebia R${:.2f}, com o aumento passa a receber R${:.2f}'.format(salario, ns))
else:
    aumento = salario * 0.10
    ns = salario + aumento
    print('O funcionario que recebia R${:.2f}, com o aumento passa a receber R${:.2f}'.format(salario, ns))

