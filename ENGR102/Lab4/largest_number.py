# By submitting this assignment, I agree to the following:
# "Aggies do not lie, cheat, or steal, or tolerate those who do."
# "I have not given or received any unauthorized aid on this assignment."
#
# Name:         Sumit Nalavade
# Section:      524
# Assignment:   Lab 4.16
# Date:         19 September 2022

#Take in 3 numbers as flaots
num1 = float(input("Enter number 1: "))
num2 = float(input("Enter number 2: "))
num3 = float(input("Enter number 3: "))

#Evalue the largest of the 3 numbers
if(num1 > num2):
    print(f"The largest number is {num1}")
elif(num2 > num3):
    print(f"The largest number is {num2}")
else:
    print(f"The largest number is {num3}")