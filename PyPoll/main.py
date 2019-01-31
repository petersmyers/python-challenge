#Reading in a .csv file
import os
import csv

csvpath = os.path.join('election_data.csv')
with open(csvpath, newline = '') as csvfile:
    csvvote = csv.reader(csvfile, delimiter = ',')
    print(csvvote)
    
    # Grab the header and take a look at the columns
    csv_header = next(csvvote)
    print(f"CSV Header: {csv_header}")

    # GIMME A LIST!
    csvvote = list(csvvote)

    # Count the number of rows as each row corresponds to a different month
    rowcount = sum(1 for row in csvvote)
    
    # Set total to zero so we have a baseline for accounting.
    total = sum((int(row[1])) for row in csvvote)
    
    # Get the names of the candidates
    candidates = [csvvote[0][2]]
    votes = [0]
    for row in csvvote:
        for i in candidates:
            if candidates[i]==row[2]:
                votes[i] +- 1
            else:
                candidates [i+1]= row[2]
                votes[i+1] = 1
    winner = max(votes)

    # Print the results
    # Bet Uncle Cleetus didn't do it this fast!
    print("The Election Results are in!")
    print("****************************")
    print(f"There were {rowcount} engaged citizens this election!")
    print("****************************")
    print(f"Here's the spread:")
    for i in candidates:
        print(f"{candidates[1]} received {(votes[1]/rowcount)*100}% of the votes ({votes[i]})")
    print("****************************")
    print(f"The winner of this election for an ambiguous office is...")
    print("** drum roll **")
    print(f"{winner.upper}!!!!!")

    # Now we have the PLEASURE of writing our results to a file.
    out_csvpath = os.path.join('election_results.txt')
    with open(out_csvpath, 'w', newline='') as txtfile:
        txtwriter=txt.writer(txtfile, delimiter = ',')
        txtwriter.writerow("Summary of the Profits and Losses")


