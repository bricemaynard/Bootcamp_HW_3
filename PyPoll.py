import os
import csv

# Path to collect data from the Resources folder
pypoll_csv = ('election_data.csv')

candidates = []
totalvotes = 0
votecountbycan = []


with open (pypoll_csv, 'r') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')

    header = next(csvreader)

    for row in csvreader:
        totalvotes = totalvotes + 1
        candidate = row[2]

        if candidate in candidates:
            candidate_index = candidates.index(candidate)
            votecountbycan[candidate_index] = votecountbycan[candidate_index] + 1

        else:
            candidates.append(candidate)
            votecountbycan.append(1)

votepercentbycan = []
max_votes = votecountbycan[0]
max_index = 0

for x in range(len(candidates)):
    percentageofvote = round(votecountbycan[x]/totalvotes*100, 2)
    votepercentbycan.append(percentageofvote)

    if votecountbycan[x] > max_votes:
        max_votes = votecountbycan[x]
        max_index = x

election_winner = candidates[max_index]

print("Election Results!")
print("-----------------")
print(f"Total Votes: {totalvotes}")
print("-----------------")
for x in range(len(candidates)):
    print(f"{candidates[x]}: {votepercentbycan[x]}% ({votecountbycan[x]})")
print("-----------------")
print(f"Winner: {election_winner}")
print("-----------------")

with open('PyPollAnalysis.txt', 'w') as text:
  text.write("Election Results" + "\n")
  text.write("---------------------\n")
  text.write(f"Total Votes: {totalvotes}""\n")
  text.write("---------------------\n")
  for x in range(len(candidates)):
    text.write(f"{candidates[x]}: {votepercentbycan[x]}% ({votecountbycan[x]})""\n")
  text.write("---------------------\n")
  text.write(f"Winnder: {election_winner}""\n")
  text.write("---------------------\n")
