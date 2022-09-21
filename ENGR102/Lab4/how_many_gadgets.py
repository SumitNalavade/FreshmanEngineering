# By submitting this assignment, I agree to the following:
#   "Aggies do not lie, cheat, or steal, or tolerate those who do."
#   "I have not given or received any unauthorized aid on this assignment."
#
# Names:        Sumit Nalavade
# Section:      524
# Assignment:   Lab 4.18
# Date:         20 September 2022
#

def calculateGadgets(days):
    # Evaluate various conditions
    if(days <= 0):
        print("You entered an invalid number!")
        return
    
    if(days < 11):
        totalGadgets = days * 5
    elif(days <= 60):
        totalGadgets = (10 * 5) + (days - 10) * 50
    elif(days <= 101):
        totalGadgets = int((10 * 5) + ((60 - 10) * 50) + ((49+(110-days))/2)*(days-60))
    else:
        totalGadgets = 3730
    
    print(f"The total number of gadgets produced on day {days} is {totalGadgets}")

totalGadgets = 0

days = int(input("Please enter a positive value for day: "))

calculateGadgets(days)

