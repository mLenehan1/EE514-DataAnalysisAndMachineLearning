from loadData import loadJson
from loadData import splitFeaturesAndTargets
from loadData import countRealFake
from exportData import exportTestTrain
from bagOfWords import bagOfWords
from dataAnalysis import countHeadlineLength
from sklearn.model_selection import LeaveOneOut
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.model_selection import KFold
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import TfidfTransformer
from sklearn.naive_bayes import MultinomialNB
from sklearn.pipeline import Pipeline
from sklearn.linear_model import SGDClassifier
from sklearn import metrics
from sklearn.model_selection import GridSearchCV
import numpy as np
import pickle
from sklearn.metrics._plot.confusion_matrix import plot_confusion_matrix
from matplotlib import pyplot as plt

data = loadJson('fake_news.json')
x, y = splitFeaturesAndTargets(data)

X_train, X_test, y_train, y_test = train_test_split(
    x, y, shuffle=True, test_size=0.25, random_state=1)

countHeadlineLength(X_train, y_train)

countRealFake(y_train, y_test)


# loo = LeaveOneOut()
# print(loo.get_n_splits(X_train))
# print(loo)
# for train_index, test_index in loo.split(X_train.to_frame(), y_train.to_frame()):
#     print("Train:", train_index, "Test:", test_index)
#     X_train, X_test = X_train[train_index], X_train[test_index]
#     y_train, y_test = y_train[train_index], y_test[test_index]
#     print(X_train, X_test, y_train, y_test)

exportTestTrain(X_train, X_test, y_train, y_test)

count_vect, X_train_counts = bagOfWords(X_train, False, True, True)

tf_transformer = TfidfTransformer(use_idf=False).fit(X_train_counts)
X_train_tf = tf_transformer.transform(X_train_counts)
print(X_train_tf.shape)

tfidf_transformer = TfidfTransformer()
X_train_tfidf = tfidf_transformer.fit_transform(X_train_counts)
print(X_train_tfidf.shape)

text_clf = Pipeline([
    ('vect', CountVectorizer()),
    ('tfidf', TfidfTransformer()),
    ('clf', MultinomialNB()),
])

text_clf.fit(X_train.headline, y_train)
filename = 'naiveBayesModel'
pickle.dump(text_clf, open(filename, 'wb'))

docs_test = X_test.headline
predicted = text_clf.predict(docs_test)
print("Bayes")
print(np.mean(predicted == y_test))

print(metrics.classification_report(y_test,
                                    predicted, target_names=None))

cm = metrics.confusion_matrix(y_test, predicted)
print(cm)

parameters = {
    'vect__stop_words': (None, "english"),
    'vect__ngram_range': [(1, 1), (1, 2)],
    'tfidf__use_idf': (True, False),
    'clf__alpha': (1e-5, 1),
    'clf__fit_prior': (True, False),
}

gs_clf = GridSearchCV(text_clf, parameters, cv=10, n_jobs=-1)
gs_clf = gs_clf.fit(X_train.headline, y_train)
filename = 'naiveBayesModelBest'
pickle.dump(gs_clf, open(filename, 'wb'))


print(gs_clf.best_score_)
for param_name in sorted(parameters.keys()):
    print("%s: %r" % (param_name, gs_clf.best_params_[param_name]))


text_clf = Pipeline([
    ('vect', CountVectorizer()),
    ('tfidf', TfidfTransformer()),
    ('clf', SGDClassifier(loss='hinge', penalty='l2',
                          alpha=1e-3, random_state=42,
                          max_iter=5, tol=None)),
])

text_clf.fit(X_train.headline, y_train)
filename = 'SGDModel'
pickle.dump(text_clf, open(filename, 'wb'))
predicted = text_clf.predict(docs_test)
print("SGD")
print(np.mean(predicted == y_test))

print(metrics.classification_report(y_test,
                                    predicted, target_names=None))
cm = metrics.confusion_matrix(y_test, predicted)
print(cm)

parameters = {
    'vect__stop_words': (None, "english"),
    'vect__ngram_range': [(1, 1), (1, 2)],
    'tfidf__use_idf': (True, False),
    'clf__alpha': (1e-2, 1e-3),
    'clf__loss': ('hinge', 'log'),
    'clf__max_iter': (1, 2, 3, 4, 5),
    'clf__shuffle': (True, False),
}

gs_clf = GridSearchCV(text_clf, parameters, cv=10, n_jobs=-1)
gs_clf = gs_clf.fit(X_train.headline, y_train)
filename = 'SGDModelBest'
pickle.dump(gs_clf, open(filename, 'wb'))

print(gs_clf.best_score_)
for param_name in sorted(parameters.keys()):
    print("%s: %r" % (param_name, gs_clf.best_params_[param_name]))
