# By submitting this assignment, I agree to the following:
# "Aggies do not lie, cheat, or steal, or tolerate those who do."
# "I have not given or received any unauthorized aid on this assignment."
#
# Name:         Sumit Nalavade
# Section:      524
# Assignment:   Lab 5.4
# Date:         28 September 2022

from math import log10

# Get the initial excess temperature from the user
temp = float(input("Enter the excess temperature: "))

# Evaluate which range the excess temperate falls in
# Initialze the initial and final x,y variables to interpolate on
if(1.3 <= temp < 5):
    xInitial = 1.3
    xFinal = 5
    yInitial = 1000
    yFinal = 7000
elif(5 <= temp < 30):
    xInitial = 5
    xFinal = 30
    yInitial = 7000
    yFinal = 1.5 * 10**6
elif(30 <= temp < 120):
    xInitial = 30
    xFinal = 120
    yInitial = 1.5 * 10**6
    yFinal = 2.5 * 10**4
elif(120 <= temp <= 1200):
    xInitial = 120
    xFinal = 1200
    yInitial = 2.5 * 10**4
    yFinal = 1.5 * 10**6
else:
    # If the excess temperature is either less than 1.3 or greater than 1200, print a message to the user and terminate the program
    print("Surface heat flux is not available")
    exit(0)

# Calculate the slope
slope = log10(yFinal/yInitial) / log10(xFinal/xInitial)
# Plug the slope into the equation to calculate the surface heat flux
surfaceHeatFlux = yInitial * ((temp / xInitial)**slope)

# Print out the surface heat flux to the user
print(f"The surface heat flux is approximately {round(surfaceHeatFlux)} W/m^2")