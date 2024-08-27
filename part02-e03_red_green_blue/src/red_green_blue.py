#!/usr/bin/env python3

import re


def red_green_blue(filename="src/rgb.txt"):
    with open(filename) as f:
        f.readline()
        l = []
        for line in f:
            l.append('\t'.join(re.findall(r'\d+|\w+(?:\s\w+)*', line.strip())))
    print(l)
    return l


def main():
    red_green_blue()


if __name__ == "__main__":
    main()
