# By submitting this assignment, I agree to the following:
# "Aggies do not lie, cheat, or steal, or tolerate those who do."
# "I have not given or received any unauthorized aid on this assignment."
#
# Name:         Sumit Nalavade
# Section:      524
# Assignment:   Lab 4.19
# Date:         19 September 2022

from cmath import sqrt

a = int(input("Please enter the coefficient A: "))
b = int(input("Please enter the coefficient B: "))
c = int(input("Please enter the coefficient c: "))

if(a == 0 and b == 0):
    print("You entered an invalid combination of coefficients!")

discriminant = (b**2) - (4*a*c)

sol1 = (-b-sqrt(discriminant))/(2*a)
sol2 = (-b+sqrt(discriminant))/(2*a)

print(sol1, sol2)
