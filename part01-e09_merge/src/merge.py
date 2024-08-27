#!/usr/bin/env python3

def merge(L1, L2):
    while True:
        if not L1:
            return L2
        if not L2:
            return L1
        if L1[0] < L2[0]:
            return [L1[0]] + merge(L1[1:], L2)
        else:
            return [L2[0]] + merge(L1, L2[1:])
    return []


def main():
    L1 = [1, 3, 5, 7]
    L2 = [2, 4, 6, 8]
    print(merge(L1, L2))


if __name__ == "__main__":
    main()
