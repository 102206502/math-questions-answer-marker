# -*- coding: utf-8 -*-
import feature_to_vector
from sklearn.cross_validation import train_test_split
from sklearn import svm
from sklearn import metrics
from sklearn.preprocessing import scale
from sklearn import cluster
from sklearn.manifold import Isomap
import numpy as np
import matplotlib.pyplot as plt



X_data, Y_data = feature_to_vector.get_all_data(2)
X_train, X_test, Y_train, Y_test = train_test_split(X_data, Y_data, test_size = 0.25, random_state = 42)
print(X_data)
print(Y_data)
print(Y_data.shape)

clf = svm.SVC(kernel='linear')
clf.fit(X_train, Y_train)

predicted = clf.predict(X_test)

print(metrics.classification_report(Y_test, predicted))
print(metrics.confusion_matrix(Y_test, predicted))

# X_iso = Isomap(n_neighbors=10).fit_transform(X_train)

# fig, ax = plt.subplots(1, 2, figsize=(8, 4))

# fig.subplots_adjust(top=0.85)

# ax[0].scatter(X_iso[:, 0], X_iso[:, 1], c=predicted)
# ax[0].set_title('Predicted labels')
# ax[1].scatter(X_iso[:, 0], X_iso[:, 1], c=y_train)
# ax[1].set_title('Actual Labels')

# # 加入標題
# fig.suptitle('Predicted versus actual labels', fontsize=14, fontweight='bold')

# # 顯示圖形
# plt.show()

