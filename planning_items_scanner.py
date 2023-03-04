import pandas as pd
def planning_items_scanner(file_name):
    '''
    reads the passed in file and returns a list of lists for the data in the CSV file
    :param file_name: string
    :return: file_pointer: list of lists
    '''
    df = pd.read_csv(file_name)
    return df

if __name__ == "__main__":
    print(planning_items_scanner("FY21_Planning_Items.csv"))