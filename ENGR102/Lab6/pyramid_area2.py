# By submitting this assignment, I agree to the following:
#   "Aggies do not lie, cheat, or steal, or tolerate those who do."
#   "I have not given or received any unauthorized aid on this assignment."
#
# Names:        Sumit Nalavade
#               Srikar Velavarthipati
#               Surya Jasper
# Section:      524
# Assignment:   Lab 6.12
# Date:         3 October 2022


from math import sqrt

# first, we need to prompt the user for our side length and the number of layers in the pyramid
sideLength = float(input('Enter the side length in meters: '))
numLayers = int(input('Enter the number of layers: '))

# calculate the area of each square and triangle using the side length and the respective area formulas
squareArea = sideLength**2
triangleArea = sqrt(3)/4 * sideLength**2

# arithmetic sequence
n_sq = 3 * numLayers*(numLayers+1)/2

n_tri = numLayers**2

ans = n_sq * squareArea + n_tri * triangleArea

print(f'You need {ans:.2f} m^2 of gold foil to cover the pyramid')