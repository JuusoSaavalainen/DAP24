#!/usr/bin/env python3

import pandas as pd
from sklearn import linear_model


def coefficient_of_determination():
    df = pd.read_csv("src/mystery_data.tsv", sep="\t")
    model = linear_model.LinearRegression(fit_intercept=True)
    model.fit(df.iloc[:, :-1], df.iloc[:, -1])
    rsqrt = [model.score(df.iloc[:, :-1], df.iloc[:, -1])]
    for i in range(df.shape[1]-1):
        X = df.iloc[:, i].values.reshape(-1, 1)
        y = df.iloc[:, -1]
        model.fit(X, y)
        rsqrt.append(model.score(X, y))
    return rsqrt


def main():
    coefficients = coefficient_of_determination()


if __name__ == "__main__":
    main()
