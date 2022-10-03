# By submitting this assignment, I agree to the following:
# "Aggies do not lie, cheat, or steal, or tolerate those who do."
# "I have not given or received any unauthorized aid on this assignment."
#
# Name:         Sumit Nalavade
# Section:      524
# Assignment:   Lab 6.13
# Date:         2 October 2022

# Ask the user to input two integers
num1 = int(input("Enter an integer: "))
num2 = int(input("Enter another integer: "))

# While loop that run 100 iterations
count = 1
while(count <= 100):
    if(count % num1 == 0 and count % num2 == 0):
        print("Howdy Whoop")
    elif(count % num1 == 0):
        print("Howdy")
    elif(count % num2 == 0):
        print("Whoop")
    else:
        print(count)

    count += 1

