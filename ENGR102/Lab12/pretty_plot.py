# By submitting this assignment, I agree to the following:
# "Aggies do not lie, cheat, or steal, or tolerate those who do."
# "I have not given or received any unauthorized aid on this assignment."
#
# Name:         Sumit Nalavade
# Section:      524
# Assignment:   Lab 12.16
# Date:         15 November 2022

import numpy as np
import matplotlib.pyplot as plt

# Normal python lists to hold the x and y
xVals = []
yVals = []

P = np.array([0, 1])
M = np.matrix('1.01 0.09; -0.09 1.01')

for i in range(201):
    P = P * M

    xVals.append(P.item(0))
    yVals.append(P.item(1))

plt.plot(xVals, yVals)

plt.title("Pretty Spiral Graph")
plt.xlabel("X Coordinates")
plt.ylabel("Y Coordinates")

plt.show()