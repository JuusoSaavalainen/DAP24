#!/usr/bin/env python3

import pandas as pd


def create_series(L1: list, L2: list) -> pd.Series:
    return (pd.Series(L1, index=["a", "b", "c"]), pd.Series(L2, index=["a", "b", "c"]))


def modify_series(s1: pd.Series, s2: pd.Series) -> pd.Series:
    return (pd.concat([s1, pd.Series(s2.loc["b"], index=["d"])]), s2.drop(labels="b"))


def main():
    L1, L2 = [1, 2, 3], [4, 5, 6]
    series = create_series(L1, L2)
    series_mod = modify_series(series[0], series[1])
    joopajoo = series_mod[0] + series_mod[1]


if __name__ == "__main__":
    main()
