salario = float(input('Qual é o salario do Funcionario?R$'))
aumento = salario*0.15
novo = aumento +salario
print('Um funcionario que ganhava R$ {:.2f}, com 15% de aumento, passa a receber R$ {:.2f}'.format(salario,novo))