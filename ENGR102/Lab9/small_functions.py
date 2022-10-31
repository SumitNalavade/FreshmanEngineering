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
    return ((4 * math.pi)/3) * ((sphereRadius**2) - (holeRadius**2)) ** (3/2)
    
def partb(n):
    oddNums = [i for i in range(n) if i % 2 != 0]
    start  = 0
    while(True):
        total = 0
        numsArr = []
        if(start >= n):
            return False
        for i in (range(start, len(oddNums))):
            numsArr.append(oddNums[i])
            total += oddNums[i]
            if(total == n):
                return numsArr
        start += 1
