from datetime import date
now = date.today().year
bigger = 0
smaller = 0

for count in range(1, 8):
    year = int(input('Em que ano nasceu a {} pessoa '.format(count)))
    if (now - year) >= 18:
        bigger += 1
    else:
        smaller += 1
print('Ao todo tivemos {} pessoas maiores de idade'.format(bigger))
print('E tambem tivemos {} pessoas menores de idade'.format(smaller))





