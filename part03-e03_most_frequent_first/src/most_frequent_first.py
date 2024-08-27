#!/usr/bin/env python3

import numpy as np

# the trick for me here was to use the argsort for vector containing the
# freq per row in col c, (finding that vector also :D)
# since argsort can output indexes based on the vector with freqs mapped per row


def most_frequent_first(a, c):
    uniq, counts = np.unique(a[:, c], return_counts=True)
    c_col_counts = counts[np.where(uniq == a[:, c][:, None])[1]]
    return a[np.argsort(c_col_counts)[::-1]]


def main():
    a = np.array([[8, 9, 8, 2],
                  [0, 5, 9, 9],
                  [5, 7, 0, 4],
                  [7, 8, 6, 2],
                  [0, 1, 5, 8]])
    print(most_frequent_first(a, 0))


if __name__ == "__main__":
    main()
