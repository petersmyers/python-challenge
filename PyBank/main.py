#Reading in a .csv file
import os
import csv

csvpath = os.path.join('budget_data.csv')
with open(csvpath, newline = '') as csvfile:
    csvbudget = csv.reader(csvfile, delimiter = ',')
    print(csvbudget)
    csv_header = next(csvbudget)
    print(f"CSV Header: {csv_header}")
    rowcount = sum(1 for row in csvbudget)
    print(rowcount)
    count = 1
    firstrow = csvbudget(1)
    date = firstrow[0]
    print(firstrow)
    for row in csvbudget:
        if date != row[0]:
            count = count + 1
            date = row[0]
    print(str(count))
    # months = len(csvbudget)
    # print(f"{months}")

