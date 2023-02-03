import numpy as np
import pandas as pd


# reads Land_Water_Access.csv and returns a list of lists
def land_water_scanner():
    # # open file
    # file = open("Land_Water_Access.csv", "r")
    # # read file
    # file = file.read()
    # # split file into lines
    # file = file.split("\n")
    # # split lines into lists
    # for i in range(len(file)):
    #     file[i] = file[i].split(",")
    # # return list of lists
    # return file

    df = pd.read_csv("Land_Water_Access.csv")
    return df

# if __name__ == "__main__":
#     print(land_water_scanner())
