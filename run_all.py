# -*- coding: utf-8 -*-
"""Benchmark of all implemented algorithms
"""
# Author: Yue Zhao <yuezhao@cs.toronto.edu>
# License: BSD 2 clause

from __future__ import division
from __future__ import print_function

import os
import sys
from time import time

# temporary solution for relative imports in case pyod is not installed
# if pyod is installed, no need to use the following line
sys.path.append(
    os.path.abspath(os.path.join(os.path.dirname("__file__"), '..')))
# supress warnings for clean output
import warnings

warnings.filterwarnings("ignore")

import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from scipy.io import loadmat

from pyod.models.abod import ABOD
from pyod.models.cblof import CBLOF
from pyod.models.feature_bagging import FeatureBagging
from pyod.models.hbos import HBOS
from pyod.models.iforest import IForest
from pyod.models.knn import KNN
from pyod.models.lof import LOF
from pyod.models.mcd import MCD
from pyod.models.ocsvm import OCSVM
from pyod.models.pca import PCA

from pyod.utils.utility import standardizer
from pyod.utils.utility import precision_n_scores
from sklearn.metrics import roc_auc_score

# TODO: add neural networks, LOCI, SOS
# TODO: and update output precision (=4)
# Define data file and read X and y

# mat_file_list = ['shuttle.mat']
mat_file_list = ['cover.mat']

n_ite = 1
n_classifiers = 1

df_columns = ['Data', '#Samples', '# Dimensions', 'Outlier Perc', sys.argv[1]]

roc_df = pd.DataFrame(columns=df_columns)
prn_df = pd.DataFrame(columns=df_columns)
time_df = pd.DataFrame(columns=df_columns)

for j in range(len(mat_file_list)):

    mat_file = mat_file_list[j]
    mat = loadmat(os.path.join('data', mat_file))

    X = mat['X']
    y = mat['y'].ravel()
    outliers_fraction = np.count_nonzero(y) / len(y)
    outliers_percentage = round(outliers_fraction * 100, ndigits=4)

    # construct containers for saving results
    roc_list = [mat_file[:-4], X.shape[0], X.shape[1], outliers_percentage]
    prn_list = [mat_file[:-4], X.shape[0], X.shape[1], outliers_percentage]
    time_list = [mat_file[:-4], X.shape[0], X.shape[1], outliers_percentage]

    roc_mat = np.zeros([n_ite, n_classifiers])
    prn_mat = np.zeros([n_ite, n_classifiers])
    time_mat = np.zeros([n_ite, n_classifiers])

    # Apagar o número 0 sendo passado como parâmetro do RandomState
    random_state = np.random.RandomState(0)

    # 60% data for training and 40% for testing
    X_train, X_test, y_train, y_test = \
        train_test_split(X, y, test_size=0.4, random_state=random_state)

    # standardizing data for processing
    X_train_norm, X_test_norm = standardizer(X_train, X_test)

    if sys.argv[1] == 'abod':
        classifiers = {'Angle-based Outlier Detector (ABOD)': ABOD(contamination=outliers_fraction)}
        classifiers_indices = {
            'Angle-based Outlier Detector (ABOD)': 0}
    elif sys.argv[1] == 'cblof':
        classifiers = {'Cluster-based Local Outlier Factor': CBLOF(contamination=outliers_fraction, check_estimator=False, random_state=random_state)}
        classifiers_indices = {'Cluster-based Local Outlier Factor': 0}
    elif sys.argv[1] == 'fb':
        classifiers = {'Feature Bagging': FeatureBagging(contamination=outliers_fraction, check_estimator=False, random_state=random_state)}
        classifiers_indices = {'Feature Bagging': 0}
    elif sys.argv[1] == 'hbos':
        classifiers = {'Histogram-base Outlier Detection (HBOS)': HBOS(contamination=outliers_fraction)}
        classifiers_indices = {'Histogram-base Outlier Detection (HBOS)': 0}
    elif sys.argv[1] == 'iforest':
        classifiers = {'Isolation Forest': IForest(contamination=outliers_fraction, random_state=random_state)}
        classifiers_indices = {'Isolation Forest': 0}
    elif sys.argv[1] == 'knn':
        classifiers = {'K Nearest Neighbors (KNN)': KNN(contamination=outliers_fraction)}
        classifiers_indices = {'K Nearest Neighbors (KNN)': 0}
    elif sys.argv[1] == 'lof':
        classifiers = {'Local Outlier Factor (LOF)': LOF(contamination=outliers_fraction)}
        classifiers_indices = {'Local Outlier Factor (LOF)': 0}
    elif sys.argv[1] == 'mcd':
        classifiers = {'Minimum Covariance Determinant (MCD)': MCD(contamination=outliers_fraction, random_state=random_state)}
        classifiers_indices = {'Minimum Covariance Determinant (MCD)': 0}
    for clf_name, clf in classifiers.items():
        print("\n\nAlgorithm: ", clf_name)
        t0 = time()
        clf.fit(X_train_norm)
        test_scores = clf.decision_function(X_test_norm)
        t1 = time()
        duration = round(t1 - t0, ndigits=4)

        roc = round(roc_auc_score(y_test, test_scores), ndigits=4)
        prn = round(precision_n_scores(y_test, test_scores), ndigits=4)

        print('ROC:{roc}, precision @ rank n:{prn}, '
              'execution time: {duration}s'.format(roc=roc, prn=prn, duration=duration))

        time_mat[0, classifiers_indices[clf_name]] = duration
        roc_mat[0, classifiers_indices[clf_name]] = roc
        prn_mat[0, classifiers_indices[clf_name]] = prn

    time_list = time_list + np.mean(time_mat, axis=0).tolist()
    temp_df = pd.DataFrame(time_list).transpose()
    temp_df.columns = df_columns
    time_df = pd.concat([time_df, temp_df], axis=0)

    roc_list = roc_list + np.mean(roc_mat, axis=0).tolist()
    temp_df = pd.DataFrame(roc_list).transpose()
    temp_df.columns = df_columns
    roc_df = pd.concat([roc_df, temp_df], axis=0)

    prn_list = prn_list + np.mean(prn_mat, axis=0).tolist()
    temp_df = pd.DataFrame(prn_list).transpose()
    temp_df.columns = df_columns
    prn_df = pd.concat([prn_df, temp_df], axis=0)

# No need to save locally
# time_df.to_excel('time.xlsx', index=False)
# roc_df.to_excel('roc.xlsx', index=False)
# prn_df.to_excel('prc.xlsx', index=False)

time_df.to_csv('{algorithm}-time.csv'.format(algorithm=sys.argv[1]), index=False)
roc_df.to_csv('{algorithm}-roc.csv'.format(algorithm=sys.argv[1]), index=False)
prn_df.to_csv('{algorithm}-prc.csv'.format(algorithm=sys.argv[1]), index=False)