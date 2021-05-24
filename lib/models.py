from sklearn.naive_bayes import MultinomialNB
from sklearn import svm
def naive_bayes_model(x_train, y_train):
    model = MultinomialNB().fit(x_train, y_train)
    return model

def svm_model(x_train, y_train):
    model = svm.LinearSVC(C=0.1).fit(x_train, y_train)
    return model