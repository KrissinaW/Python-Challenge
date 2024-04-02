#Importing files

import os
import csv

#creating 
budget_data = os.path.join("budget_data.csv")

total_months = 0
total_profit_loss = 0
change_profit_loss = []
dates = []

#Read CSV file

with open(budget_data, newline= "") as csvfile:
    csv_reader = csv.reader(csvfile, delimiter=",")
    #skip header row
    next(csv_reader)

   # looping through rows in csv file
    for row in csv_reader:
        #count months
        total_months += 1

        #extract p/l dates
        profit_loss = int(row[1])
        dates_value = row[0]

        #calc total p/l
        total_profit_loss += profit_loss
        change_profit_loss.append(profit_loss)

        #store p/l/ and date
        dates.append(dates_value)

#calc changes in p/l
Changes= [change_profit_loss[i+1] - change_profit_loss[i] for i in range(len(change_profit_loss)-1)]

#calc avg change in p/l
average_change = sum(Changes) / len(Changes)

#Find greatest increase and decrease in profit
greatest_increase = max(Changes)
greatest_decrease = min(Changes)


#Find corresponding dates for greatest increase and decrease
max_increase_date = dates[Changes.index(greatest_increase)+1]
max_decrease_date = dates[Changes.index(greatest_decrease)+1]

#Print analysis
print("Financial Analysis")
print("------------------")
print(f"Total Months: {total_months}")
print(f"Total: ${total_profit_loss}")
print(f"Average Change: ${average_change: .2f}")
print(f"Greatest Increase in Profits: {max_increase_date} (${greatest_increase})")
print(f"Greatest Decrease in Profits: {max_decrease_date} (${greatest_decrease})")

#export to .txt file
output = open("output.txt", "w")

line1 = ("Financial Analysis")
line2 = ("------------------")
line3 = (f"Total Months: {total_months}")
line4 = (f"Total: ${total_profit_loss}")
line5 = (f"Average Change: ${average_change: .2f}")
line6 = (f"Greatest Increase in Profits: {max_increase_date} (${greatest_increase})")
line7 = (f"Greatest Decrease in Profits: {max_decrease_date} (${greatest_decrease})")
output.write('{}\n{}\n{}\n{}\n{}\n{}\n{}\n'.format(line1,line2,line3,line4,line5,line6,line7))
