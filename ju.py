"""
pensamento lógico -> as coisas tem uma sequencia e propósito - tudo pode ser convertido para programação
como fritar um ovo?
variável: algo que pode assumir qualquer valor
programação: inteiro e String (letras, nomes, palavras)
sinais: + - / * ** mod %
condicionais:
identação:
"""

import csv

# open the file in the write mode


# salario = int(input('Digite o seu salário: '))
#
# mensalista = input('Você é mensalistas [M] ou diarista [D]?\n ')
#
# hora_extra = int(input('Horas extras: '))
#
# porcento = int(input('Quanto porcento: '))
#
# if mensalista == 'M' or mensalista == 'm':
#     horas = 220
# else:
#     horas = 200
#
# valor_hora = (salario/horas)
# final = (valor_hora + ((porcento/100)*valor_hora)) * hora_extra
#
# print(valor_hora)
# print(final)



lista = [1, 2, 4, 5, 10, 3, 22, 12, 15]
print(lista)
for i in range(len(lista)-1):
    if lista[i] < lista[i+1]:
        print(lista[i])



