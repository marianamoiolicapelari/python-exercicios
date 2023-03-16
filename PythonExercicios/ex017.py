'''cateto1 = float(input('Digite o comprimento do cateto opsto: '))
cateto2 = float(input('Digite o comprimento do cateto adjacente: '))
hipotenusa = (cateto1 ** 2 + cateto2 ** 2) ** (1/2)
print('A hipotenusa vai medir {:.2f}'.format(hipotenusa))'''

from math import hypot
cateto1 = float(input('Digite o comprimento do cateto opsto: '))
cateto2 = float(input('Digite o comprimento do cateto adjacente: '))
hipotenusa = hypot(cateto1, cateto2)
print('A hipotenusa vai medir {:.2f}'.format(hipotenusa))
