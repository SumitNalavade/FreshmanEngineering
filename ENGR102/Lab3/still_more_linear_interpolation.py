# By submitting this assignment, I agree to the following:
#   "Aggies do not lie, cheat, or steal, or tolerate those who do."
#   "I have not given or received any unauthorized aid on this assignment."
#
# Names:        Sumit Nalavade
# Section:      524
# Assignment:   Lab 3.16
# Date:         9 September 2022
#
#

#Takes in a time between time1 & time2 to interpolated on. Prints a string with a position given a time
def calculatePosition(interpolatedTime):
    interpolatedX = x1 + ((x2 - x1)/(time2 - time1) * (interpolatedTime - time1))
    interpolatedY = y1 + ((y2 - y1)/(time2 - time1) * (interpolatedTime - time1))
    interpolatedZ = z1 + ((z2 - z1)/(time2 - time1) * (interpolatedTime - time1))

    print(f"At time {interpolatedTime:.2f} seconds the object is at ({interpolatedX:.3f}, {interpolatedY:.3f}, {interpolatedZ:.3f})")

time1 = float(input("Enter time 1: "))
x1 = float(input("Enter the x position of the object at time 1: "))
y1 = float(input("Enter the y position of the object at time 1: "))
z1 = float(input("Enter the z position of the object at time 1: "))

time2 = float(input("Enter time 2: "))
x2 = float(input("Enter the x position of the object at time 2: "))
y2 = float(input("Enter the y position of the object at time 2: "))
z2 = float(input("Enter the z position of the object at time 2: "))

intervalLength = (time2 - time1) / 4

interpolatedTime = time1
for _ in range(5):
    calculatePosition(interpolatedTime)
    interpolatedTime += intervalLength