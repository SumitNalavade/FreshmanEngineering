# By submitting this assignment, I agree to the following:
# "Aggies do not lie, cheat, or steal, or tolerate those who do."
# "I have not given or received any unauthorized aid on this assignment."
#
# Name:         Sumit Nalavade
# Section:      524
# Assignment:   Lab 3.19
# Date:         9 September 2022

from math import *

precision_value = int(input("Please enter the number of digits of precision for e: "))

print(f'The value of e to {precision_value} digits is: {e:.{precision_value}f}')