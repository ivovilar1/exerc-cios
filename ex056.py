totalage = 0
oldman = 0
nameoldman = ''
woman20 = 0

for people in range(1,5):
    name = input('Digite o nome da {}ª pessoa: '.format(people))
    age = int(input('Digite a idade da {}ª pessoa: '.format(people)))
    sex = input('Digite o sexo da {}ª pessoa[M / F]: '.format(people)).upper()
    totalage += age
    if people == 1 and sex in 'M':
        oldman = age
        nameoldman = name
    if sex in 'M' and age > oldman:
        oldman = age
        nameoldman = name
    if sex in 'F' and age < 20:
        woman20 +=1
average = totalage / 4
print('A media de idade do grupo é de {} anos'.format(average))
print('O homem mais velho tem {} anos e se chama {}'.format(oldman, nameoldman))
print('Existe {} mulheres com menos de 20 anos'.format(woman20))



