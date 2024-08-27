#!/usr/bin/env python3

def main():
    return [print((i, j)) for i in range(1, 7) for j in range(1, 7) if j+i == 5]


if __name__ == "__main__":
    main()
