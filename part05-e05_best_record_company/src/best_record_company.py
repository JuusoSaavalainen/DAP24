#!/usr/bin/env python3

import pandas as pd


def best_record_company() -> pd.DataFrame:
    df = pd.read_csv('src/UK-top40-1964-1-2.tsv', sep='\t')
    best_label = df.groupby('Publisher').sum().sort_values(
        'WoC', ascending=False).index[0]
    return df[df['Publisher'] == best_label]


def main():
    best_record_company()


if __name__ == "__main__":
    main()
