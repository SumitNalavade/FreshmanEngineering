# By submitting this assignment, I agree to the following:
# "Aggies do not lie, cheat, or steal, or tolerate those who do."
# "I have not given or received any unauthorized aid on this assignment."
#
# Name:         Sumit Nalavade
# Section:      524
# Assignment:   Lab 7.27
# Date:         6 October 2022

import math

# take in a vector, return the square root of each value squared and added together
def getMagnitude(vector):
    addedTotal = 0
    for num in vector:
        addedTotal += num ** 2

    return math.sqrt(addedTotal)

# add each value of a vector with the correspoding one in the other vector
def addVectors(vector1, vector2):
    total = []

    for (index,num) in enumerate(vector1):
        total.append(num + vector2[index])

    return total


# subtract each value of a vector with the correspoding one in the other vector
def subtractVectors(vector1, vector2):
    total = []

    for (index,num) in enumerate(vector1):
        total.append(num - vector2[index])

    return total

# Calculate the dot product by adding together the the mutiplied version of each element in a vector by the corresponding one in the other vector
def getDotProduct(vector1, vector2):
    total = 0

    for (index, num) in enumerate(vector1):
        total += num * vector2[index]

    return total

vector1 = [float(x) for x in input("Enter the elements for vector A: ").split(" ")]
vector2 = [float(x) for x in input("Enter the elements for vector B: ").split(" ")]

print(f"The magnitude of vector A is {getMagnitude(vector1):.5f}")
print(f"The magnitude of vector B is {getMagnitude(vector2):.5f}")
print(f"A + B is {addVectors(vector1, vector2)}")
print(f"A - B is {subtractVectors(vector1, vector2)}")
print(f"The dot product is {getDotProduct(vector1, vector2):.2f}")