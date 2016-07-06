from sklearn.ensemble import RandomForestClassifier, ExtraTreesClassifier, GradientBoostingClassifier
from sklearn.tree import DecisionTreeClassifier
from sklearn.cross_validation import cross_val_score, cross_val_predict
from sklearn import metrics
from AnimalDataset import AnimalDataset, AnimalTestDataset
from sklearn.ensemble import VotingClassifier
from sklearn import cross_validation
import rows
import numpy

# source_type = '_no_color_no_breed_no_foster'
# source_file = '../0cleaning/clean_data3' + source_type
# output_file = 'random_forest'+source_type
# def try_classifier(clf, tag):
#     dataset = AnimalDataset(source_file+'_cat.csv')
#     cat_testset = AnimalTestDataset(source_file+'_cat_test.csv')
#
#     clf.fit(dataset.x, dataset.y)
#     predictions_on_cats = clf.predict_proba(cat_testset.x)
#
#     scores = cross_val_score(clf, dataset.x, dataset.y, cv=5, scoring='log_loss')
#     print("Logloss (%s) on cats: %0.2f (+/- %0.2f)" % (tag, scores.mean(), scores.std() * 2))
#
#     ###########################################
#
#     dataset = AnimalDataset(source_file+'_dog.csv')
#     dog_testset = AnimalTestDataset(source_file+'_dog_test.csv')
#
#     clf.fit(dataset.x, dataset.y)
#     predictions_on_dogs = clf.predict_proba(dog_testset.x)
#
#     scores = cross_val_score(clf, dataset.x, dataset.y, cv=5, scoring='log_loss')
#     print("Logloss (%s) on dogs: %0.2f (+/- %0.2f)" % (tag, scores.mean(), scores.std() * 2))
#
#     dog_testset.export_prob_predictions_to_csv(output_file+'_'+tag+'.csv', cat_testset.ids + dog_testset.ids, list(predictions_on_cats) + list(predictions_on_dogs))

#try_classifier(DecisionTreeClassifier(), 'decisiontree')

#try_classifier(RandomForestClassifier(), 'randomforest')
# try_classifier(RandomForestClassifier(n_estimators=1000), 'randomforest_n_estimators_1000')

# try_classifier(GradientBoostingClassifier(), 'gradientboosting')


#################### Cats ##########################################

clf1 = GradientBoostingClassifier()
clf2 = RandomForestClassifier(n_estimators=1000)

eclf = VotingClassifier(estimators=[('lr', clf1), ('rf', clf2)], voting='soft', weights=[5,0.5])

source_type = '_no_color_no_breed'
source_file = '../0cleaning/clean_data3' + source_type
output_file = 'voting_classifier_with_weight'+source_type
dataset = AnimalDataset(source_file+'_cat.csv')
cat_testset = AnimalTestDataset(source_file+'_cat_test.csv')


for clf, label in zip([clf1, clf2, eclf], ['Gradient Boosting','Random Forest', 'Ensemble']):
    scores = cross_validation.cross_val_score(clf, dataset.x, dataset.y, cv=5, scoring='log_loss')
    print("Log Loss on cats: %0.2f (+/- %0.2f) [%s]" % (scores.mean(), scores.std(), label))


clf1 = GradientBoostingClassifier()
clf2 = RandomForestClassifier(n_estimators=1000)

############## Dogs #############################

eclf = VotingClassifier(estimators=[('lr', clf1), ('rf', clf2)], voting='soft', weights=[5,0.5])
dataset = AnimalDataset(source_file+'_dog.csv')
dog_testset = AnimalTestDataset(source_file+'_dog_test.csv')

for clf, label in zip([clf1, clf2, eclf], ['Gradient Boosting','Random Forest', 'Ensemble']):
    scores = cross_validation.cross_val_score(clf, dataset.x, dataset.y, cv=5, scoring='log_loss')
    print("Log Loss on dogs: %0.2f (+/- %0.2f) [%s]" % (scores.mean(), scores.std(), label))