import csv, os

csvpath = os.path.join("Resources", "PyBank_Resources_budget_data.csv")
analyzed_data = os.path.join("Resources", "output.txt")

with open(csvpath, newline='') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    #print(csvreader)
    csv_header = next(csvreader)
    month = []
    revenue = []
    revenue_change = []
    monthly_change = []
    #print(f"Header: {csv_header}")
    
    for row in csvreader:
        
        #setting months list equal to the first column in data set
        month.append(row[0])
        #print(row[0])
        
        #setting revenue list equal to the second column in dataset
        revenue.append(row[1])
        #print(row[1])
        
    total_months = len(month)
    #print(total_months)
    
    #setting all revenues values as integers in data set
    revenue_intial = map(int, revenue)
    total_revenue = (sum(revenue_intial))
    #print(total_revenue)
    
#calculating average change in dataset
    i = 0
    for i in range(len(revenue)-1):
        
        #row after iterating row - iterating row = PNL
        PNL = int(revenue[i + 1]) - int(revenue[i])
        #print(PNL)
        revenue_change.append(PNL)
    Total = sum(revenue_change)
    #print(revenue_change)
    
    monthly_change = round(Total / len(revenue_change), 2)
    #print(monthly_change)
    
#Greatest Increase
    profit_increase = max(revenue_change)
    #print(profit_increase)
    
    #increase month
    inc_month = revenue_change.index(profit_increase)
    month_increase = month[inc_month+1]
    #print(month_increase)

#Greatest Decrease
    profit_decrease = min(revenue_change)
    #print(profit_decrease)
    dec_month = revenue_change.index(profit_decrease)
    month_decrease = month[dec_month+1]
    #print(month_decrease)
    
#Printing
output = (
f'Financial Analysis'+'\n'
f'----------------------------'+'\n'
f"Total number of months: {total_months}\n"

f"Total Revenue in period: ${total_revenue}\n"
      
f"Average monthly change in Revenue: {str(monthly_change)}\n"

f"Greatest Increase in Profits: {month_increase} (${profit_increase})\n"

f"Greatest Decrease in Profits: {month_decrease} (${profit_decrease})"
)
print(output)

with open(analyzed_data, 'w') as txt_file:
    txt_file.write(output)