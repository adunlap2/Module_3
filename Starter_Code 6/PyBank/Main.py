# First We need to import the Module and CVS file
import os
import csv
#specify the path to our data
csv_reader = os.path.join("", "Resources", "budget_data.csv")

#Open and read the data set
with open(csv_reader) as csvfile:
    reader = csv.reader(csvfile, delimiter=",")
    Header = next(reader)
#Define Variables
    profit_losses = []
    profit = 0
    months = 0
    increase = ["",0]
    decrease = ["",0]
    first_line = next(reader)
    months += 1
    profit += int(first_line[1])
    previous = int(first_line[1])
    #starting For loops
    for row in reader:
        months += 1
        profit += int(row[1])
        change = int(row[1]) - previous
        profit_losses.append(change)
        previous = int(row[1])
        if change > increase[1]:
            increase[1]=change
            increase[0]=row[0]
        if change < decrease[1]:
            decrease[1]=change
            decrease[0]=row[0]
avg_change = sum(profit_losses) / len(profit_losses)
output_path = os.path.join("Anylsis 2","budget_analysis.txt")
with open(output_path,"w") as file:
    result = (
    f"Financial Analysis\n"
    f"----------------------------\n"
    f"Total Months: {months}\n"
    f"Total: ${profit}\n"
    f"Average: {avg_change}\n"
    f"Change: {change}\n"
    f"Greatest Increase in Profits: {increase[0]} ${increase[1]}\n"
    f"Greatest Decrease in Profits: {decrease[0]} ${decrease[1]}\n"
    )
    print(result)
    file.write(result)

