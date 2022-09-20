# By submitting this assignment, I agree to the following:
#   "Aggies do not lie, cheat, or steal, or tolerate those who do."
#   "I have not given or received any unauthorized aid on this assignment."
#
# Names:        Sumit Nalavade
# Section:      524
# Assignment:   Lab 4.13
# Date:         19 September 2022
#


paid = float(input("How much did you pay? "))
cost = float(input("How much did it cost? "))
totalChange = (round(paid - cost, 3)) * 100

# Evaluate the number of each coin
quarters = totalChange // 25
dimes = (totalChange - (quarters * 25)) // 10
nickels = (totalChange - (dimes * 10) - (quarters * 25)) // 5
pennies = (totalChange - (dimes * 10) - (quarters * 25)  - (nickels * 5))

change = '{:.2f}'.format(totalChange / 100)
print(f"You received ${change} in change. That is...")

personalChange = { "quarter": quarters, "dime": dimes, "nickel": nickels, "penny": pennies }

# print out the results
for coin in personalChange:
    if(personalChange[coin] <= 0):
        continue
    elif(personalChange[coin] == 1):
        print(f"{int(personalChange[coin])} {coin}")
    elif(personalChange[coin] > 1 and coin == "penny"):
        print(f"{int(personalChange[coin])} pennies")
    else:
        print(f"{int(personalChange[coin])} {coin}s")