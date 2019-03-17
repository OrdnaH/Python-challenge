import os
import csv
import sys

total_votes = 0
candidate = []
candidates = [] 
votecount = []
votesfor = {}
votepct = []
victor = 0 

def rounded(votepct):
    return [('%.3f' % n) for n in votepct]

csvpath = os.path.join('election_data.csv')

with open(csvpath) as csvfile:
    csvreader = csv.reader(csvfile)
    csv_header = next(csvreader)
    
    for row in csvreader:
        candidate = row[2]
        total_votes += 1
        try:
            if candidate not in candidates:
                candidates.append(row[2])
                votesfor[row[2]] = 1
            else:
                votesfor[row[2]] += 1
        except IndexError:
            pass

    for (key, value) in votesfor.items(): 
        if value not in votepct:
            votepct.append((value*100/total_votes))
            votecount.append(value)

victor = max(votesfor, key=votesfor.get)
votepct = rounded(votepct)

print(f"Election Results\n-------------------------\nTotal Votes: {total_votes}\n-------------------------")
for i in range (0, 4):
    print(f"{candidates[i]}: {votepct[i]}% ({votecount[i]})")

print(f"-------------------------\nWinner: {victor}\n-------------------------")

with open('results.txt', 'w') as f:
    print(f"Election Results\n-------------------------\nTotal Votes: {total_votes}\n-------------------------", file=f)

    for i in range (0, 4):
        print(f"{candidates[i]}: {votepct[i]}% ({votecount[i]})", file=f)

    print(f"-------------------------\nWinner: {victor}\n-------------------------", file=f)