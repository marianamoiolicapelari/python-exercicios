number = int(input('Digite um número: '))
ant = number - 1
sucess = number + 1

print('O número é {}, seu antecessor é {} e seu sucessor é {}.'.format(number, ant, sucess))

'''Fazendo com menos variáveis ficaria assim:
number = int(input('Digite um número: '))
print('O número é {}, seu antecessor é {} e seu sucessor é {}.'.format(number, (number-1), (number+1)))
'''
