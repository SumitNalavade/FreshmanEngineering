import random

# Abstract class Hazard
class Hazard:
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

# Class BottomlessPit extends Hazard
class BottomlessPit(Hazard):
    def __init__(self) -> None:
        super().__init__()
        pass

    def engage(self, currentPlayer):
        print("You fell into a bottomless pit! Game over!")
        currentPlayer.die()

# Class Superbat extends Hazard
class Superbat(Hazard):
    def __init__(self) -> None:
        super().__init__()
        pass

    def engage(self, currentPlayer):
        originalRoom = currentPlayer.currentRoom

        newRoom = currentPlayer.currentRoom

        while(newRoom == currentPlayer.currentRoom):
            newRoom = random.randint(1,20)

        currentPlayer.currentRoom = newRoom

        print(f"You entered a room with a superbat! It carried you into room {currentPlayer.currentRoom}")

        for hazard in ROOM_MAP[originalRoom].hazards:
            if(isinstance(hazard, Superbat)):
                ROOM_MAP[originalRoom].hazards.remove(hazard)
                break
        
        ROOM_MAP[currentPlayer.currentRoom].hazards = ROOM_MAP[currentPlayer.currentRoom].hazards.append(Superbat())

# Class Superbat extends Wumpus
class Wumpus(Hazard):
    def __init__(self) -> None:
        super().__init__()
        pass

class Room:
    connectedRooms = []
    hazards = []

    def __init__(self, connectedRooms) -> None:
        self.connectedRooms = connectedRooms

class Player:
    currentRoom = random.randrange(1,20)

    def __init__(self) -> None:
        pass

    def move(self, newRoom):
        self.currentRoom = newRoom

    def shoot(self):
        print("Shooting")

    def die(self):
        print("You died! Game Over!")
        exit(0)

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
    # Assign hazards to random rooms
    hazardousRooms = random.sample(range(1,21), 5)
    ROOM_MAP[hazardousRooms[0]].hazards = [BottomlessPit()]
    ROOM_MAP[hazardousRooms[1]].hazards = [BottomlessPit()]
    ROOM_MAP[hazardousRooms[2]].hazards = [Superbat()]
    ROOM_MAP[hazardousRooms[3]].hazards = [Superbat()]
    ROOM_MAP[hazardousRooms[4]].hazards = [Wumpus()]

    currentPlayer = Player()

    print("Hunt the Wumpus! \n")
    while(True):
        for hazard in ROOM_MAP[currentPlayer.currentRoom].hazards:
            hazard.engage(currentPlayer)

        currentRoom = currentPlayer.currentRoom

        print(f"\nYou are in room {currentRoom}")
        print(f'Tunnels lead to rooms {", ".join([str(x) for x in ROOM_MAP[currentRoom].connectedRooms])} \n')

        for connectedRoom in ROOM_MAP[currentRoom].connectedRooms:
            for hazard in ROOM_MAP[connectedRoom].hazards:
                hazard.warn(hazard)

        print("\n(1) Move\n(2) Shoot")
        move = input("")

        if(move == "1"):
            newRoom = int(input("\nWhere to? "))
            
            while((newRoom) not in ROOM_MAP[currentRoom].connectedRooms):
                newRoom = int(input(f"It is not possible to move to room {newRoom}\nPlease enter a valid room: "))

            currentPlayer.move(newRoom)
        elif(move == "2"):
            currentPlayer.shoot()