# By submitting this assignment, I agree to the following:
# "Aggies do not lie, cheat, or steal, or tolerate those who do."
# "I have not given or received any unauthorized aid on this assignment."
#
# Name:         Sumit Nalavade
# Section:      524
# Assignment:   Lab 9.16
# Date:         31 October 2022

import math

def parta(sphereRadius, holeRadius):
    sphereVolume = (4/3) * math.pi * (sphereRadius ** 3)
    cylinderVolume = math.pi * (holeRadius ** 2) * (sphereRadius * 2)

    return sphereVolume - cylinderVolume


print(parta(1,0))