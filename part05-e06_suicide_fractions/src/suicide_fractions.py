#!/usr/bin/env python3

import pandas as pd


def suicide_fractions() -> pd.Series:
    df = pd.read_csv("src/who_suicide_statistics.csv")
    # not needed
    # df = df.dropna(subset=["suicides_no"])
    df = df.drop(["year", "age", "sex"], axis=1)
    df['rate'] = df['suicides_no'] / df['population']
    df = df.groupby("country").mean()
    return pd.Series(df["rate"], index=df.index)


def main():
    print(suicide_fractions())


if __name__ == "__main__":
    main()
