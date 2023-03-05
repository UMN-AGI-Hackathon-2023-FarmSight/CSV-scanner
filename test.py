def order_items_scanner(file_name, year):
    fp = open(file_name, "r")
    fp = fp.read()
    fp = fp.split('\n')

    
    for line in fp:
        item = line.split(",")
        print(item)


order_items_scanner("FY22_LFM_Order_Items.csv", 2022)
