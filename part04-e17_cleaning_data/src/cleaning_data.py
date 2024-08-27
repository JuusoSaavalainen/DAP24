#!/usr/bin/env python3

import pandas as pd
import numpy as np
import re

# hopefully the seasons range 0-3 :D
number_map = {
    'zero': 0,
    'one': 1,
    'two': 2,
    'three': 3,
}


def str_formatter(name: str) -> object:
    parts = name.split(",")
    if len(parts) == 2:
        last_name = parts[0].strip().title()
        first_name = parts[1].strip().title()
        return f'{first_name} {last_name}'
    else:
        return f'{name.strip().title()}'


def extract_int(cell: str) -> int:
    ints = re.findall(r'\d+', cell)
    return int(ints[0]) if ints else None


def format_int(col: pd.Series) -> pd.Series:
    col = col.replace('-', np.nan)
    return col.astype(float)


def map_to_int(cell: str) -> int:
    try:
        return int(cell)
    except ValueError:
        return number_map.get(cell.lower(), None)


def cleaning_data() -> pd.DataFrame:
    df = pd.read_csv('src/presidents.tsv', sep="\t")

    df['President'] = df['President'].apply(str_formatter)
    df['Vice-president'] = df['Vice-president'].apply(str_formatter)
    df['Start'] = df['Start'].apply(extract_int)
    df['Seasons'] = df['Seasons'].apply(map_to_int)
    df['Last'] = format_int(df['Last'])

    return df


def main():
    df = cleaning_data()
    print(df.dtypes)


if __name__ == "__main__":
    main()
