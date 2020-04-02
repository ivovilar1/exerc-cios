#Faça um programa que calcule a soma entre todos os numeros impares que sao multiplos de 3 e que se encontram no intervalo de 1 ate 500.

sum = 0
count = 0
for number in range(1,501,2):
    if number % 3 == 0:
        count += 1
        sum += number
print('A soma de todos os {} valores solicitados é {}'.format(count, sum))









