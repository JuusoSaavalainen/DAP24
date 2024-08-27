#!/usr/bin/env python3

import pandas as pd


def swedish_and_foreigners() -> pd.DataFrame:
    df = pd.read_csv("src/municipal.tsv", sep="\t", header=0, index_col=0)
    df = df.loc['Akaa':'Äänekoski']
    return df.loc[(df['Share of Swedish-speakers of the population, %'] > 5) &
                  (df['Share of foreign citizens of the population, %'] > 5),
                  ["Population", "Share of Swedish-speakers of the population, %", "Share of foreign citizens of the population, %"]]


def main():
    print(swedish_and_foreigners())


if __name__ == "__main__":
    main()
