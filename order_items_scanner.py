import numpy as np
import pandas as pd


# reads Land_Water_Access.csv and returns a list of lists
def order_items_scanner(file_name):
    order_log = pd.read_csv(file_name)

    
    return order_log


print(order_items_scanner("FY22_LFM_Order_Items.csv"))
