l = float(input('Largura da parede:'))
a = float(input('Altura da parede:'))
area = l*a
tinta = area/2
print('Sua parede tem dimensao  de {}x{} e sua area é:{}m2'.format(l, a, area))
print('Para pintar essa parede, voce precisará de {}l de tinta'.format(tinta))