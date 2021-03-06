# coding: utf-8

from __future__ import division
import rows

table_3 = rows.import_from_csv('../0cleaning/clean_data.csv')

quantidade_de_exemplos = len(table_3)
cats = filter(lambda row: row.animaltype == "Cat", table_3)
cats_and_adoption = filter(lambda row: row.animaltype == "Cat" and row.outcometype == "Adoption", table_3)
cats_and_transfer = filter(lambda row: row.animaltype == "Cat" and row.outcometype == "Transfer", table_3)
cats_and_euthanasia = filter(lambda row: row.animaltype == "Cat" and row.outcometype == "Euthanasia", table_3)
cats_and_died = filter(lambda row: row.animaltype == "Cat" and row.outcometype == "Died", table_3)
cats_and_returned = filter(lambda row: row.animaltype == "Cat" and row.outcometype == "Return_to_owner", table_3)

dogs = filter(lambda row: row.animaltype == "Dog", table_3)
dogs_and_adoption = filter(lambda row: row.animaltype == "Dog" and row.outcometype == "Adoption", table_3)
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
castrated_and_adoption = filter(lambda row: (row.castration == "Neutered" or row.castration == "Spayed") and row.outcometype == "Adoption", table_3)
not_castrated = filter(lambda row: row.castration == "Intact", table_3)
not_castrated_and_adoption = filter(lambda row: row.castration == "Intact" and row.outcometype == "Adoption", table_3)
castration_unknown = filter(lambda row: row.castration == "Unknown", table_3)
has_name = filter(lambda row: row.name, table_3)
has_not_name = filter(lambda row: not row.name, table_3)
has_not_name_and_adoption = filter(lambda row: not row.name and row.outcometype == "Adoption", table_3)
has_name_and_adoption = filter(lambda row: row.name and row.outcometype == "Adoption", table_3)
weekend = filter(lambda row: row.datetime == "Sunday" or row.datetime == "Saturday", table_3)
weekend_and_adoption = filter(lambda row: (row.datetime == "Sunday" or row.datetime == "Saturday") and row.outcometype == "Adoption", table_3)
weekend_and_transfer = filter(lambda row: (row.datetime == "Sunday" or row.datetime == "Saturday") and row.outcometype == "Transfer", table_3)
weekend_and_euthanasia = filter(lambda row: (row.datetime == "Sunday" or row.datetime == "Saturday") and row.outcometype == "Euthanasia", table_3)
weekend_and_died = filter(lambda row: (row.datetime == "Sunday" or row.datetime == "Saturday") and row.outcometype == "Died", table_3)
weekend_and_returned = filter(lambda row: (row.datetime == "Sunday" or row.datetime == "Saturday") and row.outcometype == "Return_to_owner", table_3)
holidays = filter(lambda row: row.holiday == "True", table_3)
holidays_and_adoption = filter(lambda row: row.holiday == "True" and row.outcometype == "Adoption", table_3)
holidays_and_transfer = filter(lambda row: row.holiday == "True" and row.outcometype == "Transfer", table_3)
holidays_and_euthanasia = filter(lambda row: row.holiday == "True" and row.outcometype == "Euthanasia", table_3)
holidays_and_died = filter(lambda row: row.holiday == "True" and row.outcometype == "Died", table_3)
holidays_and_returned = filter(lambda row: row.holiday == "True" and row.outcometype == "Return_to_owner", table_3)
holidays_and_weekend = filter(lambda row: row.holiday == "True" and (row.datetime == "Sunday" or row.datetime == "Saturday"), table_3)
holidays_and_weekend_and_adoption = filter(lambda row: row.holiday == "True" and (row.datetime == "Sunday" or row.datetime == "Saturday") and row.outcometype == "Adoption", table_3)

kitten = filter(lambda row: row.agegroup == "kitten" , table_3)
kitten_and_adoption = filter(lambda row: row.agegroup == "kitten" and row.outcometype == "Adoption", table_3)
kitten_and_transfer = filter(lambda row: row.agegroup == "kitten" and row.outcometype == "Transfer", table_3)
kitten_and_euthanasia = filter(lambda row: row.agegroup == "kitten" and row.outcometype == "Euthanasia", table_3)
kitten_and_died = filter(lambda row: row.agegroup == "kitten" and row.outcometype == "Died", table_3)
kitten_and_returned = filter(lambda row: row.agegroup == "kitten" and row.outcometype == "Return_to_owner", table_3)
adult_cat = filter(lambda row: row.agegroup == "adult" and row.animaltype == "Cat" , table_3)
adult_cat_and_adoption = filter(lambda row: row.agegroup == "adult" and row.animaltype == "Cat" and row.outcometype == "Adoption" , table_3)
senior = filter(lambda row: row.agegroup == "senior" , table_3)
senior_and_adoption = filter(lambda row: row.agegroup == "senior" and row.outcometype == "Adoption" , table_3)
puppy = filter(lambda row: row.agegroup == "puppy" , table_3)
puppy_and_adoption = filter(lambda row: row.agegroup == "puppy" and row.outcometype == "Adoption" , table_3)
adult_dog = filter(lambda row: row.agegroup == "adult" and row.animaltype == "Dog" , table_3)
adult_dog_and_adoption = filter(lambda row: row.agegroup == "adult" and row.animaltype == "Dog" and row.outcometype == "Adoption", table_3)
aging_dog = filter(lambda row: row.agegroup == "aging_dog" , table_3)
aging_dog_and_adoption = filter(lambda row: row.agegroup == "aging_dog" and row.outcometype == "Adoption", table_3)
aging_dog_and_adoption = filter(lambda row: row.agegroup == "aging_dog" and row.outcometype == "Adoption", table_3)

adoption_and_foster = filter(lambda row: row.outcometype == "Adoption" and row.outcomesubtype == "Foster", table_3)
adoption_and_foster_2 = filter(lambda row: row.outcometype == "Adoption" and row.outcomesubtype == "In Foster", table_3)


print '--------------- Início da Análise -----------------------\n'
print 'Quantidade de exemplos: {}'.format(quantidade_de_exemplos)
print '======================================================================================================'
print '======================================================================================================'
print 'Quantidade de Gatos vs Quantidade de Cachorros: {} vs {}'.format(len(cats), len(dogs))
print '{:.4g}% dos animais adotados eram gatos'.format(len(cats_and_adoption)/len(adoption) *100)
print '{:.4g}% dos animais adotados eram cães'.format(len(dogs_and_adoption)/len(adoption) *100)
print '======================================================================================================'
print 'Quantidade de animais devolvidos para o dono: {} --> {:.4g}%'.format(len(return_to_owner), len(return_to_owner)/quantidade_de_exemplos *100)
print 'Quantidade de animais que sofreram eutanásia: {} --> {:.4g}%'.format(len(euthanasia), len(euthanasia)/quantidade_de_exemplos *100)
print 'Quantidade de animais que foram adotados: {} --> {:.4g}%'.format(len(adoption), len(adoption)/quantidade_de_exemplos *100)
print 'Quantidade de animais que foram transferidos: {} --> {:.4g}%'.format(len(transfer), len(transfer)/quantidade_de_exemplos *100)
print 'Quantidade de animais que morreram: {} --> {:.4g}%'.format(len(died), len(died)/quantidade_de_exemplos *100)
print '======================================================================================================'
print 'Quantidade de animais que castrados vs não castrados: {} vs {}'.format(len(castrated), len(not_castrated))
print '{:.4g}% dos animais adotados eram castrados'.format(len(castrated_and_adoption)/len(adoption) *100)
print '{:.4g}% dos animais adotados não eram castrados'.format(len(not_castrated_and_adoption)/len(adoption) *100)
print 'Quantidade de animais com informação de castração desconhecida: {}'.format(len(castration_unknown))
print '{:.4g}% dos animais castrados foram adotados'.format(len(castrated_and_adoption)/len(castrated) *100)
print '{:.4g}% dos animais não castrados foram adotados'.format(len(not_castrated_and_adoption)/len(not_castrated) *100)
print '======================================================================================================'
print 'Quantidade de animais com nome: {}'.format(len(has_name))
print 'Quantidade de animais sem nome: {}'.format(len(has_not_name))
print '{:.4g}% dos adotados tinham nome. Quantidade: {}'.format(len(has_name_and_adoption)/len(adoption) *100, len(has_name_and_adoption))
print '{:.4g}% dos animais com nome, foram adotados'.format(len(has_name_and_adoption)/len(has_name) *100)
print '{:.4g}% dos animais sem nome, foram adotados'.format(len(has_not_name_and_adoption)/len(has_not_name) *100)
print '======================================================================================================'
print 'Quantidade de animais com datetime em final de semana: {}  --> {:.4g}%'.format(len(weekend), len(weekend)/quantidade_de_exemplos *100)
print 'Quantidade de animais com datetime em final de semana e foi adotado: {}  --> {:.4g}%'.format(len(weekend_and_adoption), len(weekend_and_adoption)/len(adoption) *100)
print '{:.4g}% de registros em final de semana que foram com adoção'.format(len(weekend_and_adoption)/len(weekend) *100)
print '{:.4g}% de registros em final de semana que foram com eutanásia'.format(len(weekend_and_euthanasia)/len(weekend) *100)
print '{:.4g}% de registros em final de semana que foram com devolução ao dono'.format(len(weekend_and_returned)/len(weekend) *100)
print '{:.4g}% de registros em final de semana que foram com morte'.format(len(weekend_and_died)/len(weekend) *100)
print '{:.4g}% de registros em final de semana que foram com transferencia'.format(len(weekend_and_transfer)/len(weekend) *100)
print '======================================================================================================'
print 'Quantidade de animais com datetime em feriado: {} '.format(len(holidays))
print 'Quantidade de animais com datetime em feriado e foi adotado: {}  --> {:.4g}%'.format(len(holidays_and_adoption), len(holidays_and_adoption)/len(adoption) *100)
print '{:.4g}% dos registros em feriados, foram de adoção'.format(len(holidays_and_adoption)/len(holidays) *100)
print '{:.4g}% dos registros em feriados, foram de transferencia'.format(len(holidays_and_transfer)/len(holidays) *100)
print '{:.4g}% dos registros em feriados, foram de morte'.format(len(holidays_and_died)/len(holidays) *100)
print '{:.4g}% dos registros em feriados, foram de devolução'.format(len(holidays_and_returned)/len(holidays) *100)
print '{:.4g}% dos registros em feriados, foram de eutanásia'.format(len(holidays_and_euthanasia)/len(holidays) *100)
print 'Quantidade de animais com datetime em feriado e final de semana: {}'.format(len(holidays_and_weekend))
print 'Quantidade de animais com datetime em feriado e final de semana que foram adotados: {}'.format(len(holidays_and_weekend_and_adoption))
print '======================================================================================================'
print 'Quantidade de Machos vs Quantidade de Fêmeas: {} vs {}'.format(len(male), len(female))
print 'Quantidade de animais com sexo desconecido: {}'.format(len(sex_unknown))
print 'Quantidade de animais machos e adotados: {} --> {:.4g}%'.format(len(male_and_adoption), len(male_and_adoption)/len(adoption) *100)
print 'Quantidade de animais femeas e adotados: {} --> {:.4g}%'.format(len(female_and_adoption), len(female_and_adoption)/len(adoption) *100)
print 'Quantidade de animais com sexo desconhecido e adotados: {} --> {:.4g}%'.format(len(sex_unknown_and_adoption), len(sex_unknown_and_adoption)/len(adoption) *100)
print '{:.4g}% das fêmeas foram adotadas'.format(len(female_and_adoption)/len(female) *100)
print '{:.4g}% dos machos foram adotadas'.format(len(male_and_adoption)/len(male) *100)
print '======================================================================================================'
print '=========== Faixa etária: Gatos ======================================================================'
print '{:.4g}% de kitten'.format(len(kitten)/len(cats) *100)
print '{:.4g}% de adult'.format(len(adult_cat)/len(cats) *100)
print '{:.4g}% de senior'.format(len(senior)/len(cats) *100)
print '=========== Faixa etária e adoção: Gatos ============================================================='
print '{:.4g}% dos adotados eram filhotes'.format(len(kitten_and_adoption)/len(cats_and_adoption) *100)
print '{:.4g}% dos adotados eram adultos'.format(len(adult_cat_and_adoption)/len(cats_and_adoption) *100)
print '{:.4g}% dos adotados eram idosos'.format(len(senior_and_adoption)/len(cats_and_adoption) *100)

print '===========  Gatos Filhotes ============================================================='
print '{:.4g}% dos filhotes foram adotados'.format(len(kitten_and_adoption)/len(kitten) *100)
print '{:.4g}% dos filhotes foram mortos'.format(len(kitten_and_died)/len(kitten) *100)
print '{:.4g}% dos filhotes foram transferidos'.format(len(kitten_and_transfer)/len(kitten) *100)
print '{:.4g}% dos filhotes foram eutanasia'.format(len(kitten_and_euthanasia)/len(kitten) *100)
print '{:.4g}% dos filhotes foram devolvido ao dono'.format(len(kitten_and_returned)/len(kitten) *100)

print '=========== Faixa etária: cães ======================================================================='
print '{:.4g}% de puppy'.format(len(puppy)/len(dogs) *100)
print '{:.4g}% de adult'.format(len(adult_dog)/len(dogs) *100)
print '{:.4g}% de aging dog'.format(len(aging_dog)/len(dogs) *100)

print '=========== Faixa etária e adoção: Cães ============================================================='
print '{:.4g}% dos adotados eram filhotes'.format(len(puppy_and_adoption)/len(dogs_and_adoption) *100)
print '{:.4g}% dos adotados eram adultos'.format(len(adult_dog_and_adoption)/len(dogs_and_adoption) *100)
print '{:.4g}% dos adotados eram idosos'.format(len(aging_dog_and_adoption)/len(dogs_and_adoption) *100)

print '=========== Adoção e foster ============================================================='
print '{} Adotados e foster'.format(len(adoption_and_foster) + len(adoption_and_foster_2))
