# coding: utf-8

from __future__ import division
from collections import OrderedDict
import rows
import re

table = rows.import_from_csv('../0cleaning/clean_data2.csv')

statistics = {}
for row in table:
    drow = row.__dict__
    
    for key, value in drow.items():
        if key not in statistics:
            statistics[key] = {}
        
        if value not in statistics[key]:
            statistics[key][value] = 0
        statistics[key][value] += 1

string = rows.fields.UnicodeField

columns = {}
columns['value'] = string
for key in statistics.keys():
    for value in statistics[key].keys():
        columns[key + '_' + value] = string
        
table_2d_analize = rows.Table(fields=columns)
drows = map(lambda r: r.__dict__, table)
for key in statistics.keys():
    for value in statistics[key].keys():
        data = {}
        data['value'] = key + '_' + value
        for key2 in statistics.keys():
            for value2 in statistics[key2].keys():
                data[key2 + '_' + value2] = len(filter(lambda d: d[key] == value and d[key2] == value2, drows))
        table_2d_analize.append(data)
        
rows.export_to_csv(table_2d_analize, '2d_column_analize.csv')
                    