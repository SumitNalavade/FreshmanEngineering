# By submitting this assignment, I agree to the following:
# "Aggies do not lie, cheat, or steal, or tolerate those who do."
# "I have not given or received any unauthorized aid on this assignment."
#
# Name:         Sumit Nalavade
# Section:      524
# Assignment:   Lab 1.11
# Date:         26 August 2022

import math

# Calculates the force in Newtons applied to an object with a mass of 3kg, and an acceleration of 5.5m/s^2
print("Force is", 3 * 5.5, "N")

# Calculates the wavelength of x-rays in nm, scattering from a crystal lattice with a distance between crystal layers of 0.025nm,
# scattering angle of 25 degrees, and first order of diffraction using the formula nλ = 2 * d * sin(θ)
print("Wavelength is", 2 * 0.025 * math.sin(math.radians(25)), "nm")

# Calculates how much radon-222 is left after 3 days of radioactive decay given an initial amount of 5g and a half life of 3.8 days
print("Radon-222 left is", 5 * (2 ** (-3/3.8)), "g")

# Calculates the pressure of 5 moles of ideal gas with a volume of 0.25 m^3, and a temperature of 415K
print("Pressure is", ((5 * 8.314 * 415)/0.25)/1000, "kPa")