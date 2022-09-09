# By submitting this assignment, I agree to the following:
# "Aggies do not lie, cheat, or steal, or tolerate those who do."
# "I have not given or received any unauthorized aid on this assignment."
#
# Name:         Sumit Nalavade
# Section:      524
# Assignment:   Lab 3.18
# Date:         9 September 2022


from math import *

#Takes in the name of a shape(string), the sidelength and area of a shape(float) and prints out a message
def printresult(shape, side, area):
    print(f'A {shape} with side {side:.2f} has area {area:.3f}')

side_length = float(input("Please enter the side length: "))

triangle_area = (sqrt(3)/4) * side_length**2
square_area = side_length ** 2
pentagon_area = (0.25) * sqrt(5 * (5 + (2 * sqrt(5)))) * side_length**2
dodecagon_area = 3 * (2 + sqrt(3)) * side_length**2

printresult("triangle", side_length, triangle_area)
printresult("square", side_length, square_area)
printresult("pentagon", side_length, pentagon_area)
printresult("dodecagon", side_length, dodecagon_area)