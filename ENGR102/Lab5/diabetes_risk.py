from math import e


sex = input("Enter your sex (male/female): ")
age = float(input("Enter your age: "))
bmi = float(input("Enter your BMI: "))
hypertensionMeds = input("Are you on hypertension medication? (yes/no): ")
steriods = input("Do you take steriods? (yes/no): ")
currentSmoker = input("Are you a current smoker? (yes/no): ")
previousSmoker = input("Are you a previous smoker? (yes/no): ")
parentAndSiblings = input("Do you have parents and siblings with type 2 diabetes? (yes/no): ")
parentsOrSiblings = input("Do you have parents or sibling with type 2 diabetes? (yes/no): ")
familyHistory = 0
smoker = 0

if(sex == "male"):
    sex = 0
elif(sex == "female"):
    sex = 0.879

if(bmi < 25):
    bmi = 0
elif(bmi < 27.49):
    bmi = 0.699
elif(bmi < 29.99):
    bmi = 1.97
else:
    bmi = 2.518

if(hypertensionMeds == "yes"):
    hypertensionMeds = 1.222
elif(hypertensionMeds == "no"):
    hypertensionMeds = 0

if(steriods == "yes"):
    steriods = 2.191
elif(steriods == "no"):
    steriods = 0

if(currentSmoker == "yes"):
    smoker = 0.855
elif(previousSmoker == "yes"):
    smoker = -0.128

if(parentAndSiblings == "yes"):
    familyHistory = 0.753
elif(parentsOrSiblings == "yes"):
    familyHistory = 0.728

n = 6.322 + sex - (0.063 * age) - bmi - hypertensionMeds - steriods - smoker - familyHistory

risk = 100 / (1 + (e**n))