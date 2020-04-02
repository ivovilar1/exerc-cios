print('-=' * 20, end='')
print('loja virtual', end='')
print('=-' * 20)
preco = float(input('Qual o valor da compra? R$'))
print(''' FORMAS DE PAGAMENTO'
[ 1 ] à vista no dinheiro/cheque
[ 2 ] à vista no cartão
[ 3 ] 2x no cartão
[ 4 ] 3x ou mais no cartão''')
opcao = int(input('Sua opção :'))
if opcao == 1:
    desconto = preco * 0.10
    novopreco = preco - desconto
    print('O valor da compra de R${:.2f} reais com 10% de desconto ficará R${:.2f} reais'.format(preco, novopreco))
elif opcao == 2:
    desconto = preco * 0.05
    novopreco = preco - desconto
    print('O valor da compra de R${:.2f} reais com 5% de desconto ficará R${:.2f} reais'.format(preco, novopreco))
elif opcao == 3:
    parcelas = preco / 2
    print('Sua compra de R${:.2f} sera parcelada em 2x de R${:.2f} sem descontos'.format(preco,parcelas))
elif opcao == 4:
    numerodeparcelas = int(input('Quantas parcelas?'))
    juros = preco * 0.20
    precofinal = preco + juros
    parcelas = precofinal / numerodeparcelas
    print('Sua compra sera parcelada em {}x de R${:.2f} com juros'.format(numerodeparcelas, parcelas))
    print('Sua compra de R${:.2f} vai custar R${:.2f} no final'.format(preco, precofinal))
else:
    print('Opcção invalida. Tente novamente')

