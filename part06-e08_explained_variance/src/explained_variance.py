#!/usr/bin/env python3

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.decomposition import PCA


def explained_variance():
    data = pd.read_csv("src/data.tsv", sep="\t")
    base_var = data.var(axis=0).to_list()
    pca = PCA(n_components=10)
    pca.fit(data)
    return base_var, pca.explained_variance_


def main():
    v, ev = explained_variance()
    print(sum(v), sum(ev))
    print('The variances are: ', ' '.join(f'{i:.3f}' for i in v))
    print('The explained variances after PCA are: ',
          ' '.join(f'{i:.3f}' for i in ev))
    cum_ev = np.cumsum(ev)
    plt.plot(range(1, len(cum_ev) + 1), cum_ev)
    plt.show()


if __name__ == "__main__":
    main()
