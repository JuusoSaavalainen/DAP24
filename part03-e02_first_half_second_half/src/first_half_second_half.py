#!/usr/bin/env python3

import numpy as np


def first_half_second_half(a):
    size = (np.shape(a)[1] // 2)
    return a[np.sum(a[:, 0:size], axis=1) > np.sum(a[:, -size:], axis=1)]


def main():
    a = np.array([[8, 9, 8, 8],
                  [0, 5, 9, 9],
                  [5, 7, 0, 4],
                  [7, 8, 6, 2],
                  [2, 1, 5, 8]])
    print(first_half_second_half(a))


if __name__ == "__main__":
    main()
