text = input('Digite aqui sua frase: ').strip().upper()
word = text.split()
together = ''.join(word)
reverse = ''
for letter in range(len(together)- 1, -1, -1):
    reverse += together[letter]
print('O inverso de {} é {}'.format(together,reverse))
if reverse == together:
    print('Temos um palídromo')
else:
    print('Nao temos um palidromo')
