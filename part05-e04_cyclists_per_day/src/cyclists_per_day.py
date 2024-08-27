#!/usr/bin/env python3

import pandas as pd
import matplotlib.pyplot as plt


def split_date(df) -> pd.DataFrame:
    pvm_df = df['Päivämäärä'].str.split(expand=True)
    pvm_df.columns = ['Weekday', 'Day', 'Month', 'Year', 'Hour']
    pvm_df['Weekday'] = pvm_df['Weekday'].map(
        {'ma': 'Mon', 'ti': 'Tue', 'ke': 'Wed', 'to': 'Thu', 'pe': 'Fri', 'la': 'Sat', 'su': 'Sun'})
    pvm_df['Month'] = pvm_df['Month'].map(
        {'tammi': 1, 'helmi': 2, 'maalis': 3, 'huhti': 4, 'touko': 5, 'kesä': 6, 'heinä': 7, 'elo': 8, 'syys': 9, 'loka': 10, 'marras': 11, 'joulu': 12})
    pvm_df['Hour'] = pvm_df['Hour'].str.split(":").str[0]
    return pvm_df.astype({'Weekday': object, 'Day': int, 'Month': int, 'Year': int, 'Hour': int})


def split_date_continues() -> pd.DataFrame:
    df = pd.read_csv("src/Helsingin_pyorailijamaarat.csv", sep=";")
    df = df.dropna(how="all", axis=1).dropna(how="all", axis=0)
    pvm_df = split_date(df)
    df.drop('Päivämäärä', axis=1, inplace=True)
    return pd.concat([pvm_df, df], axis=1).reindex(df.index)


def cyclists_per_day() -> pd.DataFrame:
    bike_df = split_date_continues()
    bike_df = bike_df.drop('Hour', axis=1)
    bike_df = bike_df.groupby(["Year", "Month", "Day"]).sum()
    return bike_df


def main():
    bike_df = cyclists_per_day()
    plot_data = bike_df.loc[(2017, 8), :]
    plt.plot(plot_data)
    plt.xticks(plot_data.index)
    plt.show()


if __name__ == "__main__":
    main()
