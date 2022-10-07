# By submitting this assignment, I agree to the following:
# "Aggies do not lie, cheat, or steal, or tolerate those who do."
# "I have not given or received any unauthorized aid on this assignment."
#
# Name:         Sumit Nalavade
# Section:      524
# Assignment:   Lab 7.28
# Date:         7 October 2022

# take in a number and pad it with 0's until it's length is 4
def createFourDigitNumber(num):
    newNum = str(num)

    while(len(newNum) < 4):
        newNum = f"0{newNum}"

    return newNum
        

num = input("Enter a four-digit integer: ")
numCopy = createFourDigitNumber(num)

changedNums = [num]

count = 0
while(numCopy != 6174):
    acending = [int(x) for x in list(createFourDigitNumber(str(numCopy)))]
    acending.sort()
    acending = int("".join([str(x) for x in acending]))

    decending = [int(x) for x in list(createFourDigitNumber(str(numCopy)))]
    decending.sort(reverse=True)
    decending = int("".join([str(x) for x in decending]))

    if(acending > decending):
        numCopy = acending - decending
    elif(decending > acending):
        numCopy = decending - acending
    else:
        print(f"{num} > 0")
        print(f"{num} reaches 0 via Kaprekar's routine in 1 iterations")
        exit(0)

    changedNums.append(numCopy)

    count += 1

print(" > ".join([str(x) for x in changedNums]))
print(f"{num} reaches 6174 via Kaprekar's routine in {count} iterations")