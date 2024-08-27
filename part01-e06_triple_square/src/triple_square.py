#!/usr/bin/env python3


def main():
    for i in range(1, 11):
        sq = square(i)
        tr = triple(i)
        if sq > tr:
            break
        print(f"triple({i})=={tr} square({i})=={sq}")


def triple(num: int):
    return num * 3


def square(num: int):
    return num ** 2


if __name__ == "__main__":
    main()
