#!/usr/bin/env python3

import pandas as pd


def subsetting_with_loc() -> pd.DataFrame:
    df = pd.read_csv("src/municipal.tsv", sep="\t", header=0, index_col=0)
    df = df.loc['Akaa':'Äänekoski']
    return df[["Population", "Share of Swedish-speakers of the population, %", "Share of foreign citizens of the population, %"]]


def main():
    print(subsetting_with_loc())


if __name__ == "__main__":
    main()
