#!/usr/bin/env python3

import pandas as pd


def average_temperature() -> float:
    df = pd.read_csv("src/kumpula-weather-2017.csv")
    return df.loc[df['m'] == 7, 'Air temperature (degC)'].mean()


def main():
    average_temp = average_temperature()
    print(f"Average temperature in July: {average_temp}")


if __name__ == "__main__":
    main()
