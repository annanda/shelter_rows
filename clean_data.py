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

table_1 = rows.import_from_csv("train.csv")

new_fields = OrderedDict([
    ('animalid', rows.fields.UnicodeField),
    ('name', rows.fields.UnicodeField),
    ('datetime', rows.fields.UnicodeField),
    ('holiday', rows.fields.UnicodeField),
    ('outcometype', rows.fields.UnicodeField),
    ('outcomesubtype', rows.fields.UnicodeField),
    ('animaltype', rows.fields.UnicodeField),
    ('sex', rows.fields.UnicodeField),
    ('castration', rows.fields.UnicodeField),
    ('ageuponoutcome', rows.fields.UnicodeField),
    ('breed', rows.fields.UnicodeField),
    ('color', rows.fields.UnicodeField)
])

table_2 = rows.Table(fields=new_fields)
for row in table_1:
    if row.sexuponoutcome and row.sexuponoutcome != u'Unknown':
        castration, sex = row.sexuponoutcome.split()
    else:
        castration, sex = u'Unknown', u'Unknown'
    week_day = calendar.day_name[row.datetime.weekday()]
    us_holidays = holidays.UnitedStates()
    holiday = row.datetime in us_holidays
    age_in_days = get_animal_age(row.ageuponoutcome)
    table_2.append({'animalid': row.animalid, 
                    'name': row.name, 
                    'datetime': week_day, 
                    'holiday': holiday,
                    'outcometype': row.outcometype, 
                    'outcomesubtype': row.outcomesubtype,
                    'animaltype': row.animaltype, 
                    'sex': sex, 
                    'castration': castration,
                    'ageuponoutcome': age_in_days, 
                    'breed': row.breed, 
                    'color': row.color})

rows.export_to_csv(table_2, "train_cleaned.csv")

table3_fields = OrderedDict([
    #('name', rows.fields.UnicodeField),
    ('has_name', rows.fields.UnicodeField),
    #('datetime', rows.fields.UnicodeField),
    #('holiday', rows.fields.UnicodeField),
    ('free_day', rows.fields.UnicodeField),
    ('outcometype', rows.fields.UnicodeField),
    #('outcomesubtype', rows.fields.UnicodeField),
    ('animaltype', rows.fields.UnicodeField),
    ('sex', rows.fields.UnicodeField),
    ('castration', rows.fields.UnicodeField),
    #('ageuponoutcome', rows.fields.UnicodeField),
    #('breed', rows.fields.UnicodeField),
    #('color', rows.fields.UnicodeField)
])

table_3 = rows.Table(fields=table3_fields)
for row in table_2:
    if len(row.name):
        has_name = 'Yes' 
    else: 
        has_name = 'No'
    
    if (row.datetime == "Sunday" or row.datetime == "Saturday" or row.holiday == 'True'): 
        free_day = True 
    else: 
        free_day = False
    
    table_3.append({
        'has_name': has_name,
        'free_day': free_day,
        'outcometype': row.outcometype,
        'animaltype': row.animaltype,
        'sex': row.sex,
        'castration': row.castration,
    })

rows.export_to_csv(table_3, "train_cleaned_for_by_column_analize.csv")