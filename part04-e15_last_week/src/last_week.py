#!/usr/bin/env python3

import pandas as pd
import numpy as np


def last_week() -> pd.DataFrame:
    df = pd.read_csv("src/UK-top40-1964-1-2.tsv", sep="\t")
    na_frame_template = pd.DataFrame(range(1, 41), columns=['Pos'])

    df['LW'] = df['LW'].replace(['New', 'Re'], np.nan).astype(float)
    mask = (df['Pos'] == df['Peak Pos']) & (df['Pos'] != df['LW'])
    df.loc[mask, 'Peak Pos'] = np.nan

    df.dropna(subset=['LW'])
    df['Pos'] = df['LW']
    df['WoC'] = df['WoC'] - 1
    df['LW'] = np.nan

    return pd.merge(na_frame_template, df.sort_values(
        by='Pos'), on='Pos', how='left')


def main():
    df = last_week()
    print("Shape: {}, {}".format(*df.shape))
    print("dtypes:", df.dtypes)
    print(df)


if __name__ == "__main__":
    main()
