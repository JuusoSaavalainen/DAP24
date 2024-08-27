#!/usr/bin/env python3

import pandas as pd


def snow_depth() -> int:
    df = pd.read_csv("src/kumpula-weather-2017.csv")
    return max(df.loc[:, "Snow depth (cm)"])


def main():
    snow_max_depth = snow_depth()
    print(f"Max snow depth: {snow_max_depth}")


if __name__ == "__main__":
    main()
