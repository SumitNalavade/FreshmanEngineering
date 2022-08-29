# By submitting this assignment, I agree to the following:
# "Aggies do not lie, cheat, or steal, or tolerate those who do."
# "I have not given or received any unauthorized aid on this assignment."
#
# Name:         Sumit Nalavade
# Section:      524
# Assignment:   Lab 1.12
# Date:         26 August 2022

# Evaluate a limit by checking several numbers that approach 1 for the function f(x) = (x^2 - 1)/(x - 1)
print("This shows the evaluation of (x^2-1)/(x-1) evaluated close to x=1")

print("My guess is 2")

# Use the values of 8 numbers starting at 1.1 and subsequently adding an extra 0 after the decimal. Ex: 1.1, 1.01, 1.001
print(((1.1 ** 2) - 1)/(1.1-1))
print(((1.01 ** 2) - 1)/(1.01-1))
print(((1.001 ** 2) - 1)/(1.001-1))
print(((1.0001 ** 2) - 1)/(1.0001-1))
print(((1.00001 ** 2) - 1)/(1.00001-1))
print(((1.000001 ** 2) - 1)/(1.000001-1))
print(((1.0000001 ** 2) - 1)/(1.0000001-1))
print(((1.00000001 ** 2) - 1)/(1.00000001-1))
print("")

print("I think my guess was accurate")


