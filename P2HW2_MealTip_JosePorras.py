#This program will calculate the total amount of a meal and tip.
#2-19-19
#CTI-110 P2HW2- Meal Tip Calculator
#Jose Porras

#Get the total amount of meal purchase
totalmealpurchased = float(input("Enter the charge for the food: "))

#calculate the tip(15%)
tip1 = totalmealpurchased * .15
tip2 = totalmealpurchased * .18
tip3 = totalmealpurchased * .20

#the total of the meal and tip
totalpurchased1 =(totalmealpurchased + tip1)
totalpurchased2 =(totalmealpurchased + tip2)
totalpurchased3 =(totalmealpurchased + tip3)

#display the total amount of meal
print("Amount of the meal purchase :$",format(totalmealpurchased ,',.2f'))

#display the tip
print("Amount of the tip of 15% :$",format(tip1 ,',.2f'))
print("Amount of the tip of 18% :$",format(tip2 ,',.2f'))
print("Amount of the tip of 20% :$",format(tip3 ,',.2f'))

#display the total purchase
print("Amount of the total purchased :$",format(totalpurchased1 ,'.2f'))
print("Amount of the total purchased :$",format(totalpurchased2 ,'.2f'))
print("Amount of the total purchased :$",format(totalpurchased3 ,'.2f'))



