# This program will tell the sales prediction
# Date
# CTI-110 P2T1 - Sales Prediction
# Jose Porras
# Get the projected total sales.
total_sales = float(input('Enter the projected sales: '))

#calculate the profit as 23 percent of total sales.
profit = total_sales * 0.23

# Display the profit.
print('The profit is $', format(profit, ',.2f'))
