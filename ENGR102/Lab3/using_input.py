# By submitting this assignment, I agree to the following:
# "Aggies do not lie, cheat, or steal, or tolerate those who do."
# "I have not given or received any unauthorized aid on this assignment."
#
# Name:         Sumit Nalavade
# Section:      524
# Assignment:   Lab 3.17
# Date:         9 September 2022

import math

#Each block states what the calculation is and the inputs
print("This program calculates the applied force given mass and acceleration")
mass = float(input("Please enter the mass (kg): "))
acceleration = float(input("Please enter the acceleration (m/s^2): "))
force = mass * acceleration
print(f"Force is {force:.1f} N")

print("This program calculates the wavelength given distance and angle")
crystalLayerDistance = float(input("Please enter the distance (nm): "))
scatteringAngleDegrees = float(input("Please enter the angle (degrees): "))
scatteringAngleRadians = math.radians(scatteringAngleDegrees)
wavelength = 2 * crystalLayerDistance * math.sin(scatteringAngleRadians)
print(f"Wavelength is {wavelength:.4f} nm")

print("This program calculates how much Radon-222 is left given time and initial amount")
daysPassed = float(input("Please enter the time (days): "))
initialAmount = float(input("Please enter the initial amount (g): "))
halfLifeDays = 3.8
amountLeft = initialAmount * (2 ** ((-daysPassed)/halfLifeDays))
print(f"Radon-222 left is {amountLeft:.2f} g")
    
print("This program calculates the pressure given moles, volume, and temperature")
moles = float(input("Please enter the number of moles: "))
volume = float(input("Please enter the volume (m^3): "))
kelvinTemp = float(input("Please enter the temperature (K): "))
gasConstant = 8.314
pressure = ((moles * gasConstant * kelvinTemp)/volume)/1000
print(f"Pressure is {pressure:.0f} kPa")
