# By submitting this assignment, I agree to the following:
# "Aggies do not lie, cheat, or steal, or tolerate those who do."
# "I have not given or received any unauthorized aid on this assignment."
#
# Name:         Sumit Nalavade
# Section:      524
# Assignment:   Lab 6.14
# Date:         2 October 2022

import math

output = []

num = int(input("Enter a positive integer: "))
initialNum = num

# Continue looping while the number reaches 1
# If the number is even, set the number to the floor of the square root of the number
# If the number is negative, set the number to be the number to the power of 3/2 
count = 0
while(num != 1):
    output.append(str(num))

    if(num % 2 == 0):
        num = math.floor(math.sqrt(num))
    else:
        num = math.floor(num ** (3/2))

    count += 1
output.append("1")


print(f"The Juggler sequence starting at {initialNum} is: ")
print(", ".join(output))
print(f"It took {count} iterations to reach 1 ")