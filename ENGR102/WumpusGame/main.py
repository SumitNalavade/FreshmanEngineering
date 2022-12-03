# By submitting this assignment, I agree to the following:
#   "Aggies do not lie, cheat, or steal, or tolerate those who do."
#   "I have not given or received any unauthorized aid on this assignment."
#
# Name:         Surya Jasper, Sumit Nalavade, Ronit Dhawan, Srikar Velavarthipati
# Section:      524
# Assignment:   Hunt The Wumpus Game
# Date:         2 December 2022

import random

# import the playsound package for added sound effects
try:
    from playsound import playsound
except:
    pass

def sound(type):
    '''
        Take in a type of hazard (Wumpus, BottomlessPit or Superbat) and use the play sound library to play a sound effect when the player is in a neighboring room with a monster
    '''
    try:
        if(isinstance(type, Wumpus)):
            playsound("./wumpus.mp3")
        elif(isinstance(type, BottomlessPit)):
            playsound("./wind.mp3")
        elif(isinstance(type, Superbat)):
            playsound("./bat.mp3")
    except:
        pass

# Abstract class Hazard
class Hazard:
    '''
        The hazard class is the parent class of all hazards that defines the warn method which warns players when a neighboring room contains a hazard and
        the engage method which is overrided Hazard subclasses 
    '''
    def __init__(self) -> None:
        pass

    def engage(self, currentPlayer):
        pass

    def warn(self, type):
        if(isinstance(type, Wumpus)):
            print("I smell a Wumpus!")
        elif(isinstance(type, BottomlessPit)):
            print("I feel a draft!")
        elif(isinstance(type, Superbat)):
            print("Bats nearby!")

        sound(type)
        
# Class BottomlessPit extends Hazard
class BottomlessPit(Hazard):
    '''
        The BottomlessPit class inherits and extends the Hazard class by overriding the engage method to notify that when called takes in the current use as an argument
        and notifies the user that they fell into a bottomless pit, and class the die method on the current user
    '''
    def __init__(self) -> None:
        super().__init__()
        pass

    def engage(self, currentPlayer):
        print("You fell into a bottomless pit! Game over!")
        currentPlayer.die()

# Class Superbat extends Hazard
class Superbat(Hazard):
    '''
        The Superbat class inherits and extends the Hazard class by overriding the engage method that when called takes in the current player, and changes their
        current room to a random room. The superbat also moves to that room when it drops the player
    '''
    def __init__(self) -> None:
        super().__init__()
        pass

    def engage(self, currentPlayer):
        originalRoom = currentPlayer.currentRoom

        newRoom = currentPlayer.currentRoom

        # Select a random room
        while(newRoom == currentPlayer.currentRoom):
            newRoom = random.randint(1,20)

        # Change the player's room
        currentPlayer.currentRoom = newRoom

        print(f"You entered a room with a superbat! It carried you into room {currentPlayer.currentRoom}")

        # Change the location of the superbat itself as well
        for hazard in ROOM_MAP[originalRoom].hazards:
            if(isinstance(hazard, Superbat)):
                ROOM_MAP[originalRoom].hazards.remove(hazard)
        
        ROOM_MAP[currentPlayer.currentRoom].hazards = ROOM_MAP[currentPlayer.currentRoom].hazards = [Superbat()]

# Class Superbat extends Hazard
class Wumpus(Hazard):
    '''
        The Wumpus class inherits and extends the Hazard class by overriding the engage method that when called takes in the current player,
        and decides weather to call the die method on the current player and end the game, or move to a neighborning room
    '''
    def __init__(self) -> None:
        super().__init__()
        pass
        
    def engage(self, currentPlayer):        
        randomChance = random.randint(1,100)

        # 75% chance the Wumpus simply moves to a neighboring room and does nothing to the player
        if(randomChance <= 75):
            print("You entered the room with the Wumpus! Luckily it chose to move to a neighboring room")

            # Remove the Wumpus object from the current room
            for hazard in ROOM_MAP[currentPlayer.currentRoom].hazards:
                if(isinstance(hazard, Wumpus)):
                    ROOM_MAP[currentPlayer.currentRoom].hazards.remove(hazard)

            # Place the Wumpus in a random neighboring room
            newRoomIndex = ROOM_MAP[currentPlayer.currentRoom].connectedRooms[random.randint(0,2)]
            ROOM_MAP[newRoomIndex].hazards = [Wumpus()]
        else:
            print("The Wumpus woke up and ate you!")
            currentPlayer.die()

class Room:
    '''
        The room class allows us to keep track of the connecting rooms as well as the hazards in each room 
    '''
    connectedRooms = []
    hazards = []

    def __init__(self, connectedRooms) -> None:
        self.connectedRooms = connectedRooms

class Player:
    '''
        The player class represents the user who is playing the game and defines several properties critial to the game play including keeping track of the amount of
        arrows, the current room of the player and defines several methods such as move, shoot, win and die
    '''
    numArrows = 5
    currentRoom = 1

    def __init__(self) -> None:
        pass

    # Move method takes in the index of a new room and changes the value of the current room to the new room
    def move(self, newRoom):
        self.currentRoom = newRoom

    def shoot(self, roomsToShootThrough):
        '''
            The shoot method takes in an array of room indexes for an arrow to travel through and determines if the arrow path is valid.
            For the arrow path to be valid, the rooms must all be connected.
            If the arrow path is invalid, generate a random path for the arrow.
            If the arrow enters a room with the Wumpus, call the win method and end the game.
            If the arrow enters a room with the player, call the die method and end the game. 
        '''
        self.numArrows -= 1

        arrowValid = True

        # Determine if the arrow path is valid by checking to see if the all the rooms that the arrow is supposed to travel through is valid
        for roomIndex in range(0, len(roomsToShootThrough) - 1):
            nextRoom = roomsToShootThrough[roomIndex + 1]

            if(nextRoom not in ROOM_MAP[roomsToShootThrough[roomIndex]].connectedRooms):
                arrowValid = False

        # If the arrow path is valid, send the arrow through each of the rooms checking to see if it enter a room with the Wumpus or the player
        if(arrowValid == True):
            for roomIndex in roomsToShootThrough[1:]:
                print(f"Arrow going through room {roomIndex}")
                for hazard in ROOM_MAP[roomIndex].hazards:
                    if(isinstance(hazard, Wumpus)):
                        self.win()
                    elif(isinstance(hazard, Player)):
                        self.die()
        # If the arrow path is invalid, generate a random arrow path
        else:
            print("\nInvalid Arrow Path!")
            print("Generating random arrow path...")
            randomPath = []

            currentRoom = self.currentRoom 
            for i in roomsToShootThrough:
                # Generate a random arrow path
                randomRoomIndex = random.randint(0,2)

                newRoomIndex = ROOM_MAP[currentRoom].connectedRooms[randomRoomIndex]
                currentRoom = newRoomIndex

                randomPath.append(currentRoom)
            
            for roomIndex in randomPath[1:]:
                print(f"Arrow going through room {roomIndex}")
                for hazard in ROOM_MAP[roomIndex].hazards:
                    if(isinstance(hazard, Wumpus)):
                        self.win()
                    elif(isinstance(hazard, Player)):
                        self.die()

        # Check if the number of arrows is equal to 0. If so, the player can no longer kill the wumpus and the game ends
        if(self.numArrows == 0):
            print("You ran out of arrows!")
            print("Game Over!")
            exit(0)

    def die(self):
        print("You died! Game Over!")
        exit(0)

    # If the player wins, print a message to the user and play some victory music
    def win(self):
        print("You shot the Wumpus! Game Over!")
        try:
            playsound("./victoryRoyale.mp3")
            playsound("./defaultDance.mp3")
        except:
            pass
        exit(0)

# Create a dictionary object to hold all of the rooms for the game
ROOM_MAP = {
    1: Room(connectedRooms=[2,5,8]),
    2: Room(connectedRooms=[1,3,10]),
    3: Room(connectedRooms=[2,4,12]),
    4: Room(connectedRooms=[3,5,14]),
    5: Room(connectedRooms=[1,4,6]),
    6: Room(connectedRooms=(5,7,15)),
    7: Room(connectedRooms=[6,8,17]),
    8: Room(connectedRooms=[1,7,9]),
    9: Room(connectedRooms=[8,10,18]),
    10: Room(connectedRooms=[2,9,11]),
    11: Room(connectedRooms=[10,12,19]),
    12: Room(connectedRooms=[11,3,13]),
    13: Room(connectedRooms=[12,14,20]),
    14: Room(connectedRooms=[4,13,15]),
    15: Room(connectedRooms=[6,14,16]),
    16: Room(connectedRooms=[15,17,20]),
    17: Room(connectedRooms=[7,16,18]),
    18: Room(connectedRooms=[19,17,9]),
    19: Room(connectedRooms=[18,20,11]),
    20: Room(connectedRooms=[16,19,13])
}

if __name__ == "__main__":
    # Play some background music
    try:
        playsound("./background.mp3", False)
    except:
        pass

    # Assign hazards to random rooms
    hazardousRooms = random.sample(range(2,21), 5)
    ROOM_MAP[hazardousRooms[0]].hazards = [BottomlessPit()]
    ROOM_MAP[hazardousRooms[1]].hazards = [BottomlessPit()]
    ROOM_MAP[hazardousRooms[2]].hazards = [Superbat()]
    ROOM_MAP[hazardousRooms[3]].hazards = [Superbat()]
    ROOM_MAP[hazardousRooms[4]].hazards = [Wumpus()]

    currentPlayer = Player()

    print("Hunt the Wumpus!\n")
    print("Please make sure to install the playsound package and turn up your volume for added effects!")
    while(True):

        # For each turn, check and see if the current player is in a room with a hazard. If so, call the engage method on the hazard
        for hazard in ROOM_MAP[currentPlayer.currentRoom].hazards:
            hazard.engage(currentPlayer)

        currentRoom = currentPlayer.currentRoom

        # Inform the player of the room they're currently in, number of arrows remaining and the neighboring rooms
        print(f"\nYou are in room {currentRoom}")
        print(f"You have {currentPlayer.numArrows} arrows remaining")
        print(f'Tunnels lead to rooms {", ".join([str(x) for x in ROOM_MAP[currentRoom].connectedRooms])} \n')

        # Check and see if any of the neighboring rooms have a hazard inside them. If so, call the warn method on the hazard
        for connectedRoom in ROOM_MAP[currentRoom].connectedRooms:
            for hazard in ROOM_MAP[connectedRoom].hazards:
                hazard.warn(hazard)

        # Ask the user weather they want to move or shoot
        print("\n(1) Move\n(2) Shoot")
        move = input("")

        # If the user enters a 1, ask them which room they want to move to.
        # Check to see if that room is a neighboring room and if so, switch the current room variable on the current player object
        if(move == "1"):
            try:
                newRoom = int(input("\nWhere to? "))
            
                while((newRoom) not in ROOM_MAP[currentRoom].connectedRooms):
                    newRoom = int(input(f"It is not possible to move to room {newRoom}\nPlease enter a valid room: "))

                currentPlayer.move(newRoom)
            except:
                print("Invalid Input!")
        # If the user enters a 2, ask the user how many rooms they want to shoot through as well as the path of the rooms and call the shoot method on the current user
        elif(move == "2"):
            roomsToShootThrough = [currentRoom]

            try:
                numRooms = int(input("\nShoot through how many rooms (1-5)? "))

                if(numRooms < 1 or numRooms > 5):
                    raise Exception("Invalid input!")

                for i in range(1, numRooms + 1):
                    roomsToShootThrough.append(int(input(f"Room #{i} of path: ")))
            except:
                print("Invalid Input!")

            currentPlayer.shoot(roomsToShootThrough)

        else:
            print("Invaid input.")