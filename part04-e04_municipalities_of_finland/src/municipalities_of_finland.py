#!/usr/bin/env python3

import pandas as pd


def municipalities_of_finland() -> pd.DataFrame:

    df = pd.read_csv("src/municipal.tsv", sep="\t", header=0, index_col=0)
    return df.loc['Akaa':'Äänekoski']


def main():
    print(municipalities_of_finland())


if __name__ == "__main__":
    main()
