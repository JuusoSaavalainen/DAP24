#!/usr/bin/env python3

import pandas as pd


def top_bands() -> pd.DataFrame:
    df_bands = pd.read_csv("src/bands.tsv", sep="\t")
    df_top40 = pd.read_csv("src/UK-top40-1964-1-2.tsv", sep="\t")
    df_bands['Band'] = df_bands['Band'].str.lower()
    df_top40['Artist'] = df_top40['Artist'].str.lower()
    merge_df = pd.merge(df_bands, df_top40, left_on="Band",
                        right_on="Artist", how="inner")
    return merge_df


def main():
    print(top_bands())


if __name__ == "__main__":
    main()
