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
        this.totalScore = this.getRoundPoints()
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
