#!/usr/bin/env python3

import pandas as pd


def cyclists():
    df = pd.read_csv("src/Helsingin_pyorailijamaarat.csv", sep=";")
    return df.dropna(how="all", axis=1).dropna(how="all", axis=0)


def main():
    cycle = cyclists()


if __name__ == "__main__":
    main()
