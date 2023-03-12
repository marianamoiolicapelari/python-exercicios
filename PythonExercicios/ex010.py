real = float(input('Quanto dinheiro você tem na carteira? R$'))

dolar = real / 5.22
euro = real / 5.56

print('Você têm R${:.2f} reais e pode comprar US${:.2f} dólares ou €{:.2f} euros.'.format(real, dolar, euro))