#!/usr/bin/env python3

import pandas as pd
import matplotlib.pyplot as plt


def split_date(df: pd.DataFrame) -> pd.DataFrame:
    pvm_df = df['Päivämäärä'].str.split(expand=True)
    pvm_df.columns = ['Weekday', 'Day', 'Month', 'Year', 'Hour']
    pvm_df['Weekday'] = pvm_df['Weekday'].map(
        {'ma': 'Mon', 'ti': 'Tue', 'ke': 'Wed', 'to': 'Thu', 'pe': 'Fri', 'la': 'Sat', 'su': 'Sun'})
    pvm_df['Month'] = pvm_df['Month'].map(
        {'tammi': 1, 'helmi': 2, 'maalis': 3, 'huhti': 4, 'touko': 5, 'kesä': 6, 'heinä': 7, 'elo': 8, 'syys': 9, 'loka': 10, 'marras': 11, 'joulu': 12})
    pvm_df['Hour'] = pvm_df['Hour'].str.split(":").str[0]
    pvm_df = pvm_df.astype(
        {'Weekday': object, 'Day': int, 'Month': int, 'Year': int, 'Hour': int})
    pvm_df["Date"] = pd.to_datetime(pvm_df[["Year", "Month", "Day", "Hour"]])
    df.drop('Päivämäärä', axis=1, inplace=True)
    return df.set_index(pvm_df["Date"])


def bicycle_timeseries() -> pd.DataFrame:
    df = pd.read_csv("src/Helsingin_pyorailijamaarat.csv", sep=";")
    df = df.dropna(how="all", axis=1).dropna(how="all", axis=0)
    df = split_date(df)
    return df


def commute() -> pd.DataFrame:
    df = bicycle_timeseries()
    df = df.loc["2017-08", :]
    df = df.groupby(df.index.weekday).sum()
    df = df.rename(index={0: 'Mon', 1: 'Tue', 2: 'Wed',
                          3: 'Thu', 4: 'Fri', 5: 'Sat', 6: 'Sun'})
    return df


def main():
    data = commute()
    plt.plot(data)
    plt.show()


if __name__ == "__main__":
    main()
