# By submitting this assignment, I agree to the following:
#   "Aggies do not lie, cheat, or steal, or tolerate those who do."
#   "I have not given or received any unauthorized aid on this assignment."
#
# Names:        Surya Jasper, Sumit Nalavade, Srikar Velavarthipati, Ronit Dhawan
# Section:      524
# Assignment:   8.10
# Date:         24 10 2022

# Create an initial array to hold the ascii art for all of the numbers we can print
nums = [
    ['000', ' 1 ', '222', '333', '4 4', '555', '666', '777', '888', '999', ' '],
    ['0 0', '11 ', '  2', '  3', '4 4', '5  ', '6  ', '  7', '8 8', '9 9', ':'],
    ['0 0', ' 1 ', '222', '333', '444', '555', '666', '  7', '888', '999', ' '],
    ['0 0', ' 1 ', '2  ', '  3', '  4', '  5', '6 6', '  7', '8 8', '  9', ':'],
    ['000', '111', '222', '333', '  4', '555', '666', '  7', '888', '999', ' ']
]

# Initialize a variable to hold what we're going to print out at the end
finalTime = ""

inputTimeArr = list(input("Enter the time: \n"))

# Convert the inputted numbers to valid values to index the nums array
for index, i in enumerate(inputTimeArr):
    if(i == ":"):
        inputTimeArr[index] = 10
        continue

    inputTimeArr[index] = int(float(i))

# Iterate 5 times and add the specific ascii art from the nums array to the finalTime string
for index, i in enumerate(nums):
    for num in inputTimeArr:
        finalTime += nums[index][num] + " "
    if(index != 4):
        finalTime += "\n"

# Print out the final ascii art
print(finalTime)
