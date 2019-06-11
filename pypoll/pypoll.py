import os
import csv
import sys
# variables
total_votes = 0
candidate = []
candidates = [] 
votecount = []
votesfor = {}
votepct = []
victor = 0 
# function for calculating vote percentages
def rounded(votepct):
    return [('%.3f' % n) for n in votepct]
# open csv and iterate (loop) through data while performing calculations
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
#output results
print(f"Election Results\nTotal Votes: {total_votes}")
for i in range (0, 4):
    print(f"{candidates[i]}: {votepct[i]}% ({votecount[i]})")
print(f"Winner: {victor}")

with open('results.txt', 'w') as f:
    print(f"Election Results\n-------------------------\nTotal Votes: {total_votes}\n-------------------------", file=f)
    for i in range (0, 4):
        print(f"{candidates[i]}: {votepct[i]}% ({votecount[i]})", file=f)
    print(f"-------------------------\nWinner: {victor}\n-------------------------", file=f)