#!/usr/bin/env python3

import sys
import math


def summary(filename):
    with open(filename) as f:
        floats = []
        for line in f.readlines():
            line = line.strip()
            try:
                floatt = float(line)
                floats.append(floatt)
            except ValueError:
                pass
    average = sum(floats) / len(floats)
    std = math.sqrt(sum([(i - average) * (i - average)
                         for i in floats]) / (len(floats) - 1))
    return (sum(floats), average, std)


def main():
    for i in sys.argv[1:]:
        triple = summary(i)
        print(
            f'File: {i} Sum: {triple[0]:.6f} Average: {triple[1]:.6f} Stddev: {triple[2]:.6f}')


if __name__ == "__main__":
    main()
