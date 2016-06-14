# coding: utf-8

import rows

table_3 = rows.import_from_csv('novo.csv')

quantidade_de_exemplos = len(table_3)
print '--------------- Início da Análise -----------------------\n'
print 'Quantidade de exemplos: {}'.format(quantidade_de_exemplos)

cats = filter(lambda row: row.animaltype == "Cat", table_3)
dogs = filter(lambda row: row.animaltype == "Dog", table_3)

print 'Quantidade de Gatos vs Quantidade de Cachorros: {} vs {}'.format(len(cats), len(dogs))