#!/usr/bin/env python3

import pandas as pd


def suicide_fractions() -> pd.Series:
    df = pd.read_csv("src/who_suicide_statistics.csv")
    df = df.drop(["year", "age", "sex"], axis=1)
    df['rate'] = df['suicides_no'] / df['population']
    df = df.groupby("country").mean()
    return pd.Series(df["rate"], index=df.index)


def suicide_weather() -> tuple:
    df_weather = pd.read_html(
        "src/List_of_countries_by_average_yearly_temperature.html", index_col="Country", header=0)[0]
    df_weather = pd.Series(df_weather.iloc[:, 0], index=df_weather.index)
    df_weather = df_weather.str.replace("\u2212", "-").astype(float)
    df_suicides = suicide_fractions()
    spearman = df_weather.corr(df_suicides, method="spearman")
    shared = len(df_suicides.index.intersection(df_weather.index))
    return (df_suicides.shape[0], df_weather.shape[0], shared, spearman)


def main():
    values = suicide_weather()
    print(f'Suicide DataFrame has {values[0]} rows')
    print(f'Temperature DataFrame has {values[1]} rows')
    print(f'Common DataFrame has {values[2]} rows')
    print(f'Spearman correlation: {values[3]}')


if __name__ == "__main__":
    main()
