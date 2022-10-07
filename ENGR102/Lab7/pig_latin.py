# By submitting this assignment, I agree to the following:
# "Aggies do not lie, cheat, or steal, or tolerate those who do."
# "I have not given or received any unauthorized aid on this assignment."
#
# Name:         Sumit Nalavade
# Section:      524
# Assignment:   Lab 7.25
# Date:         6 October 2022

# Create a list of all vowels
vowels = ["a", "e", "i", "o", "u", "y"]

# "treat" a consonant by starting at the beginning of the word and moving all letters which are consonants to the end and adding "ay"
def treatConsonants(word):
    consonants = []

    for letter in word:
        if(letter not in vowels):
            consonants.append(letter)
        else:
            break

    combinedConsonants = "".join(consonants)

    return f"{str(word).replace(combinedConsonants, '', 1)}{combinedConsonants}ay"

# "treat" a vowel by adding "yay" to the end
def treatVowels(word):
    return f"{word}yay"

# initialize and array to hold the "treated" words
finalWords = []
initialSentence = input("Enter word(s) to convert to Pig Latin: ")

# loop over all the words in the sentence and call either the "treatConsonants" or "treatVowels" function depending on what the first letter of the word is
for word in initialSentence.lower().split(" "):
    firstLetter = word[0]

    if(firstLetter not in vowels):
        # Add the "treated" word to the finalWords array
        finalWords.append(treatConsonants(word))
    else:
        finalWords.append(treatVowels(word))
        
print(f"In Pig Latin, \"{initialSentence}\" is: {' '.join(finalWords)}")