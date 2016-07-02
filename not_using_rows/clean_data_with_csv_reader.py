# coding: utf-8

#import rows
import calendar
import holidays
from collections import OrderedDict
import csv

def import_from_csv(file):
    with open(file, newline='') as csv_file:
        rows_as_dict = list(csv.DictReader(csv_file))
        #rows_as_object = map(lambda row: type('row', (), row)(), rows_as_dict)
        #return list(rows_as_object)
        return rows_as_dict

def export_to_csv(data, file):
    with open(file, 'w', newline='') as csv_file:
        writer = csv.DictWriter(csv_file, fieldnames=sorted(data[0].keys()))
        writer.writeheader()
        for row in data:
            writer.writerow(row)

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

table_1 = import_from_csv("train.csv")

table_2 = []
for row in table_1:
    if row['SexuponOutcome'] and row['SexuponOutcome'] != u'Unknown':
        castration, sex = row['SexuponOutcome'].split()
    else:
        castration, sex = u'Unknown', u'Unknown'
    
    # week_day = calendar.day_name[row['DateTime'].weekday()]
    # us_holidays = holidays.UnitedStates()
    # holiday = row['DateTime'] in us_holidays
    age_in_days = get_animal_age(row['AgeuponOutcome'])
    table_2.append({'animalid': row['AnimalID'], 
                    'name': row['Name'],
                    #'datetime': week_day, 
                    #'holiday': holiday,
                    'outcometype': row['OutcomeType'], 
                    'outcomesubtype': row['OutcomeSubtype'],
                    'animaltype': row['AnimalType'], 
                    'sex': sex, 
                    'castration': castration,
                    'ageuponoutcome': age_in_days, 
                    'breed': row['Breed'], 
                    'color': row['Color']})

export_to_csv(table_2, "train_cleaned_test.csv")

table_3 = []
for row in table_2:
    if len(row['name']):
        has_name = 'Yes' 
    else: 
        has_name = 'No'
    
    # if (row['datetime'] == "Sunday" or row['datetime'] == "Saturday" or row['holiday'] == 'True'): 
    #     free_day = True 
    # else: 
    #     free_day = False
    
    table_3.append({
        'has_name': has_name,
        #'free_day': free_day,
        'outcometype': row['outcometype'],
        'animaltype': row['animaltype'],
        'sex': row['sex'],
        'castration': row['castration'],
    })

export_to_csv(table_3, "train_cleaned_for_by_column_analize_test.csv")