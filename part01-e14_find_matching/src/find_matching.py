#!/usr/bin/env python3

def find_matching(L, pattern):
    l = []
    for i, x in enumerate(L):
        if pattern in x:
            l.append(i)
    return l


def main():
    find_matching(["sensitive", "engine", "rubbish", "comment"], "en")


if __name__ == "__main__":
    main()
