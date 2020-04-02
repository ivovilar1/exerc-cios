oneterm = int(input('Digite o primeiro termo: '))
reason = int(input('Digite a razão: '))
tenth = oneterm + (10 - 1) * reason
for count in range(oneterm, tenth + reason, reason):
    print('{}'.format(count), end=' -> ')
print('Acabou!')

