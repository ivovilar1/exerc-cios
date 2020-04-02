bigger = 0
smaller = 0
for count in range(1,6):
    weight = float(input('Peso da {}ª pessoa: '.format(count)))
    if count == 1:
        bigger = weight
        smaller = weight
    else:
        if weight > bigger:
            bigger = weight
        if weight < smaller:
            smaller = weight
print('O maior peso lido foi {} Kg'.format(bigger))
print('O menor peso lio foi {} Kg'.format(smaller))