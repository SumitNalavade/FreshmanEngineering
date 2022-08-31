# By submitting this assignment, I agree to the following:
# "Aggies do not lie, cheat, or steal, or tolerate those who do."
# "I have not given or received any unauthorized aid on this assignment."
#
# Name:         Sumit Nalavade
# Section:      524
# Assignment:   Lab 2.10
# Date:         31 August 2022

#Calculate an (x,y,z) coordinate given at time=12, position=(8,6,7) and at time=85, position=(-5, 30, 9)
def calcPosition(interpolatedTime):
    initialTime = 12
    finalTime = 85

    initialX = 8
    initialY = 6
    initialZ = 7

    finalX = -5
    finalY = 30
    finalZ = 9

    interpolatedX = initialX + ((finalX - initialX)/(finalTime - initialTime) * (interpolatedTime - initialTime))
    interpolatedY = initialY + ((finalY - initialY)/(finalTime - initialTime) * (interpolatedTime - initialTime))
    interpolatedZ = initialZ + ((finalZ - initialZ)/(finalTime - initialTime) * (interpolatedTime - initialTime))

    return (interpolatedX, interpolatedY, interpolatedZ)

x1, y1, z1 = calcPosition(30)
print("At time 30.0 seconds:")
print(f"x1 = {x1} m")
print(f"y1 = {y1} m")
print(f"z1 = {z1} m")
print("-----------------------")

x2, y2, z2 = calcPosition(37.5)
print("At time 37.5 seconds:")
print(f"x2 = {x2} m")
print(f"y2 = {y2} m")
print(f"z2 = {z2} m")
print("-----------------------")

x3, y3, z3 = calcPosition(45)
print("At time 45.0 seconds:")
print(f"x3 = {x3} m")
print(f"y3 = {y3} m")
print(f"z3 = {z3} m")
print("-----------------------")

x4, y4, z4 = calcPosition(52.5)
print("At time 52.5 seconds:")
print(f"x4 = {x4} m")
print(f"y4 = {y4} m")
print(f"z4 = {z4} m")
print("-----------------------")

x5, y5, z5 = calcPosition(60)
print("At time 60.0 seconds:")
print(f"x5 = {x5} m")
print(f"y5 = {y5} m")
print(f"z5 = {z5} m")