n1 = 7.0
n2 = 8.5
n3 = 3.0
n4 = 5.0

media = (n1 + n2 + n3 + n4)/4

if (media < 3):
    print(' Média: ', media, '. Situação: Reprovado')
elif (media < 7):
    print(' Média: ', media, '. Situação: Exame')
else :
    print(' Média: ', media, '. Situação: Aprovado')