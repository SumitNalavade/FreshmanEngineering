# By submitting this assignment, I agree to the following:
#   "Aggies do not lie, cheat, or steal, or tolerate those who do."
#   "I have not given or received any unauthorized aid on this assignment."
#
# Name:         Sumit Nalavade, Surya Jasper, Ronit Dhawan, Srikar Velavarthipati
# Section:      524
# Assignment:   Lab 11.10
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

        for fields in self.fieldsArr:
            splitFields = fields.split(":")
            key = splitFields[0]
            value = splitFields[1]

            if(key == "byr"):
                if(int(value) < 1920 or int(value) > 2005):
                    return False

            if(key == "iyr"):
                if(int(value) < 2012 or int(value) > 2022):
                    return False

            if(key == "eyr"):
                if(int(value) < 2022 or int(value) > 2032):
                    return False

            if(key == "hgt"):
                if(value[-2:] not in ["cm", "in"]):
                    return False

                if(value[-2:] == "cm"):
                    if(float(value.replace("cm", "")) < 150 or float(value.replace("cm", "")) > 193):
                        return False
                elif(value[-2:] == "in"):
                    if(float(value.replace("in", "")) < 59 or float(value.replace("in", "")) > 76):
                        return False
            
            if(key == "ecl"):
                if(value not in ["amb", "blu", "brn", "gry", "grn", "hzl", "oth"]):
                    return False

            if(key == "pid"):
                if(len(value) != 9):
                    return False

            if(key == "cid"):
                if(len(str(int(value))) != 3):
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
        
with open("valid_passports2.txt", "w") as validPassportsFile:
    for validPassport in validPassports:
        validPassportsFile.write(validPassport + "\n\n")

print(f"There are {validPassportsCount} valid passports")