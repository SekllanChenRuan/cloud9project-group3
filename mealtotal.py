# mealtotal.py

 
# This program will recieve input from user on the 
# meal amount, tip percent, and tax rate(%).
# Then it will calculate the total amount.
 

# steps
# 1. input meal amount
# 2. input tip percent
# 3. input tax rate
# 4. calculate 
# 5. display total

# by sekllan chenruan

#mealAmount function: returns the entered meal amount
def mealAmount():
    mealAmount = float(input("Enter the meal amount: "))
    return mealAmount

#tipPercent function: returns the tip percentage
def tipPercent():
    tip = float(input("Enter tip percent: "))
    return tip

#taxrate function: returns tax rate
def taxrate():
    taxrate = float(input("Enter the tax: "))
    return taxrate

def calculateTip():
    #calls the mealamount function, tipPercent function, and taxrate function
    amount = mealAmount()
    tip = tipPercent()
    tax = taxrate()
    
    #tipamount is amount * tip%
    tipamount = amount * tip
    #taxamount is amount * tax rate
    taxamount = amount * tax
    
    #final cost is the sum of everything
    finalcost = amount + tipamount + taxamount
    #rounds the finalcost
    finalcost = round(finalcost,2)
    display(finalcost)

def display(total):
    #this function outputs the total
    print("The total is $", total)


def main():
    #calls calculateTip function
    calculateTip()

main()

    
