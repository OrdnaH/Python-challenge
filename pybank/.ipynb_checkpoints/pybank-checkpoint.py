import os
import csv

num_months = 0
total_net = 0
prior_month = 0
net_change = []
months = []
current_month = []

csvpath = os.path.join('budget_data.csv')
with open(csvpath) as csvfile:
    csvreader = csv.reader(csvfile)
    csv_header = next(csvreader)
    
    for row in csvreader:
        revenue = int(row[1])
        month = [row[0]]
        months.append(month)
        num_months += 1
        total_net += revenue

        monthly_change = revenue - prior_month
        prior_month = revenue
        net_change += [monthly_change]
        current_month += month
        
max_inc = max(net_change)
max_dec = min(net_change)
max_month = months[net_change.index(max(net_change))]
min_month = months[net_change.index(min(net_change))]
max_month = max_month[0]
min_month = min_month[0]
net_change = sum(net_change[1:])

print(f"Financial Analysis\nTotal Months: {num_months}\nTotal: ${total_net}\nAverage Change: ${net_change/(num_months-1):.2f}")
print(f"Greatest Increase in Profits: {max_month} (${max_inc})\nGreatest Decrease in Profits: {min_month} (${max_dec})")

with open('results.txt', 'w') as f:
    print(f"Financial Analysis\nTotal Months: {num_months}\nTotal: ${total_net}\nAverage Change: ${net_change/(num_months-1):.2f}", file=f)
    print(f"Greatest Increase in Profits: {max_month} (${max_inc})\nGreatest Decrease in Profits: {min_month} (${max_dec})", file=f)