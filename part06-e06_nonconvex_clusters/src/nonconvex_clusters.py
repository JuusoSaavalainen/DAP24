#!/usr/bin/env python3

import pandas as pd
import numpy as np
from sklearn.cluster import DBSCAN
from sklearn.metrics import accuracy_score


def handle_data() -> tuple:
    data = pd.read_csv("src/data.tsv", sep="\t")
    X = data[["X1", "X2"]].values
    y = data["y"].values
    unique_labels = len(np.unique(y))
    return X, y, unique_labels


def nonconvex_clusters() -> pd.DataFrame:
    results = []
    X, y, unique_labels = handle_data()
    for i in np.arange(0.05, 0.2, 0.05):
        model = DBSCAN(eps=i).fit(X)
        labels = model.labels_
        labels_clean = labels[labels != -1]
        clusters = len(np.unique(labels_clean))
        outliers = np.sum(labels == -1)
        score = np.nan if clusters != unique_labels else accuracy_score(
            y[labels != -1], labels_clean)
        results.append({"eps": float(i), "Score": float(
            score), "Clusters": float(clusters), "Outliers": float(outliers)})
    return pd.DataFrame(results)


def main():
    print(nonconvex_clusters())


if __name__ == "__main__":
    main()
