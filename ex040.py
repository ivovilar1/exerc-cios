n1 = float(input('Primeira nota:'))
n2 = float(input('Segunda nota:'))
n3 = float(input('Terceira nota:'))
media = (n1 + n2 + n3) / 3
if media >= 7:
    print('As suas notas foram {}, {}, {} e sua media foi {:.1f}, portanto esta aprovado'.format(n1, n2, n3, media))
elif 4 < media < 7:
    print('As suas notas foram {}, {}, {} e a sua media foi {:.1f}, portanto esta de recuperação'.format(n1, n2, n3, media))
else:
    print('As suas notas foram {}, {}, {} e a sua media foi {:.1f}, portanto esta reprovado'.format(n1, n2, n3, media))
