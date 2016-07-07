from sklearn.ensemble import RandomForestClassifier, ExtraTreesClassifier, GradientBoostingClassifier
from sklearn.tree import DecisionTreeClassifier
from sklearn.cross_validation import cross_val_score, cross_val_predict
from sklearn import metrics
from AnimalDataset import AnimalDataset, AnimalTestDataset
import rows
import numpy

source_type = '_no_color_no_breed'
source_file = '../0cleaning/clean_data3' + source_type
output_file = 'trees'+source_type
def try_classifier(clf, tag):
    dataset = AnimalDataset(source_file+'_cat.csv')
    cat_testset = AnimalTestDataset(source_file+'_cat_test.csv')
    
    clf.fit(dataset.x, dataset.y)
    predictions_on_cats = clf.predict_proba(cat_testset.x)
    
    scores = cross_val_score(clf, dataset.x, dataset.y, cv=5, scoring='log_loss')
    print("Logloss (%s) on cats: %0.2f (+/- %0.2f)" % (tag, scores.mean(), scores.std() * 2))
    
    ###########################################
    
    dataset = AnimalDataset(source_file+'_dog.csv')
    dog_testset = AnimalTestDataset(source_file+'_dog_test.csv')
    
    clf.fit(dataset.x, dataset.y)
    predictions_on_dogs = clf.predict_proba(dog_testset.x)
    
    scores = cross_val_score(clf, dataset.x, dataset.y, cv=5, scoring='log_loss')
    print("Logloss (%s) on dogs: %0.2f (+/- %0.2f)" % (tag, scores.mean(), scores.std() * 2))
    
    dog_testset.export_prob_predictions_to_csv(output_file+'_'+tag+'.csv', cat_testset.ids + dog_testset.ids, list(predictions_on_cats) + list(predictions_on_dogs))

# try_classifier(DecisionTreeClassifier(), 'decisiontree')
# try_classifier(DecisionTreeClassifier(min_samples_split=1), 'decisiontree_min_samples_split_1')
# try_classifier(DecisionTreeClassifier(max_features=1), 'decisiontree_max_features_1')
# try_classifier(DecisionTreeClassifier(max_features=3), 'decisiontree_max_features_3')
# try_classifier(DecisionTreeClassifier(max_features='auto'), 'decisiontree_max_features_auto')
# try_classifier(DecisionTreeClassifier(max_features='sqrt'), 'decisiontree_max_features_sqrt')
# try_classifier(DecisionTreeClassifier(max_features='log2'), 'decisiontree_max_features_log2')
# try_classifier(DecisionTreeClassifier(max_features=None), 'decisiontree_max_features_None')


# try_classifier(RandomForestClassifier(), 'randomforest')
# try_classifier(RandomForestClassifier(n_estimators=1000), 'randomforest_n_estimators_1000')
# # try_classifier(RandomForestClassifier(n_estimators=10000), 'randomforest_n_estimators_10000') nao faz diferenca
# try_classifier(RandomForestClassifier(n_estimators=1000, min_samples_split=1), 'randomforest_n_estimators_1000_min_samples_split_1')
# try_classifier(RandomForestClassifier(n_estimators=1000, min_samples_split=3), 'randomforest_n_estimators_1000_min_samples_split_1')
# try_classifier(RandomForestClassifier(max_features=1), 'randomforest_max_features_1')
# try_classifier(RandomForestClassifier(max_features=3), 'randomforest_max_features_3')
# try_classifier(RandomForestClassifier(max_features='auto'), 'randomforest_max_features_auto')
# try_classifier(RandomForestClassifier(max_features='sqrt'), 'randomforest_max_features_sqrt')
# try_classifier(RandomForestClassifier(max_features='log2'), 'randomforest_max_features_log2')
# try_classifier(RandomForestClassifier(max_features=None), 'randomforest_max_features_None')

# try_classifier(RandomForestClassifier(), 'randomforest')
# try_classifier(RandomForestClassifier(n_estimators=1000), 'randomforest_n_estimators_1000')

# try_classifier(RandomForestClassifier(), 'randomforest')
# try_classifier(RandomForestClassifier(n_estimators=2000), 'randomforest_n_estimators_2000')
# try_classifier(RandomForestClassifier(n_estimators=1000, min_samples_split=5), 'randomforest_n_estimators_1000_split_3')

# try_classifier(ExtraTreesClassifier(), 'extratrees')
# try_classifier(ExtraTreesClassifier(n_estimators=1000), 'extratrees_n_estimators_1000')
# try_classifier(ExtraTreesClassifier(n_estimators=3000), 'extratrees_n_estimators_3000')
# try_classifier(ExtraTreesClassifier(n_estimators=1000, min_samples_split=1), 'extratrees_n_estimators_1000_min_samples_split_1')
# try_classifier(ExtraTreesClassifier(n_estimators=1000, min_samples_split=3), 'extratrees_n_estimators_1000_min_samples_split_1')
# try_classifier(ExtraTreesClassifier(max_features=1), 'extratrees_max_features_1')
# try_classifier(ExtraTreesClassifier(max_features=3), 'extratrees_max_features_3')
# try_classifier(ExtraTreesClassifier(max_features='auto'), 'extratrees_max_features_auto')
# try_classifier(ExtraTreesClassifier(max_features='sqrt'), 'extratrees_max_features_sqrt')
# try_classifier(ExtraTreesClassifier(max_features='log2'), 'extratrees_max_features_log2')
# try_classifier(ExtraTreesClassifier(max_features=None), 'extratrees_max_features_None')

# try_classifier(GradientBoostingClassifier(), 'gradientboosting')
# try_classifier(GradientBoostingClassifier(min_samples_split=1), 'gradientboosting_min_samples_split_1')
# try_classifier(GradientBoostingClassifier(min_samples_split=3), 'gradientboosting_min_samples_split_3')
# try_classifier(GradientBoostingClassifier(max_features=1), 'gradientboosting_max_features_1')
# try_classifier(GradientBoostingClassifier(max_features=3), 'gradientboosting_max_features_3')
# try_classifier(GradientBoostingClassifier(max_features='auto'), 'gradientboosting_max_features_auto')
# try_classifier(GradientBoostingClassifier(max_features='sqrt'), 'gradientboosting_max_features_sqrt')
# try_classifier(GradientBoostingClassifier(max_features='log2'), 'gradientboosting_max_features_log2')
# try_classifier(GradientBoostingClassifier(max_features=None), 'gradientboosting_max_features_None')
# try_classifier(GradientBoostingClassifier(n_estimators=1000), 'gradientboosting_n_estimators_1000')
# try_classifier(GradientBoostingClassifier(n_estimators=3000), 'gradientboosting_n_estimators_3000')

try_classifier(GradientBoostingClassifier(), 'gradientboosting')
# try_classifier(GradientBoostingClassifier(learning_rate=0.9), 'gradientboosting_learning_rate_09')
# try_classifier(GradientBoostingClassifier(n_estimators=1000), 'gradientboosting_n_estimators_1000')
# try_classifier(GradientBoostingClassifier(max_depth=4), 'gradientboosting_max_depth_4')

