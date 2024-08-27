#!/usr/bin/env python3

import numpy as np
from sklearn.linear_model import LinearRegression
import matplotlib.pyplot as plt


def fit_line(x: np.array, y: np.array) -> tuple:
    model = LinearRegression()
    model.fit(x.reshape(-1, 1), y)
    return model.coef_[0], model.intercept_


def main():
    x = np.array([1, 2, 3, 4, 5])
    y = np.array([1, 1, 3, 1, 5])
    a, b = fit_line(x, y)

    print(f'Slope: {a}')
    print(f'Intercept: {b}')

    plt.scatter(x, y)
    plt.plot(x, a*x + b)
    plt.show()


if __name__ == "__main__":
    main()
