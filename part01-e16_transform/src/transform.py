#!/usr/bin/env python3

def transform(s1, s2):
    s1 = [int(element) for element in s1.split()]
    s2 = [int(element) for element in s2.split()]
    return list(map(lambda tupl: tupl[0] * tupl[1], zip(s1, s2)))


def main():
    transform("1 5 3", "2 6 -1")


if __name__ == "__main__":
    main()
