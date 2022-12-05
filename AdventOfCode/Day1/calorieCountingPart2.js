const fs = require("fs")

class Elf {
    constructor(caloriesArr) {
        this.caloriesArr = caloriesArr.map((calories) => Number(calories))
    }
    
    getTotalCalories() {
        return this.caloriesArr.reduce((accr, curr) => accr += curr, 0)
    }
}

const fileData = fs.readFileSync("./input.txt").toString()
    
const elfData = fileData.split("\n\n").map((elm) => new Elf(elm.split("\n")).getTotalCalories()).sort(function (a, b) {  return a - b;  });

const largestCalories = [elfData[elfData.length - 1], elfData[elfData.length - 2], elfData[elfData.length - 3]]

const totalCalories = largestCalories.reduce((accr, curr) => accr + curr, 0)

console.log(`The three elves with the largest number of calories have ${totalCalories} total calories`)