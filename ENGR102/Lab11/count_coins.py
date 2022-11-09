# By submitting this assignment, I agree to the following:
# "Aggies do not lie, cheat, or steal, or tolerate those who do."
# "I have not given or received any unauthorized aid on this assignment."
#
# Name:         Sumit Nalavade
# Section:      524
# Assignment:   Lab 11.12
# Date:         9 November 2022

gameFile = open("game.txt", "r")
# Create an array of instructions by calling the .strip() method to remove the "\n"
rawInstructionsArr = [x.strip() for x in gameFile.readlines()]
gameFile.close()

count = 0
pointer = 0

outputText = []

try:
    while True:
        instructionArr = rawInstructionsArr[pointer].split(" ")

        operation = instructionArr[0]
        sign = instructionArr[1][0]
        num = int(instructionArr[1][1:])

        if(operation == "coin"):
            if(sign == "+"):
                count += num
                outputText.append(f"{num}")
            else:
                count -= num
                outputText.append(f"{sign}{num}")
            
            pointer += 1

        elif(operation == "jump"):
            if(sign == "+"):
                pointer += num
            else:
                pointer -= num
        else:
            pointer += 1
except:
    with open("coins.txt", "w") as coinsFile:
        for output in outputText:
            coinsFile.write(output + "\n")

    print(f"Total coins collected: {count}")