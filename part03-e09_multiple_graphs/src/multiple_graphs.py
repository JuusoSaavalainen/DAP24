#!/usr/bin/env python3

import matplotlib.pyplot as plt


def main():

    x = 2, 4, 6, 7
    y = 4, 3, 5, 1
    x2 = 1, 2, 3, 4
    y2 = 4, 2, 3, 1

    plt.plot(x, y, x2, y2)
    plt.title("Title")
    plt.xlabel("My x-axis")
    plt.ylabel("My y-axis")
    plt.show()


if __name__ == "__main__":
    main()
