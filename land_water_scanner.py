import numpy as np
import pandas as pd


# reads Land_Water_Access.csv and returns a pandas array of arrays
def land_water_scanner(file_name):
    # df = pd.read_csv("Land_Water_Access.csv")
    producer_accesses = {}
    fp = open(file_name)
    fp = fp.read()
    
    fp = fp.split('\n')

    for row in fp:
        access = row.split(",")
        producer = access[0]
        producer_accesses[producer] = [access[1], access[2]]
    

    return producer_accesses

def water_access(file_name, producer):
    producer_accesses = land_water_scanner(file_name)

    return producer_accesses[producer][1]


def land_access(file_name, producer):
    producer_accesses = land_water_scanner(file_name)

    return producer_accesses[producer][0]

if __name__ == "__main__":
    print(land_water_scanner("Land_Water_Access.csv"))
    print(water_access("Land_Water_Access.csv", "AFC"))
    print(water_access("Land_Water_Access.csv", "BXF"))


    
    
