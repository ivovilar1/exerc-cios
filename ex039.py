from datetime import date
ano = int(input('Ano de Nascimento:'))
anoatual = date.today().year
idade = anoatual - ano
print('Quem nasceu no ano {} tem {} anos  em {}'.format(ano, idade, anoatual))
if idade < 18:
    saldo= 18 - idade
    print('Ainda faltam {} anos para o alistamento'.format(saldo))
    alista = anoatual + saldo
    print('Seu alistamento será em {}'.format(alista))
elif idade > 18:
    saldo = idade - 18
    print('Voce ja deveria ter se alistado há {} anos'.format(saldo))
    alista = anoatual - saldo
    print('Voce se alistou no ano {}'.format(alista))
else:
    print('Voce tem que se alistar nesse ano')
