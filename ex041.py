from datetime import date
nasc = int(input('Ano de nascimento:'))
anoatual = date.today().year
idade = anoatual - nasc
if idade <=9:
    print('O atleta tem {} anos'.format(idade))
    print('Classificação: Mirim')
elif 9 < idade < 14:
    print('O atleta tem {} anos'.format(idade))
    print('Classificação: Infantil')
elif 14 < idade < 19:
    print('O atleta tem {} anos'.format(idade))
    print('Classificação: Junior')
elif  19 < idade < 25:
    print('O atleta tem {} anos'.format(idade))
    print('Classificação: Sênior')
elif idade > 25:
    print('O atleta tem {} anos'.format(idade))
    print('Classificação: Master')