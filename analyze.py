# coding: utf-8

from __future__ import division
import rows

table_3 = rows.import_from_csv('novo.csv')

quantidade_de_exemplos = len(table_3)
cats = filter(lambda row: row.animaltype == "Cat", table_3)
dogs = filter(lambda row: row.animaltype == "Dog", table_3)
male = filter(lambda row: row.sex == "Male", table_3)
female = filter(lambda row: row.sex == "Female", table_3)
sex_unknown = filter(lambda row: row.sex == "Unknown", table_3)
return_to_owner = filter(lambda row: row.outcometype == "Return_to_owner", table_3)
euthanasia = filter(lambda row: row.outcometype == "Euthanasia", table_3)
adoption = filter(lambda row: row.outcometype == "Adoption", table_3)
transfer = filter(lambda row: row.outcometype == "Transfer", table_3)
died = filter(lambda row: row.outcometype == "Died", table_3)



print '--------------- Início da Análise -----------------------\n'
print 'Quantidade de exemplos: {}'.format(quantidade_de_exemplos)
print 'Quantidade de Gatos vs Quantidade de Cachorros: {} vs {}'.format(len(cats), len(dogs))
print 'Quantidade de Machos vs Quantidade de Fêmeas: {} vs {}'.format(len(male), len(female))
print 'Quantidade de animais com sexo desconecido: {}'.format(len(sex_unknown))
print 'Quantidade de animais devolvidos para o dono: {} --> {:.4g}%'.format(len(return_to_owner), len(return_to_owner)/quantidade_de_exemplos *100)
print 'Quantidade de animais que sofreram eutanásia: {} --> {:.4g}%'.format(len(euthanasia), len(euthanasia)/quantidade_de_exemplos *100)
print 'Quantidade de animais que foram adotados: {} --> {:.4g}%'.format(len(adoption), len(adoption)/quantidade_de_exemplos *100)
print 'Quantidade de animais que foram transferidos: {} --> {:.4g}%'.format(len(transfer), len(transfer)/quantidade_de_exemplos *100)
print 'Quantidade de animais que morreram: {} --> {:.4g}%'.format(len(died), len(died)/quantidade_de_exemplos *100)
