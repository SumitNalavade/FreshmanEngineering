# By submitting this assignment, I agree to the following:
# "Aggies do not lie, cheat, or steal, or tolerate those who do."
# "I have not given or received any unauthorized aid on this assignment."
#
# Name:         Sumit Nalavade
# Section:      524
# Assignment:   Lab 4.15
# Date:         19 September 2022

############ Part A ############
a = input("Enter True or False for a: ")
b = input("Enter True or False for b: ")
c = input("Enter True or False for c: ")

if(a == "True" or a == "T" or a == "t"):
    a = True
else:
    a = False

if(b == "True" or b == "T" or b == "t"):
    b = True
else:
    b = False

if(c == "True" or c == "T" or c == "t"):
    c = True
else:
    c = False

############ Part B ############
print(f"a and b and c: {a and b and c}")
print(f"a or b or c: {a or b or c}")

############ Part C ############
print(f"XOR: {(a and not b) or (not a and b)}")
print(f"Odd number: {(a and b and c) or (a and not(b) and not(c)) or (not(a) and b and not(c)) or (not(a) and not(b) and c)}")