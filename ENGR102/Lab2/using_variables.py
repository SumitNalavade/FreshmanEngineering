# By submitting this assignment, I agree to the following:
# "Aggies do not lie, cheat, or steal, or tolerate those who do."
# "I have not given or received any unauthorized aid on this assignment."
#
# Name:         Sumit Nalavade
# Section:      524
# Assignment:   Lab 2.9
# Date:         31 August 2022

import math

# Calculates the force in Newtons applied to an object with a mass of 3kg, and an acceleration of 5.5m/s^2
mass = 3
acceleration = 5.5

force = mass * acceleration
print(f"Force is {force} N")

# Calculates the wavelength of x-rays in nm, scattering from a crystal lattice with a distance between crystal layers of 0.025nm,
# scattering angle of 25 degrees, and first order of diffraction using the formula nλ = 2 * d * sin(θ)
crystalLayerDistance = 0.025
scatteringAngleDegrees = 25
scatteringAngleRadians = math.radians(scatteringAngleDegrees)

wavelength = 2 * crystalLayerDistance * math.sin(scatteringAngleRadians)
print(f"Wavelength is {wavelength} nm")

# Calculates how much radon-222 is left after 3 days of radioactive decay given an initial amount of 5g and a half life of 3.8 days
daysPassed = 3
initialAmount = 5
halfLifeDays = 3.8

amountLeft = initialAmount * (2 ** ((-daysPassed)/halfLifeDays))
print(f"Radon-222 left is {amountLeft} g")

# Calculates the pressure of 5 moles of ideal gas with a volume of 0.25 m^3, and a temperature of 415K
moles = 5
volume = 0.25
kelvinTemp = 415
gasConstant = 8.314

pressure = ((moles * gasConstant * kelvinTemp)/volume)/1000
print(f"Pressure is {pressure} kPa")