# By submitting this assignment, I agree to the following:
#   "Aggies do not lie, cheat, or steal, or tolerate those who do."
#   "I have not given or received any unauthorized aid on this assignment."
#
# Names:        Sumit Nalavade
# Section:      524
# Assignment:   Lab 4.19
# Date:         20 September 2022
#

from math import sqrt

# Function so we can return and terminate the program at specified points
def calculateRoots(a, b, c):
    if (a == 0) and (b == 0):
        print("You entered an invalid combination of coefficients!")
        return
    elif(a == 0 and b != 0):
        root = (c * -1) / b
        print(f"The root is x = {root}")
        return

    if discriminant >= 0:
        positiveRoot = (-b + sqrt(discriminant)) / (2 * a)
        negativeRoot = (-b - sqrt(discriminant)) / (2 * a)

        if discriminant == 0:
            print(f"The root is x = {positiveRoot}")
        else:
            print(f"The roots are x = {positiveRoot} and x = {negativeRoot}")
    else:
        real = -b/(2 * a)
        imaginary = sqrt(discriminant * -1)/(2 * a)

        positiveRoot = f"{real} + {imaginary}i"
        negativeRoot = f"{real} - {imaginary}i"
        print(f"The roots are x = {positiveRoot} and x = {negativeRoot}")

a = float(input("Please enter the coefficient A: "))
b = float(input("Please enter the coefficient B: "))
c = float(input("Please enter the coefficient C: "))

discriminant = (b**2) - (4 * a * c)

calculateRoots(a, b, c)