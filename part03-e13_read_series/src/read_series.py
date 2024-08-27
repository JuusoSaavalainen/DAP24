#!/usr/bin/env python3

import pandas as pd


def read_series():
    index_list, value_list = [], []

    while True:
        User_input = input().split()

        if User_input == []:
            break

        if len(User_input) < 2:
            raise Exception

        value_list.append(User_input[1])
        index_list.append(User_input[0])

    return pd.Series(value_list, index=index_list)


def main():
    a = read_series()
    print(a, type(a))


if __name__ == "__main__":
    main()
