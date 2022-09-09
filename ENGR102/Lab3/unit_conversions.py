# By submitting this assignment, I agree to the following:
#   "Aggies do not lie, cheat, or steal, or tolerate those who do."
#   "I have not given or received any unauthorized aid on this assignment."
#
# Names:        Sumit Nalavade
# Section:      524
# Assignment:   Lab 3.15
# Date:         9 September 2022
#
#

#Input for the user
quantity = float(input("Please enter the quantity to be converted: "))

#Define a scaling factor for each conversion
POUNDS_TO_NEWTONS_SCALING_FACTOR = 4.4482216153
newtons = quantity * POUNDS_TO_NEWTONS_SCALING_FACTOR

METERS_TO_FEET_SCALING_FACTOR = 3.28084
feet = quantity * METERS_TO_FEET_SCALING_FACTOR

ATMOSPHERES_TO_KILOPASCALS_SCALING_FACTOR = 101.325
kilopascals = quantity * ATMOSPHERES_TO_KILOPASCALS_SCALING_FACTOR

WATTS_TO_BTU_SCALING_FACTOR = 3.412142
Btu = quantity * WATTS_TO_BTU_SCALING_FACTOR

LITERS_PER_SECOND_TO_GALLONS_PER_MINUTE_SCALING_FACTOR = 15.850323141489
gallons_per_minute = quantity * LITERS_PER_SECOND_TO_GALLONS_PER_MINUTE_SCALING_FACTOR

degrees_farenheit = (quantity * 1.8) + 32

print(f"{quantity:.2f} pounds force is equivalent to {newtons:.2f} Newtons")
print(f"{quantity:.2f} meters is equivalent to {feet:.2f} feet")
print(f"{quantity:.2f} atmospheres is equivalent to {kilopascals:.2f} kilopascals")
print(f"{quantity:.2f} watts is equivalent to {Btu:.2f} BTU per hour")
print(f"{quantity:.2f} liters per second is equivalent to {gallons_per_minute:.2f} US gallons per minute")
print(f"{quantity:.2f} degrees Celsius is equivalent to {degrees_farenheit:.2f} degrees Fahrenheit")