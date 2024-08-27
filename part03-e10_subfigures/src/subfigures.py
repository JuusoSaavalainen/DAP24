#!/usr/bin/env python3

import numpy as np
import matplotlib.pyplot as plt


def subfigures(a):

    x = a[:, 0]
    y = a[:, 1]
    colors = a[:, 2]
    sizes = a[:, 3]

    fig, ax = plt.subplots(1, 2)
    ax[0].plot(x, y)
    ax[1].scatter(x, y, c=colors, s=sizes, cmap="plasma")
    plt.show()


def main():
    subfigures(a)


if __name__ == "__main__":
    main()
