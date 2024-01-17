#import dictionaries
import csv
import os
#Pull the CSV file
csv_reader = os.path.join("","Resources","election_data.csv")
#open CSV File
with open(csv_reader) as csvfile:
    reader = csv.reader(csvfile, delimiter=",")
    header = next(reader)
    first_row = next(reader)
# Define varibles
    total_votes = 0
    canidate = {}
    winner = [0, ""]
    output = 0
    total_votes += 1
#Start for loop
    for row in reader:
        total_votes += 1
        canidate_name = row[2]
        if canidate_name not  in canidate.keys():
            canidate[canidate_name]=0
        canidate[canidate_name]+=1

output_path = os.path.join("PyPoll Analysis","election_data.txt")
with open(output_path, "w") as file:
        result = f'''
        Election Results
        -------------------------
        Total Votes: {total_votes}
        -------------------------
        '''
        for canidate_name in canidate.keys():
            result = f'{canidate_name}: {canidate[canidate_name] / total_votes * 100:.2f}% ({canidate[canidate_name]:,})\n'
            result += f'------------------\nWinner: {winner[1]}\n----------------------'
            print(result)
        file.write(result)






    #reader = csv.reader(csvfile, delimiter=",")
    #Header = next(reader)