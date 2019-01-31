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

    # Get the names of the candidates
    candidates = [csvvote[0][2]]
    votes = [0]
    for row in csvvote:
        keep = 0
        for i in range(0,len(candidates)):
            if keep == 0:
                if candidates[i]==row[2]:
                    votes[i] += 1
                    keep = 1
        if keep == 0:    
            candidates.append(row[2])
            votes.append(int(1))
    w = votes.index(max(votes))
    winner = candidates[w]
    # Print the results
    # Bet Uncle Cleetus didn't do it this fast!
    print("The Election Results are in!")
    print("****************************")
    print(f"There were {rowcount} engaged citizens this election!")
    print("****************************")
    print(f"Here's the spread:")
    for k in range(0,len(candidates)):
        print(f"{candidates[k]} received {round((votes[k]/rowcount)*100, 2)}% of the votes (n = {votes[k]})")
    print("****************************")
    print(f"The winner of this election for an ambiguous office is...")
    print("** DRUM ROLLLLL **")
    print(f"{winner}!!!!!")

    # Gotta keep a record of these results to make them legit!
    out_txtpath = os.path.join('election_results.txt')
    with open(out_txtpath, 'w') as text_file:
        text_file.write("The Election Results are in!\r")
        text_file.write("****************************\r")
        text_file.write(f"There were {rowcount} engaged citizens this election!\r")
        text_file.write("****************************\r")
        text_file.write(f"Here's the spread:\r")
        for k in range(0,len(candidates)):
            text_file.write(f"{candidates[k]} received {round((votes[k]/rowcount)*100, 2)}% of the votes (n = {votes[k]})\r")
        text_file.write("****************************\r")
        text_file.write(f"The winner of this election for an ambiguous office is...\r")
        text_file.write("** DRUM ROLLLLL **\r")
        text_file.write(f"{winner}!!!!!")
