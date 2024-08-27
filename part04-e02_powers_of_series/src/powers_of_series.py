#!/usr/bin/env python3

import pandas as pd


def powers_of_series(s: pd.Series, k: int) -> pd.DataFrame:
    return pd.DataFrame({idx: s**idx for idx in range(1, k+1)}, index=s.index)


def main():
    s = pd.Series([1, 2, 3, 4], index=list("abcd"))
    print(powers_of_series(s, 4))


if __name__ == "__main__":
    main()
