const { group, groupEnd } = require('console')
const fs = require('fs')

class Group {
    constructor(rucksacks) {
        this.rucksacks = rucksacks.map((rucksack) => rucksack.split(""))
    }

    getCommonValue() {
        const [firstRucksack, secondRucksack, thirdRucksack] = this.rucksacks

        const commonValue = firstRucksack.filter((item) => {
            if(secondRucksack.includes(item) && thirdRucksack.includes(item)) {
                return item
            }
        })

        return commonValue[0]
    }

    getPriority() {
        let priority
        const commonValue = this.getCommonValue()

        commonValue.toUpperCase() === commonValue ? priority = commonValue.charCodeAt(0) - 38 : priority = commonValue.charCodeAt(0) - 96

        return priority
    }
}


const fileData = fs.readFileSync("./input.txt").toString().split("\n")

const groups = []

let i = 0
while(i < fileData.length) {
    groups.push(new Group([fileData[i], fileData[i + 1], fileData[i + 2]]))

    i += 3
}

groupPriorities = groups.map((group) => group.getPriority())

sumGroupPriorities = groupPriorities.reduce((accr, curr) => accr += curr)

console.log(`The sum of the priorities of the badges of each three-elf group is ${sumGroupPriorities}`)