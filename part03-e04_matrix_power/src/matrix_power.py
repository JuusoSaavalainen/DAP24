#!/usr/bin/env python3
import numpy as np
from functools import reduce


def matrix_power(a, n):
    if n == 0:
        return np.eye(a.shape[0])
    if n < 0:
        a = np.linalg.inv(a)
    return reduce(lambda x, y: x@y, [a] * abs(n))


def main():
    a = np.random.random((4, 4))
    b = np.random.random((0, 0))
    print(matrix_power(a, -2))
    # print(np.linalg.matrix_power(a, 3))


if __name__ == "__main__":
    main()
