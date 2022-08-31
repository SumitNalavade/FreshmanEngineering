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

from math import pi

#Part 1
def calculateTotalDistance(interpolatedTime):
    initialTime = 10
    initialPosition = 2026

    finalTime = 55
    finalPosition = 23026

    #Calculate the position of the iss at a given time (interpolatedTime)
    interpolatedPosition = initialPosition + ((finalPosition - initialPosition)/(finalTime - initialTime) * (interpolatedTime - initialTime))

    return interpolatedPosition

#Part 2
def calculateDistanceFromHouston(testTime):
    earthRadius = 6745
    earthCircumference = 2 * pi * earthRadius

    totalDistance = calculateTotalDistance(testTime)
    distanceFromHouston = totalDistance % earthCircumference

    return distanceFromHouston

print("Part 1:")
print(f'For t = {25} minutes, the position p = {calculateTotalDistance(25)} kilometers')

print("Part 2:")
print(f'For t = {300} minutes, the position p = {calculateDistanceFromHouston(300)} kilometers')
