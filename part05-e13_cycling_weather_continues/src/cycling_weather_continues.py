#!/usr/bin/env python3


import pandas as pd
from sklearn import linear_model


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
    return pd.concat([pvm_df, df], axis=1)


def cycling_weather() -> pd.DataFrame:
    bike_df = split_date_continues()
    bike_df = bike_df[bike_df['Year'] == 2017].groupby(
        ['Year', 'Month', 'Day']).sum().reset_index()
    weather_df = pd.read_csv('src/kumpula-weather-2017.csv')
    merged = pd.merge(bike_df, weather_df, left_on=[
        'Year', 'Month', 'Day'], right_on=['Year', 'm', 'd'])
    merged.drop(['m', 'd', 'Time', 'Time zone'], axis=1, inplace=True)
    merged = merged.ffill()
    return merged


def cycling_weather_continues(station):
    df = cycling_weather()
    model = linear_model.LinearRegression(fit_intercept=True)
    y = df[station]
    X = df[['Precipitation amount (mm)',
            'Snow depth (cm)', 'Air temperature (degC)']]
    model.fit(X, y)
    coefs = model.coef_
    return coefs, model.score(X, y)


def main():
    place = 'Merikannontie'
    coef, scor = cycling_weather_continues(place)
    print(f"Measuring station: {place}")
    print(
        f"Regression coefficient for variable 'precipitation': {coef[0]:.1f}")
    print(f"Regression coefficient for variable 'snow depth': {coef[1]:.1f}")
    print(f"Regression coefficient for variable 'temperature': {coef[2]:.1f}")
    print(f"Score: {scor:.2f}")


if __name__ == "__main__":
    main()
