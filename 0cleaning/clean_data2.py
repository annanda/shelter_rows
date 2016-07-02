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

table_2 = rows.import_from_csv("clean_data.csv")

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

rows.export_to_csv(table_3, "clean_data2.csv")