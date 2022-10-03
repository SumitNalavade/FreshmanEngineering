# By submitting this assignment, I agree to the following:
# "Aggies do not lie, cheat, or steal, or tolerate those who do."
# "I have not given or received any unauthorized aid on this assignment."
#
# Name:         Sumit Nalavade
# Section:      524
# Assignment:   Lab 6.15
# Date:         2 October 2022

# Get the sum of numbers from 1 to (n - 1)
def getInitialSumOfNumbers(num):
    count = 0
    for i in range(1, num):
        count += i
    
    return count

# Get the sum of numbers (n + 1) to (n + r)
def calcSum(num, iterator):
    sum = 0
    for i in range(num + 1, num + iterator + 1):
        sum += i
    return sum

num = int(input("Enter a value for n: "))

initialSumOfNumbers = getInitialSumOfNumbers(num)

count = 0
isEven = False
while(isEven == False):
    count += 1
    if(initialSumOfNumbers == calcSum(num, count)):
        isEven = True
        print(f"{num} is a balancing number with r={count}")
    elif(initialSumOfNumbers < calcSum(num , count)):
        print(f"{num} is not a balancing number")
        break