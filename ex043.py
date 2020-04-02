peso = float(input('Digite o seu peso: (kg)'))
altura = float(input('Digite sua altura: (m)'))
imc = peso / (altura * altura)
print('O Seu IMC é de {:.2f}'.format(imc))
if imc < 18.5:
    print('Voce esta abaixo do peso')
elif imc <= 25:
    print('Voce esta no peso ideal')
elif imc <= 30:
    print('Voce esta sobrepeso')
elif imc <= 40:
    print('Voce esta obeso')
else:
    print('CUIDADO!!, seu peso esta classificado como obesidade morbida')
