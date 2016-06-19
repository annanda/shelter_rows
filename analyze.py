# coding: utf-8

from __future__ import division
import rows
import re

table_3 = rows.import_from_csv('novo.csv')

quantidade_de_exemplos = len(table_3)
cats = filter(lambda row: row.animaltype == "Cat", table_3)
dogs = filter(lambda row: row.animaltype == "Dog", table_3)
male = filter(lambda row: row.sex == "Male", table_3)
male_and_adoption = filter(lambda row: row.sex == "Male" and row.outcometype == "Adoption", table_3)
female = filter(lambda row: row.sex == "Female", table_3)
female_and_adoption = filter(lambda row: row.sex == "Female" and row.outcometype == "Adoption", table_3)
sex_unknown = filter(lambda row: row.sex == "Unknown", table_3)
sex_unknown_and_adoption = filter(lambda row: row.sex == "Unknown" and row.outcometype == "Adoption", table_3)
return_to_owner = filter(lambda row: row.outcometype == "Return_to_owner", table_3)
euthanasia = filter(lambda row: row.outcometype == "Euthanasia", table_3)
adoption = filter(lambda row: row.outcometype == "Adoption", table_3)
transfer = filter(lambda row: row.outcometype == "Transfer", table_3)
died = filter(lambda row: row.outcometype == "Died", table_3)
castrated = filter(lambda row: row.castration == "Neutered" or row.castration == "Spayed", table_3)
not_castrated = filter(lambda row: row.castration == "Intact", table_3)
castration_unknown = filter(lambda row: row.castration == "Unknown", table_3)
name = re.compile('..*')
has_name = filter(lambda row: name.match(row.name), table_3)
has_name_and_adoption = filter(lambda row: name.match(row.name) and row.outcometype == "Adoption", table_3)
weekend = filter(lambda row: row.datetime == "Sunday" or row.datetime == "Saturday", table_3)
weekend_and_adoption = filter(lambda row: (row.datetime == "Sunday" or row.datetime == "Saturday") and row.outcometype == "Adoption", table_3)
holidays = filter(lambda row: row.holiday == "True", table_3)
holidays_and_adoption = filter(lambda row: row.holiday == "True" and row.outcometype == "Adoption", table_3)
holidays_and_weekend = filter(lambda row: row.holiday == "True" and (row.datetime == "Sunday" or row.datetime == "Saturday"), table_3)


print '--------------- Início da Análise -----------------------\n'
print 'Quantidade de exemplos: {}'.format(quantidade_de_exemplos)
print '======================================================================================================'
print '======================================================================================================'
print 'Quantidade de Gatos vs Quantidade de Cachorros: {} vs {}'.format(len(cats), len(dogs))
print '======================================================================================================'
print 'Quantidade de Machos vs Quantidade de Fêmeas: {} vs {}'.format(len(male), len(female))
print 'Quantidade de animais com sexo desconecido: {}'.format(len(sex_unknown))
print '======================================================================================================'
print 'Quantidade de animais devolvidos para o dono: {} --> {:.4g}%'.format(len(return_to_owner), len(return_to_owner)/quantidade_de_exemplos *100)
print 'Quantidade de animais que sofreram eutanásia: {} --> {:.4g}%'.format(len(euthanasia), len(euthanasia)/quantidade_de_exemplos *100)
print 'Quantidade de animais que foram adotados: {} --> {:.4g}%'.format(len(adoption), len(adoption)/quantidade_de_exemplos *100)
print 'Quantidade de animais que foram transferidos: {} --> {:.4g}%'.format(len(transfer), len(transfer)/quantidade_de_exemplos *100)
print 'Quantidade de animais que morreram: {} --> {:.4g}%'.format(len(died), len(died)/quantidade_de_exemplos *100)
print '======================================================================================================'
print 'Quantidade de animais que castrados vs não castrados: {} vs {}'.format(len(castrated), len(not_castrated))
print 'Quantidade de animais com informação de castração desconhecida: {}'.format(len(castration_unknown))
print '======================================================================================================'
print 'Quantidade de animais com nome: {}'.format(len(has_name))
print '{:.4g}% dos adotados tinham nome. Quantidade: {}'.format(len(has_name_and_adoption)/len(adoption) *100, len(has_name_and_adoption))
print '{:.4g}% dos animais com nome, foram adotados'.format(len(has_name_and_adoption)/len(has_name) *100)
print '======================================================================================================'
print 'Quantidade de animais com datetime em final de semana: {}  --> {:.4g}%'.format(len(weekend), len(weekend)/quantidade_de_exemplos *100)
print 'Quantidade de animais com datetime em final de semana e foi adotado: {}  --> {:.4g}%'.format(len(weekend_and_adoption), len(weekend_and_adoption)/len(adoption) *100)
print '======================================================================================================'
print 'Quantidade de animais com datetime em feriado: {} '.format(len(holidays))
print 'Quantidade de animais com datetime em feriado e foi adotado: {}  --> {:.4g}%'.format(len(holidays_and_adoption), len(holidays)/len(adoption) *100)
print 'Quantidade de animais com datetime em feriado e final de semana: {}'.format(len(holidays_and_weekend))
print '======================================================================================================'
print 'Quantidade de animais machos e adotados: {} --> {:.4g}%'.format(len(male_and_adoption), len(male_and_adoption)/len(adoption) *100)
print 'Quantidade de animais femeas e adotados: {} --> {:.4g}%'.format(len(female_and_adoption), len(female_and_adoption)/len(adoption) *100)
print 'Quantidade de animais com sexo desconhecido e adotados: {} --> {:.4g}%'.format(len(sex_unknown_and_adoption), len(sex_unknown_and_adoption)/len(adoption) *100)

