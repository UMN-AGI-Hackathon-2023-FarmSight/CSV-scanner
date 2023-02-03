import numpy as np
import pandas as pd


# reads Land_Water_Access.csv and returns a numpy array of arrays
def land_water_scanner():
    arr = np.loadtxt("Land_Water_Access.csv", delimiter=",", dtype=str)
    return arr

# if __name__ == "__main__":
#     print(land_water_scanner())
