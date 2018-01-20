#!/bin/env python
import pandas as pd
import numpy as np


if __name__ == "__main__":
    path = "data/resultadosfinais2014.csv"
    df = pd.read_csv(path)
    df.drop(['ano'], 1, inplace=True)
    print(df)
