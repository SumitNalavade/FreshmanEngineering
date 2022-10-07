# By submitting this assignment, I agree to the following:
# "Aggies do not lie, cheat, or steal, or tolerate those who do."
# "I have not given or received any unauthorized aid on this assignment."
#
# Name:         Sumit Nalavade
# Section:      524
# Assignment:   Lab 7.26
# Date:         6 October 2022

# Define some conversions for certain letters
conversions = {
    "a" : 4,
    "e" : 3,
    "o": 0,
    "s" : 5,
    "t" : 7
}

# Ask user for the initial text
initialSentence = input("Enter some text: ").lower()
# Create a copy of the initialSentence that we can modify
initialSentenceCopy = [word for word in initialSentence]

# Loop though the initialSentence and each time a letter is in the conversions dictionary, replace it with the appropritate conversion
for (index, letter) in enumerate(initialSentence):
    if(letter in conversions.keys()):
        initialSentenceCopy[index] = str(conversions[letter])

print(f"In leet speak, \"{initialSentence}\" is:")
print(''.join(initialSentenceCopy))