# i0

import pandas as pd
# Read the CSV file
df = pd.read_csv("FY21_Planning_Items.csv")
distributions = []
sucessfulDeliveries = pd.read_csv("FY21_LFM_Order_Items.csv")
for index, row in sucessfulDeliveries.iterrows():
    distributions.append(str(row["Distribution Date"]))

def getTotalDeliveries(company):
  totalDeliveries = 0
  for index, row in df.iterrows():
    # Access data for each column by column name
    if row["Producer Code"] == company:
      totalDeliveries += 1
  return totalDeliveries

def withinWeek(week, distribution):
  week = week.split(" ")
  week = week[0].split("/")
  week = week[2] + week[0] + week[1]
  distribution = distribution.split(" ")
  distribution = distribution[0].split("/")
  distribution = distribution[2] + distribution[0] + distribution[1]
  if int(week) - 7 <= int(distribution) <= int(week):
    return True
  return False

def getFailedDeliveries(company):
  failedDeliveries = 0
  for index, row in df.iterrows():
    # Access data for each column by column name
    if row["Producer Code"] == company:
      for distribution in distributions:
        if withinWeek(str(row["Delivery Week"]), distribution):
          failedDeliveries += 1
          break
  return failedDeliveries

def getProbabilityACompanyWillFailDelivery(company):
  totalDeliveries = getTotalDeliveries(company)
  failedDeliveries = getFailedDeliveries(company)
  return failedDeliveries / totalDeliveries * 100
  
print("%.2f" % getProbabilityACompanyWillFailDelivery("NTN"))