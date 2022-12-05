const fs = require("fs")

/*
X : Loose
Y: Draw
Z: Win
*/

/*
Opponent:
A: Rock
B: Paper
C: Scissors

Player:
X: Rock
Y: Paper
Z: Scissors

Scoring:
Rock: 1
Paper: 2
Scissors: 3

Loss: 0
Draw: 3
Win: 6
*/

class Round {
    constructor(movesArr) {
        this.movesArr = movesArr
        this.determinePlayerMove()
        this.getRoundPoints()
    }

    determinePlayerMove() {
        let playerMove = ""
        const [opponentMove, outcome] = this.movesArr
        
        switch (outcome) {
            case "X": //Loose
                if(opponentMove === "A") {
                    playerMove = "Z"
                } else if (opponentMove == "B") {
                    playerMove = "X"
                } else if (opponentMove == "C") {
                    playerMove = "Y"
                }
                this.movesArr = [opponentMove, playerMove]
                return
            case "Y": // Draw
                if(opponentMove == "A") {
                    playerMove = "X"
                } else if(opponentMove == "B") {
                    playerMove = "Y"
                } else if(opponentMove == "C") {
                    playerMove = "Z"
                }
                this.movesArr = [opponentMove, playerMove]
                return
            case "Z": // Win
                if(opponentMove == "A") {
                    playerMove = "Y"
                } else if(opponentMove == "B") {
                    playerMove = "Z"
                } else if(opponentMove == "C") {
                    playerMove = "X"
                }
                this.movesArr = [opponentMove, playerMove]
                return
        }
    }

    getRoundPoints = () => {
        let roundPoints = 0
        
        const opponentMove = this.movesArr[0]
        const playerMove = this.movesArr[1]
    
        switch (playerMove) {
            case "X":
                roundPoints += 1
                if(opponentMove === "A") {
                    roundPoints += 3
                } else if(opponentMove == "B") {
                    roundPoints += 0
                } else if(opponentMove == "C") {
                    roundPoints += 6
                }
                return roundPoints
            case "Y":
                roundPoints += 2
                if(opponentMove === "A") {
                    roundPoints += 6
                } else if(opponentMove == "B") {
                    roundPoints += 3
                } else if(opponentMove == "C") {
                    roundPoints += 0
                }
                return roundPoints
            case "Z":
                roundPoints += 3
                if(opponentMove === "A") {
                    roundPoints += 0
                } else if(opponentMove == "B") {
                    roundPoints += 6
                } else if(opponentMove == "C") {
                    roundPoints += 3
                }
                return roundPoints
        }
    }

    getScore = () => {
        return this.getRoundPoints()
    }
}

const fileData = fs.readFileSync("./input.txt").toString()

const roundArr = fileData.split("\n").map((data) => new Round(data.split(" ")))

const totalScore = roundArr.reduce((accr, curr) => accr += curr.getScore(), 0)

console.log(`The players total score is ${totalScore}`)
