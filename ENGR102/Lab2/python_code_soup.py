# By submitting this assignment, I agree to the following:
# "Aggies do not lie, cheat, or steal, or tolerate those who do."
# "I have not given or received any unauthorized aid on this assignment."
#
# Name:         Sumit Nalavade
# Section:      524
# Assignment:   Lab 2.10
# Date:         31 August 2022

#Outputs 1
x = 1
z = 0
z += x
print(z)

#Outputs 26
y = 10
z += y
z += y
z += x
z += x
z += x
z += x
z += x
print(z)

#Outputs 102
y = 10
x = y
z = 0
y *= x
z += y
x = 1
z += x
z += x
print(z)

#Outputs 1000000000
z = 0
y = 10
x = y
y *= x
y *= x
y *= x
y *= x
y *= x
y *= x
y *= x
y *= x
z += y
print(z)

#Outputs 8675
y = 10
x = y
y *= x
y *= x
x = 1
x += 1
x += 1
x += 1
x += 1
x += 1
x += 1
x += 1
y *= x
z = 0
z += y
y = 10
x = y
y = 10
y *= x
x = 1
x += 1
x += 1
x += 1
x += 1
x += 1
y *= x
z += y
y = 10
x = 1
x += 1
x += 1
x += 1
x += 1
x += 1
x += 1
y *= x
z += y
x = 1
x += 1
x += 1
x += 1
x += 1
z += x
print(z)