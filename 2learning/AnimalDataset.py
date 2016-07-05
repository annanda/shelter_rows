import csv

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