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

def partc(char, name, company, email):
    def getLongest(char, name, company, email):
        longest = ''
        for i in [char, name, company, email]:
            if(len(i) > len(longest)):
                longest = i
        
        return longest

    card = ""

    longest = getLongest(char, name, company, email)

    card = f"""
{char+"".center(len(longest)+5,char)}
{char+name.center(len(longest)+4)+char}
{char+company.center(len(longest)+4)+char}
{char+email.center(len(longest)+4)+char}
{char+"".center(len(longest)+5,char)}""".strip()

    return card

def partd(nums):
    nums.sort()
    print(nums)

    minimum = nums[0]
    maximum = nums[len(nums) - 1]
    median = 0

    if(len(nums) % 2 != 0):
        median = nums[int(len(nums) / 2)]
        print(median)
    else:
        lower = (nums[int(len(nums) / 2)])
        upper = (nums[int((len(nums) / 2) - 1)])

        median = (lower + upper) / 2

    return (minimum, median, maximum)