
#initial imports
import os
import csv

os.system('cls')

csvpath = os.path.join('PyBank', 'Resources', 'budget_data.csv')

#defining variables
months = []
prof_loss = 0
pl_list = []
changes = []
big_change = 0
bc_name = ""
small_change = 0
sc_name = ""

#reading csv file
with open(csvpath, 'r') as csvfile:

    csvreader = csv.reader(csvfile, delimiter = ',')
    csv_header = next(csvreader)

    #adds values of csv to list variables
    for row in csvreader:

        months.append(row[0])
        prof_loss = prof_loss + int(row[1])
        pl_list.append(int(row[1]))

#finds each change between months, ignores initial value
for x in range(len(months)):

    if x == 0:

        continue
        
    else:
            
        changes.append((int(pl_list[x]) - (int(pl_list[x - 1]))))

#average function
def av(list):

    return sum(list) / len(list)

#tracks which change is the greatest increase and decrease
for x in range((len(months)) - 1):

    if x == -1:

        continue

    elif changes[x] > big_change:

        big_change = changes[x]
        bc_name = months[x + 1]
    
    elif changes[x] < small_change:

        small_change = changes[x]
        sc_name = months[x + 1]

#prints results to terminal
print("Financial Analysis")
print("\n")
print("-------------------")
print("\n")
print("Total Months: " + str(len(months)))
print("\n")
print("Total: $" + str(prof_loss))
print("\n")
print("Average Change: $" + str(round(av(changes), 2)))
print("\n")
print("Greatest Increase in Profits: " + bc_name + " ($" + str(big_change) + ")")
print("\n")
print("Greatest Decrease in Profits: " + sc_name + " ($" + str(small_change) + ")")

textpath = os.path.join('PyBank', 'Analysis', 'Bank.txt')

#writes results to text file
with open(textpath, 'w') as f:
    f.write("Financial Analysis")
    f.write("\n")
    f.write("-------------------")
    f.write("\n")
    f.write("Total Months: " + str(len(months)))
    f.write("\n")
    f.write("Total: $" + str(prof_loss))
    f.write("\n")
    f.write("Average Change: $" + str(round(av(changes), 2)))
    f.write("\n")
    f.write("Greatest Increase in Profits: " + bc_name + " ($" + str(big_change) + ")")
    f.write("\n")
    f.write("Greatest Decrease in Profits: " + sc_name + " ($" + str(small_change) + ")")