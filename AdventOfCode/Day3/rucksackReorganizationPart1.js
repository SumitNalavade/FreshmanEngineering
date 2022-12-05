const fs = require('fs')

class Rucksack {
    constructor(str) {
        this.items = str.split("")
        this.firstHalf = this.items.slice(0, this.items.length/2)
        this.secondHalf = this.items.splice(this.items.length/2, this.items.length - 1)
    }

    getCommonValue() {
        const commonValue = this.firstHalf.filter((item) => {
            if(this.secondHalf.includes(item)) {
                return item
            }
        })[0]

        return commonValue
    }

    getPriority() {
        let priority
        const commonValue = this.getCommonValue()

        commonValue.toUpperCase() === commonValue ? priority = commonValue.charCodeAt(0) - 38 : priority = commonValue.charCodeAt(0) - 96

        return priority
    }
}

const fileData = fs.readFileSync("./input.txt").toString()
const roundArr = fileData.split("\n").map((data) => new Rucksack(data))

const priorities = roundArr.map((rucksack) => rucksack.getPriority())

const sumPriorities = priorities.reduce((accr, curr) => accr + curr)

console.log(`The sum of priorities of the item type that appears in both compartments of the rucksack is ${sumPriorities}`)