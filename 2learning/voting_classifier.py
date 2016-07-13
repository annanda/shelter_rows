from sklearn.ensemble import RandomForestClassifier, ExtraTreesClassifier, GradientBoostingClassifier
from AnimalDataset import AnimalDataset, AnimalTestDataset
from sklearn.ensemble import VotingClassifier
from sklearn.tree import DecisionTreeClassifier
from sklearn import cross_validation

# Usando a votacao como classificador 

#################### Cats ##########################################

clf1 = GradientBoostingClassifier()
clf2 = RandomForestClassifier(n_estimators=1000)
clf3 = DecisionTreeClassifier()

eclf = VotingClassifier(estimators=[('bg', clf1), ('rf', clf2), ('dt', clf3)], voting='soft', weights=[5,0.5, 1])

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
clf3 = DecisionTreeClassifier()

############## Dogs #############################

eclf = VotingClassifier(estimators=[('lr', clf1), ('rf', clf2), ('dt', clf3)], voting='soft', weights=[5,0.5, 1])
dataset = AnimalDataset(source_file+'_dog.csv')
dog_testset = AnimalTestDataset(source_file+'_dog_test.csv')

for clf, label in zip([clf1, clf2, eclf], ['Gradient Boosting','Random Forest', 'Ensemble']):
    scores = cross_validation.cross_val_score(clf, dataset.x, dataset.y, cv=5, scoring='log_loss')
    print("Log Loss on dogs: %0.2f (+/- %0.2f) [%s]" % (scores.mean(), scores.std(), label))