import numpy as np

KEY = np.array([
    ["T", "E", "X", "A", "S"],
    ["H", "B", "R", "P", "L"],
    ["Y", "K", "I", "Q", "Z"],
    ["V", "O", "C", "W", "D"],
    ["G", "F", "M", "U", "N"]
])
BINGOMAPPINGS = { "B":0, "I":1, "N":2, "G":3, "O":4 }

encryptedMessage = "B2N3O4O4I1O5B2I4G4O4B3G1B5O1"

encryptedMessageList = []

pointer = 0
try:
    for index in range(len(encryptedMessage)):
        encryptedMessageList.append([encryptedMessage[pointer + 1], BINGOMAPPINGS[encryptedMessage[pointer]]])
        pointer += 2
except IndexError:
    pass

for coordinateList in encryptedMessageList:
    row = int(coordinateList[0]) - 1
    col = int(coordinateList[1])

    print(KEY[row][col], end="")