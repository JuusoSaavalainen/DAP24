#!/usr/bin/env python3

import pandas as pd


def below_zero() -> int:
    df = pd.read_csv("src/kumpula-weather-2017.csv")
    return df.loc[df['Air temperature (degC)'] < 0, :].shape[0]


def main():
    b_0 = below_zero()
    print(f'Number of days below zero: {b_0}')


if __name__ == "__main__":
    main()
