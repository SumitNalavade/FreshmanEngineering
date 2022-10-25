# By submitting this assignment, I agree to the following:
#   "Aggies do not lie, cheat, or steal, or tolerate those who do."
#   "I have not given or received any unauthorized aid on this assignment."
#
# Names:        Surya Jasper, Sumit Nalavade, Srikar Velavarthipati, Ronit Dhawan
# Section:      524
# Assignment:   Lab 8 Ascii Clock
# Date:         24 10 2022

CHARS_TO_ASCII = {
  "1": [
    " 1 ",
    "11 ",
    " 1 ",
    " 1 ",
    "111",
  ],
  "2": [
    "222",
    "  2",
    "222",
    "2  ",
    "222",
  ],
  "3": [
    "333",
    "  3",
    "333",
    "  3",
    "333",
  ],
  "4": [
    "4 4",
    "4 4",
    "444",
    "  4",
    "  4",
  ],
  "5": [
    "555",
    "5  ",
    "555",
    "  5",
    "555",
  ],
  "6": [
    "666",
    "6  ",
    "666",
    "6 6",
    "666",
  ],
  "7": [
    "777",
    "  7",
    "  7",
    "  7",
    "  7",
  ],
  "8": [
    "888",
    "8 8",
    "888",
    "8 8",
    "888",
  ],
  "9": [
    "999",
    "9 9",
    "999",
    "  9",
    "  9",
  ],
  "0": [
    "000",
    "0 0",
    "0 0",
    "0 0",
    "000",
  ],
  ":": [
    " ",
    ":",
    " ",
    ":",
    " ",
  ],
}

def print_time_as_ascii(time):
  for i in range(5):
    for char in time:
      print(CHARS_TO_ASCII[char][i], end=" ")
    print()

time_str = input("Enter the time: ")
print()
print_time_as_ascii(time_str)