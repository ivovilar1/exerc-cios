produto = float(input('Qual o valor do produto? R$'))
desconto = produto*0.05
pf = produto - desconto
print('O produto que custava R${:.2f}, na promoção com o desconto de %5 vai custar R$ {:.2f}'.format(produto, pf))