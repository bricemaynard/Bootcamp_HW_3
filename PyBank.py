import os
import csv

# Path to collect data from the Resources folder
pybank_csv = ('budget_data.csv')

months = {}
TotalProfitLosses = 0
change = 0
prev = 0
total = 0
greatest_increase = 0
sum_change = 0
otherchange = 0
otherprev = 0
othertotal = 9999999999999999999999999
greatest_decrease = 0
othersum_change = 0


with open(pybank_csv, 'r') as csvfile:

    # Split the data on commas
    csvreader = csv.reader(csvfile, delimiter=',')

    header = next(csvreader)

    # Loop through the data
    for row in csvreader:
      
      TotalProfitLosses = TotalProfitLosses + int(row[1])

      date = row[0]

      if date in months:
        months[date] = months[date] + 1
      else:
        months[date] = 1

      total = total + 1      
      if total > 1:

          change = int(row[1]) - prev

          sum_change = sum_change + change

          if change > greatest_increase:
              greatest_increase = change
              greatest_date = date

      prev = int(row[1])

      othertotal = othertotal + 1      
      if othertotal > 1:

          otherchange = int(row[1]) - otherprev

          othersum_change = othersum_change + otherchange

          if change < greatest_decrease:
              greatest_decrease = otherchange
              lowest_date = date

      otherprev = int(row[1])
average_change = round(sum_change/(len(months)-1), 2)

print("Financial Analysis")
print("------------------")
print("Total Months: " + str(len(months)))
print("Total: $"+str(TotalProfitLosses))
print("Average Change: $" + str(average_change))
print("Greatest Increase in Profits: " + str(greatest_date) + " $" + (str(greatest_increase)))
print("Greatest Decrease in Profits: " + str(lowest_date) + " $" + (str(greatest_decrease)))

with open('PyBankAnalysis.txt', 'w') as text:
  text.write("Financial Analysis" + "\n")
  text.write("------------------\n")
  text.write("Total Months: " + str(len(months))+"\n")
  text.write("Total: $"+str(TotalProfitLosses)+"\n")
  text.write("Average Change: $" + str(average_change)+"\n")
  text.write("Greatest Increase in Profits: " + str(greatest_date) + " $" + (str(greatest_increase))+"\n")
  text.write("Greatest Decrease in Profits: " + str(lowest_date) + " $" + (str(greatest_decrease))+"\n")


