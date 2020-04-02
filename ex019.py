import random
a1 = input('digite o nome do primeiro aluno:')
a2 = input('digite o nome do segundo aluno:')
a3 = input('digite o nome do terceiro aluno:')
a4 = input('digite o nome do quarto aluno:')
aleatorio = a1, a2, a3, a4
escolhido = random.choice(aleatorio)
print('O aluno escolhido foi:{}'.format(escolhido))