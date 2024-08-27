#!/usr/bin/env python3

import math
import numpy as np


def solve_quadratic(a: float, b: float, c: float):
    d = (b * b) - (4 * a * c)
    if d < 0:
        return (-1, -1)
    x1 = (-b + math.sqrt(d)) / (2 * a)
    x2 = (-b - math.sqrt(d)) / (2 * a)
    return (x1, x2)


def main():
    print(solve_quadratic(2, 1, 2))


if __name__ == "__main__":
    main()
