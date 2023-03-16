from math import trunc
numero = float(input('Digite um número: '))
inteiro = trunc(numero)
print('O valor digitado foi {} e a sua porção inteira é {}'.format(numero, inteiro))

'''arredondando sem módulos
num = float(input('Digite um número: '))
print('O valor digitado foi {} e a sua porção inteira é {}'.format(num, int(num)))
'''
