#!/usr/bin/env python3

def interleave(*lists):
    zipped = zip(*lists)
    return [element for tuples in zipped for element in tuples]


def main():
    print(interleave([1, 2, 3], [20, 30, 40], ['a', 'b', 'c']))


if __name__ == "__main__":
    main()
