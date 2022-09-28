# By submitting this assignment, I agree to the following:
#   "Aggies do not lie, cheat, or steal, or tolerate those who do."
#   "I have not given or received any unauthorized aid on this assignment."
#
# Names:        Sumit Nalavade
#               Surya Jasper
#               Srikar Velavarthipati
# Section:      524
# Assignment:   Lab 5.3
# Date:         26 September 2022

from math import e

# Initialize numerical values for each factor that we'll use in calculation
sexValue = 0
bmiValue = 0
hypertensionMedicationValue = 0
steroidsValue = 0
smokerValue = 0
familyHistoryValue = 0
isParentAndSibling = "f"
isFormerSmoker = "f"

# Ask user a series of questions
# Make sure to cast the value of each variable to lowercase if the type is string
sex = input("Enter your sex (M/F): ").lower()
age = int(input("Enter your age (years): "))
bmi = float(input("Enter your BMI: "))
isHypertension = input("Are you on medication for hypertension (Y/N)? ").lower()
isSteroids = input("Are you on steroids (Y/N)? ").lower()
isCurrentSmoker = input("Do you smoke cigarettes (Y/N)? ").lower()
if(isCurrentSmoker == "n"):
    isFormerSmoker = input("Did you used to smoke (Y/N)? ").lower()
isFamilyHistory = input("Do you have a family history of diabetes (Y/N)? ").lower()
if(isFamilyHistory == "y"):
    isParentAndSibling = input("Both parent and sibling (Y/N)? ").lower()

# Evaluate the answers the user inputted and assign numberical scores for each
# Initial score of each is 0
if(sex == "f"):
    sexValue = 0.879

if(25 <= bmi < 27.49):
    bmiValue = 0.699
elif(27.5 <= bmi <= 29.99):
    bmiValue = 1.97
elif(bmi >= 30):
    bmiValue = 2.518

if(isHypertension == "y"):
    hypertensionMedicationValue = 1.222

if(isSteroids == "y"):
    steroidsValue = 2.191

# Ask the user if they're a current smoker and if yes, set the value to 0.855, but if they put no, ask them if they used to smoke and if yes, set the value to -0.218
if(isCurrentSmoker == "y"):
    smokerValue = 0.855
else:
    if(isFormerSmoker == "y"):
        smokerValue = -0.218

# Ask the user if they have a history of type-2 diabetes in their family. If yes, ask if they've had a parent and sibling. If yes, set the value to 0.753, if no, set the value to 0.728
# If the use answers no to the first question, the value will already be set to 0
if(isFamilyHistory == "y"):
    if(isParentAndSibling == "y"):
        familyHistoryValue = 0.753
    else:
        familyHistoryValue = 0.728

# Calculate the overall risk of type-2 diabetes for a person given their answers to the questions
n = 6.322 + sexValue - (0.063 * age) - bmiValue - hypertensionMedicationValue - steroidsValue - smokerValue - familyHistoryValue
risk = 100 / (1 + (e ** n))

# Print a message to the user with their risk for developing type-2 diabetes
print(f"Your risk of developing type-2 diabetes is {risk:.1f}%")
