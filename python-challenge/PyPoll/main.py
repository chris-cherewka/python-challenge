import csv, os

csvpath = os.path.join("Resources", "PyPoll_Resources_election_data.csv")
analyzed_data = os.path.join("Resources", "election_results.txt")

with open(csvpath, newline='') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    print(csvreader)
    csv_header = next(csvreader)
    
    #Declaring variables
    votes = []
    county = []
    candidates = []
    khan = []
    correy = []
    li = []
    otooley = []


    for row in csvreader:
        votes.append(row[0])
        county.append(row[1])
        candidates.append(row[2])

    #VOTE COUNT
    total_votes = (len(votes))
    #print(total_votes)

    #Votes by Person
    for candidate in candidates:
        if candidate == "Khan":
            khan.append(candidates)
            khan_votes = len(khan)
        elif candidate == "Correy":
            correy.append(candidates)
            correy_votes = len(correy)
        elif candidate == "Li":
            li.append(candidates)
            li_votes = len(li)
        else:
            otooley.append(candidates)
            otooley_votes = len(otooley)
    #print(khan_votes)
    #print(correy_votes)
    #print(li_votes)
    #print(otooley_votes)
    
    
    #Percentages
    khan_percent = round(((khan_votes / total_votes) * 100), 2)
    correy_percent = round(((correy_votes / total_votes) * 100), 2)
    li_percent = round(((li_votes / total_votes) * 100), 2)
    otooley_percent = round(((otooley_votes / total_votes) * 100), 2)
    #print(khan_percent)
    #print(correy_percent)
    #print(li_percent)
    #print(otooley_percent)
    
    #Winner 
    if khan_percent > max(correy_percent, li_percent, otooley_percent):
        winner = "Khan"
    elif correy_percent > max(khan_percent, li_percent, otooley_percent):
        winner = "Correy"  
    elif li_percent > max(correy_percent, khan_percent, otooley_percent):
        winner = "Li"
    else:
        winner = "O'Tooley"

#Print Statements

results = (
f"Election Results\n"
f"-----------------------------------\n"
f"Total Votes: {total_votes}\n"
f"-----------------------------------\n"
f"Khan: {khan_percent}% ({khan_votes})\n"
f"Correy: {correy_percent}% ({correy_votes})\n"
f"Li: {li_percent}% ({li_votes})\n"
f"O'Tooley: {otooley_percent}% ({otooley_votes})\n"
f"-----------------------------------\n"
f"Winner: {winner}\n"
f"-----------------------------------\n"
)

print(results)

with open(analyzed_data, 'w') as txt_file:
    txt_file.write(results)