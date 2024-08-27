#!/usr/bin/env python3

import pandas as pd
import numpy as np


def missing_value_types() -> pd.DataFrame:
    df = pd.DataFrame({"Year of independence": ["-", "1917", "1776", "1523", "-", "1992"],
                       "President": ["-", "Niinistö", "Trump", "-", "Steinmeier", "Putin"]},
                      index=["United Kingdom", "Finland", "USA", "Sweden", "Germany", "Russia"])
    df["Year of independence"] = df["Year of independence"].replace(
        "-", np.nan).astype(float)
    df["President"] = df["President"].replace("-", None)
    return df


def main():
    print(missing_value_types())


if __name__ == "__main__":
    main()
