largura = float(input('Digite a largura da parede:'))
altura = float(input('Digite a altura da parede:'))

area = largura * altura
tinta = area / 2

print('Sua parede tem a dimensão de {}x{} e sua área é de {:.2f}m².'.format(largura, altura, area))
print('Para pintar essa parede, você precisará de {}l de tinta.'.format(tinta))

