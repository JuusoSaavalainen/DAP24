#!/usr/bin/env python3

import pandas as pd


def growing_municipalities(df: pd.DataFrame) -> float:
    n2 = df.shape[0]
    n1 = df.loc[df['Population change from the previous year, %'] > 0].shape[0]
    return n1 / n2


def main():
    df = pd.read_csv("src/municipal.tsv", sep="\t", index_col=0)
    growing = growing_municipalities(df.loc['Akaa':'Äänekoski'])
    print(f"Proportion of growing municipalities: {growing:.1%}")


if __name__ == "__main__":
    main()
