# -*- coding: utf-8 -*-
import feature_to_vector
from sklearn.cross_validation import train_test_split
from sklearn import svm

X_data = feature_to_vector.X_data
Y_data = feature_to_vector.Y_data
print(Y_data)
print(Y_data.shape)

clf = svm.SVC()
clf.fit(X_data, Y_data)