# By submitting this assignment, I agree to the following:
#   "Aggies do not lie, cheat, or steal, or tolerate those who do."
#   "I have not given or received any unauthorized aid on this assignment."
#
# Name:         Sumit Nalavade, Surya Jasper, Ronit Dhawan, Srikar Velavarthipati
# Section:      524
# Assignment:   Lab 11.10
# Date:         17 November 2022

# As a team, we have gone through all required sections of the  
# tutorial, and each team member understands the material

import numpy as np

A = np.array([[ 0, 1, 2, 3],
    [ 4, 5, 6, 7],
    [ 8, 9, 10, 11 ]])

B = np.array([[ 0, 1 ],
    [ 2, 3 ],
    [ 4, 5 ],
    [ 6, 7 ]])

C = np.array([[ 0, 1, 2 ],
    [ 3, 4, 5 ]])

D = A @ B @ C

print(f"A = {A} \n")
print(f"B = {B} \n")
print(f"C = {C} \n")

print(f"D = {D} \n")

print(f"D^T = {np.transpose(D)} \n")

print(f"E = {(D ** (1/2)) / 2}")