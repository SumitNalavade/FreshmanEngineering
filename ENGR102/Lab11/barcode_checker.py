# By submitting this assignment, I agree to the following:
# "Aggies do not lie, cheat, or steal, or tolerate those who do."
# "I have not given or received any unauthorized aid on this assignment."
#
# Name:         Sumit Nalavade
# Section:      524
# Assignment:   Lab 11.11
# Date:         9 November 2022

fileName = input("Enter the name of the file: ")

barcodesFile = open(fileName, "r")
# Make an array of barcodes as strings with the '\n' removed
barcodesArr = [x.strip() for x in barcodesFile.readlines()]
barcodesFile.close()

validBarcodes = []

for barcode in barcodesArr:
    barcodeGroupA = []
    barcodeGroupB = []

    for index in range(0, 12):
        if(index % 2 == 0):
            barcodeGroupA.append(int(barcode[index]))
        else:
            barcodeGroupB.append(int(barcode[index]))

    sumDigits = (sum(barcodeGroupB) * 3) +sum(barcodeGroupA)

    evalDigit = 10 - (sumDigits % 10)

    if(evalDigit == int(barcode) % 10):
        validBarcodes.append(barcode)

with open("valid_barcodes.txt", "w") as validBarcodesFile:
    for barcode in validBarcodes:
        validBarcodesFile.write(barcode + "\n")

print(f"There are {len(validBarcodes)} valid barcodes")