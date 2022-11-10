
#initial imports
import os
import csv

os.system('cls')

csvpath = os.path.join('PyPoll', 'Resources', 'election_data.csv')

#defining variables
candidates = []
vote_breakdown = {}
dict = {}
winner = ""
winner_v = 0

#reading csv file
with open(csvpath, 'r') as csvfile:

    csvreader = csv.reader(csvfile, delimiter = ',')
    csv_header = next(csvreader)

    #adds to list of candidates
    for row in csvreader:

        dict[row[0]] = row[2]
        if candidates.count(row[2]) > 0:
            continue
        else:
            candidates.append(row[2])

    #adds to dictionary of votes
    for i in range(len(candidates)):

        vote_count = 0
        for row in dict:

            if dict[row] == candidates[i]:

                vote_count = vote_count + 1
        
        vote_breakdown[candidates[i]] = vote_count

#percentage function
def perc(v, sum):

    return round((v / sum) * 100, 3)

#finds total number of votes
total = len(dict)

#prints results to terminal
print("Election Results")
print("\n")
print("------------------")
print("\n")
print("Total Votes: " + str(total))
print("\n")
print("------------------")
print("\n")
#for loop that prints results of each candidate, no matter the number of candidates
for candidate in candidates:
    for votes in vote_breakdown:
        if votes == candidate:
            print(candidate + ": " + str(perc(vote_breakdown[votes], total)) + "% (" + str(vote_breakdown[votes]) + ")")
            if vote_breakdown[votes] > winner_v:
                winner = candidate
                winner_v = vote_breakdown[votes]

print("\n")
print("------------------")
print("\n")
print("Winner: " + winner)

textpath = os.path.join('PyPoll', 'Analysis', 'Poll.txt')

#writes results to text file
with open(textpath, 'w') as f:

    f.write("Election Results")
    f.write("\n")
    f.write("------------------")
    f.write("\n")
    f.write("Total Votes: " + str(total))
    f.write("\n")
    f.write("------------------")
    f.write("\n")
    for candidate in candidates:
        for votes in vote_breakdown:
            if votes == candidate:
                f.write(candidate + ": " + str(perc(vote_breakdown[votes], total)) + "% (" + str(vote_breakdown[votes]) + ")")
                f.write("\n")
                if vote_breakdown[votes] > winner_v:
                    winner = candidate
                    winner_v = vote_breakdown[votes]
    
    f.write("\n")
    f.write("------------------")
    f.write("\n")
    f.write("Winner: " + winner)
