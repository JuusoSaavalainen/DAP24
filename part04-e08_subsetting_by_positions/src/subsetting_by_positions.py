#!/usr/bin/env python3

import pandas as pd


def subsetting_by_positions() -> pd.DataFrame:
    df = pd.read_csv("src/UK-top40-1964-1-2.tsv",
                     sep="\t", header=0, index_col=0)
    return df.iloc[0:10, ["Title", "Artist"]]


def main():
    print(subsetting_by_positions())


if __name__ == "__main__":
    main()
