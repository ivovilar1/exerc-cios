carteira = float(input('Quanto dinheiro voce tem na carteira?R$'))
dol = carteira/3.27
print('Com R${:.2f} voce pode comprar US${:.2f}'.format(carteira, dol))
