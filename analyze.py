# coding: utf-8

import rows

table_3 = rows.import_from_csv('novo.csv')

quantidade_de_exemplos = len(table_3)
cats = filter(lambda row: row.animaltype == "Cat", table_3)
dogs = filter(lambda row: row.animaltype == "Dog", table_3)
male = filter(lambda row: row.sex == "Male", table_3)
female = filter(lambda row: row.sex == "Female", table_3)
sex_unknown = filter(lambda row: row.sex == "Unknown", table_3)


print '--------------- Início da Análise -----------------------\n'
print 'Quantidade de exemplos: {}'.format(quantidade_de_exemplos)
print 'Quantidade de Gatos vs Quantidade de Cachorros: {} vs {}'.format(len(cats), len(dogs))
print 'Quantidade de Machos vs Quantidade de Fêmeas: {} vs {}'.format(len(male), len(female))
print 'Quantidade de animais com sexo desconecido: {}'.format(len(sex_unknown))