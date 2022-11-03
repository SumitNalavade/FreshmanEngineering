# By submitting this assignment, I agree to the following:
# "Aggies do not lie, cheat, or steal, or tolerate those who do."
# "I have not given or received any unauthorized aid on this assignment."
#
# Name:         Sumit Nalavade
# Section:      524
# Assignment:   Lab 10.14
# Date:         2 November 2022

# Evaluates if a number is greater or less than the secret number
def evaluateNumber(secretNumber, guessNumber):
    if(guessNumber < secretNumber):
        print("Too low!")
    elif(guessNumber > secretNumber):
        print("Too high!")
        
def getGuess():
    guessNumber = 0

    try:
        guessNumber = int(input("What is your guess? "))
    except:
        try:
            guessNumber = int(input("Bad input! Try again: "))
        except:
            try:
                guessNumber = int(input("Bad input! Try again: "))
            except:
                guessNumber = int(input("Bad input! Try again: "))

    return guessNumber

secretNumber = 26
guessNumber = 0
count = 0

print("Guess the secret number! Hint: it's an integer between 1 and 100...")

while(guessNumber != secretNumber):    
    count += 1   
    
    guessNumber = getGuess()
    
    evaluateNumber(secretNumber, guessNumber)

print(f"You guessed it! It took you {count} guesses.")