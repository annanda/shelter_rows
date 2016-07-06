from sklearn.ensemble import RandomForestClassifier
from sklearn.cross_validation import cross_val_score, cross_val_predict
from sklearn import metrics
from AnimalDataset import AnimalDataset, AnimalTestDataset
import rows
import numpy

dataset = AnimalDataset('../0cleaning/clean_data3_no_breed_cat.csv')
cat_testset = AnimalTestDataset("../0cleaning/clean_data3_no_breed_cat_test.csv")

#print(cat_testset.ids)
#print(dataset.x[0:10])
#print(dataset.y)
#print(cat_testset.x)

clf = RandomForestClassifier(n_estimators=20)

clf.fit(dataset.x, dataset.y)
predictions_on_cats = clf.predict(cat_testset.x)

# print(predictions_on_cats)
# print(len(cat_testset.x))
# print(len(predictions_on_cats))

scores = cross_val_score(clf, dataset.x, dataset.y, cv=5)
print("Accuracy on cats: %0.2f (+/- %0.2f)" % (scores.mean(), scores.std() * 2))

dataset = AnimalDataset('../0cleaning/clean_data3_no_breed_dog.csv')
dog_testset = AnimalTestDataset("../0cleaning/clean_data3_no_breed_dog_test.csv")

#print(dog_testset.ids)
#print(dataset.x[0:10])
#print(dataset.y)
#print(dog_testset.x)

clf = RandomForestClassifier(n_estimators=20)

clf.fit(dataset.x, dataset.y)
predictions_on_dogs = clf.predict(dog_testset.x)

# print(predictions_on_dogs)
# print(len(dog_testset.x))
# print(len(predictions_on_dogs))

scores = cross_val_score(clf, dataset.x, dataset.y, cv=5)
print("Accuracy on dogs: %0.2f (+/- %0.2f)" % (scores.mean(), scores.std() * 2))

dog_testset.export_exact_predictions_to_csv('random_forest_no_breed.csv', cat_testset.ids + dog_testset.ids, list(predictions_on_cats) + list(predictions_on_dogs))