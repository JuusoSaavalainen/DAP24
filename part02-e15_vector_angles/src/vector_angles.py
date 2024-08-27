#!/usr/bin/env python3

import numpy as np
import scipy.linalg


def vector_angles(X, Y):
    # be aware that even with clipping ->
    # using: np.sqrt(np.sum(np.square(x), axis=1))
    # fucks this up :_), so you just learned that
    # but now its useless.. :D

    x_inner = scipy.linalg.norm(X, axis=1)
    y_inner = scipy.linalg.norm(Y, axis=1)
    alakerrat = x_inner * y_inner
    ylakerrat = np.sum(X * Y, axis=1)
    values = ylakerrat / alakerrat
    return np.degrees(np.arccos(np.clip(values, -1, 1)))


def main():
    a, b = np.random.randn(3, 2), np.random.randn(3, 2)
    vector_angles(a, b)


if __name__ == "__main__":
    main()
