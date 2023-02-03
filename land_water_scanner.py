import numpy as np
import pandas as pd


# reads Land_Water_Access.csv and returns a pandas array of arrays
def land_water_scanner():
    df = pd.read_csv("Land_Water_Access.csv")
    return df

if __name__ == "__main__":
    print(land_water_scanner())
