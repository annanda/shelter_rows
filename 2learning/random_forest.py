from sklearn.ensemble import RandomForestClassifier
from sklearn.cross_validation import cross_val_score
from AnimalDataset import AnimalDataset

dataset = AnimalDataset('../0cleaning/clean_data3_cat.csv')

#print(dataset.x[0:10])
#print(dataset.y)

clf = RandomForestClassifier(n_estimators=10)
#clf = clf.fit(X, Y)

scores = cross_val_score(clf, dataset.x, dataset.y, cv=5)

print("Accuracy: %0.2f (+/- %0.2f)" % (scores.mean(), scores.std() * 2))