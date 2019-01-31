#Reading in a .csv file
import os
import csv

csvpath = os.path.join('budget_data.csv')
with open(csvpath, newline = '') as csvfile:
    
    # Creates an evil object called a "csv.reader"
    # This is an iterator, so whenever you touch a row, it goes poof!
    # And is never seen again. 
    csvbudget = csv.reader(csvfile, delimiter = ',')
    print(csvbudget)
    
    # Grab the header and take a look at the columns
    csv_header = next(csvbudget)
    print(f"CSV Header: {csv_header}")

    # Turn that iterator into a list!
    # Now the thing can be manipulated till the fucking cows come home.
    csvbudget = list(csvbudget)

    # Count the number of rows as each row corresponds to a different month
    rowcount = sum(1 for row in csvbudget)
    
    # Set total to zero so we have a baseline for accounting.
    total = sum((int(row[1])) for row in csvbudget)
    
    # Get the average change of P/L
    # Also going to look for the gretest loss and profit months
    # Let's set some baseline variables for our for-loop
    PLavg = 0
    loss = (int(csvbudget[1][1]) - int(csvbudget[0][1]))
    profit = (int(csvbudget[1][1]) - int(csvbudget[0][1]))
    lowest = 0
    highest = 0

    # For-loop: GO!
    # Starting at 1 because we need to be able to subtract the row above.
    # Could also have started at 0 and then not included last row. Either or. 
    for i in range(1,len(csvbudget)):
        PnL = (int(csvbudget[i][1]) - int(csvbudget[i-1][1]))
        PLavg += PnL
        if loss > PnL:
            loss = PnL
            lowest=i
        elif profit < PnL:
            profit = PnL
            highest = i
    PLavg = PLavg/(len(csvbudget)-1)
    
    # Print some shit and see if it matches the Assignment
    print(f"Total months: {rowcount}")
    print(f"Total: ${total}")
    print(f"Average change: ${round(PLavg,2)}")
    print(f"Month of greatest prosperity: {csvbudget[highest][0]} (${profit})")
    print(f"Month of epic sadness: {csvbudget[lowest][0]} (${loss})")

    # Now we have the PLEASURE of writing our results to a file.
    out_txtpath = os.path.join('ProfitLoss_Summary.txt')
    with open(out_txtpath, 'w') as text_file:
        # txtwriter=txt.writer(txtfile, delimiter = ',')
        text_file.write("Summary of the Profits and Losses\r")
        text_file.write(f"Total months: {rowcount}\r")
        text_file.write(f"Total: ${total}\r")
        text_file.write(f"Average change: ${round(PLavg,2)}\r")
        text_file.write(f"Month of greatest prosperity: {csvbudget[highest][0]} (${profit})\r")
        text_file.write(f"Month of epic sadness: {csvbudget[lowest][0]} (${loss})\r")


