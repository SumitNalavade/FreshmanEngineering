# By submitting this assignment, I agree to the following:
#   "Aggies do not lie, cheat, or steal, or tolerate those who do."
#   "I have not given or received any unauthorized aid on this assignment."
#
# Name:         Sumit Nalavade, Surya Jasper, Ronit Dhawan, Srikar Velavarthipati
# Section:      524
# Assignment:   Lab 11.9
# Date:         13 November 2022

# Class to hold the fields and to deterimine if it's valid
# Helps organize some of the data a little bit better
class Passport():
    fieldsArr = []
    originalText = ""

    def __init__(self, fieldsArr) -> None:
        self.fieldsArr = fieldsArr

    def isValid(self):
        if(len(self.fieldsArr) < 8):
            for field in self.fieldsArr:
                if("hcl" in field):
                    return False

        return True
                    
validPassports = []

filename = input("Enter the name of the file: ")

scannedPassportsFile = open(filename, "r")
scannedPassportsList = scannedPassportsFile.read().split("\n\n")
scannedPassportsFile.close()

validPassportsCount = 0
for i in scannedPassportsList:
    passport = Passport(i.replace("\n", " ").split(" "))

    if(passport.isValid() == True):
        validPassportsCount += 1
        validPassports.append(i)
        
with open("valid_passports.txt", "w") as validPassportsFile:
    for validPassport in validPassports:
        validPassportsFile.write(validPassport + "\n\n")

print(f"There are {validPassportsCount} valid passports")