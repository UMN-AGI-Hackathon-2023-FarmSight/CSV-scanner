import pandas as pd
import numpy as np

FILENAME_PLANNED = 'FY22_Planning_Items.csv'
FILENAME_REAL = 'FY22_LFM_Order_Items.csv'

# Read in the data
planned = pd.read_csv(FILENAME_PLANNED)
real = pd.read_csv(FILENAME_REAL)

# convert the pd to np
planned_np = planned.to_numpy()
real_np = real.to_numpy()

print(planned["Delivery Week"])
print("____________________________")
print(real["Delivery Week"])