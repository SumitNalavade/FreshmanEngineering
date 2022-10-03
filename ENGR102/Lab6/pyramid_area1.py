# By submitting this assignment, I agree to the following:
#   "Aggies do not lie, cheat, or steal, or tolerate those who do."
#   "I have not given or received any unauthorized aid on this assignment."
#
# Names:        Sumit Nalavade
#               Srikar Velavarthipati
# Section:      524
# Assignment:   Lab 6.11
# Date:         3 October 2022

from math import sqrt

def getSurfaceArea(sideLength, numLayers):
    surfaceArea = 0
    for i in range(1, numLayers + 1):
        surfaceArea += i * 3 * (sideLength ** 2)

    return surfaceArea

# Ask the user to input the side length of each triangle as well as the number of layers of the geometry temple
sideLength = float(input("Enter the side length in meters: "))
numLayers = int(input("Enter the number of layers: "))

# Get the total surface area of the geometry temple by adding together the surface areas of the the top with the rest
totalArea = getSurfaceArea(sideLength, numLayers) + (sqrt(3) / 4) * (numLayers * sideLength) ** 2

print(f'You need {totalArea:.2f}m^2 of gold foil to cover the pyramid')