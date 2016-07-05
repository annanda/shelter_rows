import csv
from collections import OrderedDict
import rows

class AnimalDataset:
    
    def __init__(self, pathToDataset):
        self.x = []
        self.y = []
        
        with open(pathToDataset, 'r') as csv_file:
            examples = list(csv.reader(csv_file, delimiter=','))
            examples = examples[1:] # remove header
            
            for row in examples:
                example = [int(feature) for feature in row[:-1]]
                self.x.append(example)
                
                self.y.append(row[-1])
                
class AnimalTestDataset:
    
    def __init__(self, pathToDataset):
        self.x = []
        self.ids = []
        
        with open(pathToDataset, 'r') as csv_file:
            examples = list(csv.reader(csv_file, delimiter=','))
            examples = examples[1:] # remove header
            
            for row in examples:
                example = [int(feature) for feature in row[1:]] # ignore id
                idi = int(row[0])
                self.x.append(example)
                self.ids.append(idi)
                
    def export_exact_predictions_to_csv(self, ids, predictions):
        new_rows = []
        
        # classifier = {
        #     'Return_to_owner': 0,
        #     'Euthanasia': 1,
        #     'Adoption': 2,
        #     'Transfer': 3,
        #     'Died': 4
        # }

        for i, prediction in enumerate(predictions):
            #ID	Adoption	Died	Euthanasia	Return_to_owner	Transfer
            # print(type(prediction))
            # print(prediction == '3')
            # print(int(prediction == '3'))
            
            new_row = OrderedDict({})
            new_row['ID'] = ids[i]
            new_row['Adoption'] = int(prediction == '2')
            new_row['Died'] = int(prediction == '4')
            new_row['Euthanasia'] = int(prediction == '1')
            new_row['Return_to_owner'] = int(prediction == '0')
            new_row['Transfer'] = int(prediction == '3')
            
            new_rows.append(new_row)
            
        new_rows.sort(key=lambda e: e['ID'])
        #print(new_rows)
        
        new_fields = [(key, rows.fields.UnicodeField) for key in new_rows[0].keys()]
        table_to = rows.Table(fields=OrderedDict(new_fields))
        for row in new_rows:
            table_to.append(row)
            
        rows.export_to_csv(table_to, "random_forest_prediction.csv")