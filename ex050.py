#Desenvolva um programa que leia seis numeros inteiros e mostre a soma apenas daqueles que forem pares.
#Se o valor for impar, desconsidere-o
sum = 0
for count in range(1,7):
    number = int(input('Digite um valor: '))
    if number %2 == 0:
        sum += number
    else:
        print('Valor invalido, digite apenas pares')
print('A soma dos numeros pares é {}'.format(sum))

