numbercousin = int(input('Digite um numero: '))
division = 0

for count in range(1,numbercousin + 1):
    if numbercousin % count == 0:
       print('\033[33m', end=' ')
       division += 1
    else:
        print('\033[31m', end=' ')
    print('{}'.format(count), end='')
print('\n\033[m O numero {} foi divisivel {} vezes'.format(numbercousin,division))
if division == 2:
    print('E por isso que ele é um NUMERO PRIMO')
else:
    print('E por isso que ele nao é um NUMERO PRIMO')



