#!/usr/bin/env python3

import scipy.cluster.hierarchy as hc
import scipy.spatial as sp
import pandas as pd
import numpy as np
from sklearn.cluster import AgglomerativeClustering
from sklearn.metrics import accuracy_score
from sklearn.metrics import pairwise_distances

from matplotlib import pyplot as plt

import seaborn as sns
sns.set(color_codes=True)


def toint(x):
    mappi = {'A': 0, 'C': 1, 'G': 2, 'T': 3}
    if len(x) == 1:
        return mappi.get(x, -1)
    else:
        return [mappi.get(i, -1) for i in x]


def get_features_and_labels(filename):
    data = pd.read_csv(filename, sep='\t')
    X = np.array([toint(i) for i in data['X']])
    y = np.array(data['y'])
    return X, y


def plot(distances, method='average', affinity='euclidean'):
    mylinkage = hc.linkage(sp.distance.squareform(distances), method=method)
    g = sns.clustermap(distances, row_linkage=mylinkage, col_linkage=mylinkage)
    g.fig.suptitle(
        f"Hierarchical clustering using {method} linkage and {affinity} affinity")
    plt.show()


def cluster_euclidean(filename):
    data = get_features_and_labels(filename)
    X = data[0]
    y = data[1]
    model = AgglomerativeClustering(
        n_clusters=2, affinity='euclidean', linkage='average')
    model.fit(X)
    return accuracy_score(y, model.labels_)


def cluster_hamming(filename):
    data = get_features_and_labels(filename)
    X = data[0]
    y = data[1]
    distances = pairwise_distances(X, metric='hamming')
    model = AgglomerativeClustering(
        n_clusters=2, affinity='precomputed', linkage='average')
    model.fit(distances)
    return accuracy_score(y, 1 - model.labels_)


def main():
    print("Accuracy score with Euclidean affinity is",
          cluster_euclidean("src/data.seq"))
    print("Accuracy score with Hamming affinity is",
          cluster_hamming("src/data.seq"))


if __name__ == "__main__":
    main()
