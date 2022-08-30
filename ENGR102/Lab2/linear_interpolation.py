# By submitting this assignment, I agree to the following:
#   "Aggies do not lie, cheat, or steal, or tolerate those who do."
#   "I have not given or received any unauthorized aid on this assignment."
#
# Names:        Sumit Nalavade
#               Srikar Velavarthipati
#               Derk Lanz
#               Andrew Stephans
# Section:      524
# Assignment:   Lab 2.8
# Date:         30 08 2022

#Part 1
initialTime = 10
initialPosition = 2026

finalTime = 55
finalPosition = 23026

#Given time ('x' value to interpolate)
testTime = 25

#Calculate the position of the iss at a given time (testTime)
testPosition = initialPosition + ((finalPosition - initialPosition)/(finalTime - initialTime) * (testTime - initialTime))

print(f'For t = {testTime} minutes, the position p = {testPosition} kilometers')

