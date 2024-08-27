#!/usr/bin/env python3

import pandas as pd
from sklearn.linear_model import LinearRegression


def mystery_data():
    df = pd.read_csv("src/mystery_data.tsv", sep="\t")
    model = LinearRegression(fit_intercept=False)
    model.fit(df.iloc[:, :-1], df.iloc[:, -1])
    return model.coef_


def main():
    coefficients = mystery_data()
    for i, coef in enumerate(coefficients):
        print(f'Coefficient of X{i + 1} is {coef}')


if __name__ == "__main__":
    main()
