allstar = float(input('O valor do Allstar é: R$ '))

parcelado = allstar + (allstar * 8 / 100)
dinheiro = allstar - (allstar * 12 / 100)

print('O Allstar parcelado custa R$ {:.2f} e à vista no dinheiro custa R$ {:.2f}'.format(parcelado, dinheiro))
