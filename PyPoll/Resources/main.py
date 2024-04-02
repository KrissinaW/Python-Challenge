#Importing file

import os
import csv

#creating 
election_data = os.path.join("election_data.csv")

#list with cadidates names
candidates = []

#list num of votes
num_votes = []

#list to show the % of total voters 
percent_votes = []

#Counter for the number of votes
total_votes = 0

#Read CSV file
with open(election_data, newline="") as csvfile:
    csv_reader = csv.reader(csvfile, delimiter=",")
    #skip header row
    next(csv_reader)

   # looping through rows in csv file
    for row in csv_reader:
        #count votes
        total_votes += 1

        #if the cand is not on our list then add them along with a vote. If they are on the list we will add a vote. 
        if row[2] not in candidates:
            candidates.append(row[2])
            index = candidates.index(row[2])
            num_votes.append(1)
        else:
            index = candidates.index(row[2])
            num_votes[index] +=1

#Add to percent_vote list
    for votes in num_votes:
        percentage = (votes/total_votes) * 100
        percentage = "%.3f%%" % percentage
        percent_votes.append(percentage)

# Find winner
winner_index = num_votes.index(max(num_votes))
winning_can = candidates[winner_index]

#Show result
print("Election Results")
print("----------------------------")
print(f"Total Votes: {total_votes}")
print("----------------------------")
for i in range(len(candidates)):
    print(f"{candidates[i]}: {percent_votes[i]} ({num_votes[i]})")
print("-------------------------")
print(f"Winner: {winning_can}")
print("-------------------------")

#Export to .txt file
with open("output.txt", "w") as output:
    output.write ("Election Results\n")
    output.write ("----------------------------\n")
    output.write (f"Total Votes: {total_votes}\n")
    output.write ("----------------------------\n")
    for i in range(len(candidates)):
        output.write (f"{candidates[i]}: {percent_votes[i]} ({num_votes[i]})\n")
    output.write ("-------------------------\n")
    output.write (f"Winner: {winning_can}\n")
    output.write ("-------------------------\n")


