#!/usr/bin/env python3

import sys


def file_count(filename):
    lines_res = 0
    words_res = 0
    characts_res = 0
    with open(filename) as f:
        for line in f:
            lines_res += 1
            if line == '\n':
                characts_res += 1
                continue
            words = line.split(" ")
            words_res += len(words)
            for i in line:
                characts_res += 1
    return (lines_res, words_res, characts_res)


def main():
    for i in sys.argv[1:]:
        triple = file_count(i)
        print(f'{triple[0]}\t{triple[1]}\t{triple[2]}\t{i}')


if __name__ == "__main__":
    main()
