# coding: utf-8

import rows
import calendar
import holidays
from collections import OrderedDict

def get_animal_age(name):
    if name == '': return -1

    how_many, period = name.split()

    how_many = int(how_many)
    # remove plural
    period = period[:-1] if period.endswith('s') else period

    daysInPeriod = {
        'year': 365,
        'month': 31,
        'week': 7,
        'day': 1
    }.get(period)

    return how_many * daysInPeriod
    
def get_animal_has_name(row):
    if len(row.name):
        has_name = 'Yes' 
    else: 
        has_name = 'No'
        
    return has_name
    
def get_animal_is_free_day(row):
    week_day = calendar.day_name[row.datetime.weekday()]
    us_holidays = holidays.UnitedStates()
    holiday = row.datetime in us_holidays
    
    if (week_day == "Sunday" or week_day == "Saturday" or holiday == True): 
        free_day = 'Yes'
    else: 
        free_day = 'No'
        
    return free_day
    
def get_animal_castration_columns(row):
    if row.sexuponoutcome and row.sexuponoutcome != u'Unknown':
        castration = row.sexuponoutcome.split()[0]
    else:
        castration = u'Castration_Unknown'
        
    if(castration == 'Spayed' or castration == 'Neutered'):
        castration = 'Castration'
    
    columns = OrderedDict({
        'Castration_Unknown': 0,
        'Intact': 0,
        'Castration': 0
    })
        
    columns[castration] = 1
    
    return columns
    
def get_animal_sex_columns(row):
    if row.sexuponoutcome and row.sexuponoutcome != u'Unknown':
        sex = row.sexuponoutcome.split()[1]
    else:
        sex = u'Sex_Unknown'
        
    columns = OrderedDict({
        'Sex_Unknown': 0,
        'Male': 0,
        'Female': 0
    })
        
    columns[sex] = 1
    
    return columns

def get_cat_breed_columns(row):
    # Perceba que todos com Rex no nome da raça vão ter 'Rex' como 1, não só os que são só 'Rex'
    # Mix foi incluido para facilitar o algoritmo, mas tecnicamente não é uma raça por si só
    know_breeds = [
        "Mix",
        "Domestic Shorthair", "Rex", "Domestic Medium Hair", "Himalayan", "Domestic Longhair", "Munchkin Longhair", 
        "Norwegian Forest Cat", "Sphynx", "Cymric", "American Shorthair", "Maine Coon", "Balinese", "Cornish Rex", 
        "Japanese Bobtail", "Ragdoll", "Snowshoe", "Manx", "Angora", "Havana Brown", "Tonkinese", "Siamese", 
        "Pixiebob Shorthair", "Russian Blue", "Burmese", "Javanese", "Bengal", "Exotic Shorthair", "Turkish Van", 
        "British Shorthair", "Ocicat", "Persian", "Abyssinian", "Devon Rex", "Bombay"]
    column_titles = know_breeds
    
    columns = OrderedDict()
    for title in column_titles:
        columns['breed_'+title.replace(' ', '')] = 1 if title in row.breed else 0
    
    return columns

def get_cat_color_columns(row):
    know_colors = 'Blue Cream Lilac White Brown Gray Black Tan Flame Orange Buff Apricot Chocolate Yellow Pink Silver'.split()
    know_patterns = 'Tabby Tortie Torbie Point Tiger Agouti Calico Seal Lynx Smoke'.split()
    column_titles = know_colors + know_patterns
    
    columns = OrderedDict()
    for title in column_titles:
        columns['color_'+title] = 1 if title in row.color else 0
    
    return columns
    
def get_animal_age_columns(row):
    pass

# Columns in train.csv
# AnimalID,Name,DateTime,OutcomeType,OutcomeSubtype,AnimalType,SexuponOutcome,AgeuponOutcome,Breed,Color

table_from = rows.import_from_csv("../train.csv")

new_rows = []
for row in table_from:
    new_row = OrderedDict()
    
    # AnimalID: não deve ser importante
    
    # Name: só interessa se tem ou não nome, não que nome é
    #new_row['has_name'] = get_animal_has_name(row)
    
    # DateTime: só interessa se é feriado ou não, não qual data especifica é
    #new_row['is_free_day'] = get_animal_is_free_day(row)
    
    # OutcomeType é o que queremos prever
    
    # OutcomeSubtype: não disponivel no conjunto de teste, nem é pedido que seja previsto
    
    # AnimalType: Vamos criar tabelas separadas para cada tipo de animal
    
    # SexuponOutcome: separamos em sexo e castração. Criamos um coluna por tipo de cada
    # Spayed e Neutered são dois nomes para a mesma coisa, por isso viraram 'Castration'
    #new_row.update(get_animal_castration_columns(row))
    #new_row.update(get_animal_sex_columns(row))
    
    # AgeuponOutcome
    #new_row.update(get_animal_age_columns(row))
    
    # Breed
    new_row.update(get_cat_breed_columns(row))
    new_row['breed'] = row.breed
    
    # Color
    #new_row.update(get_cat_color_columns(row))
    
    new_rows.append(new_row)

new_fields = [(key, rows.fields.UnicodeField) for key in new_rows[0].keys()]
table_to = rows.Table(fields=OrderedDict(new_fields))
for row in new_rows:
    table_to.append(row)
    
rows.export_to_csv(table_to, "clean_data3.csv")