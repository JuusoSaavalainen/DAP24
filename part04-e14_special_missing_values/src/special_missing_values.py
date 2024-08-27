#!/usr/bin/env python3

import pandas as pd
import numpy as np


def special_missing_values() -> pd.DataFrame:
    df = pd.read_csv("src/UK-top40-1964-1-2.tsv", sep="\t")
    df['LW'] = df['LW'].replace(['New', 'Re'], np.nan).astype(float)
    return df.loc[df['Pos'] > df['LW'], :]


def main():
    print(special_missing_values())


if __name__ == "__main__":
    main()
