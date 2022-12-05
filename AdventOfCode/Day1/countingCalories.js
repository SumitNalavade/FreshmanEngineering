const fs = require("fs")

const getInput = () => {
    const data = fs.readFileSync("./input.txt").toString()

    return data.split("\n\n")
}

const getTotalElfCalories = (elfCalories) => {
    const totalElfCalories = elfCalories.split("\n").reduce((accr, curr) => accr += Number(curr), 0)
    
    return totalElfCalories
}

data = getInput().map((input) => getTotalElfCalories(input))

maxValue = data[0]
data.forEach((elm) => {
    if(elm > maxValue) {
        maxValue = elm
    }
})

console.log(maxValue)