const fs = require("fs")

class Elf {
    constructor(caloriesArr) {
        this.caloriesArr = caloriesArr.map((calories) => Number(calories))
    }
    
    getTotalCalories() {
        return this.caloriesArr.reduce((accr, curr) => {
            return accr += curr
        }, 0)
    }
}

const fileData = fs.readFileSync("./input.txt").toString()
    
elfData = fileData.split("\n\n").map((elm) => new Elf(elm.split("\n")))

maxCalories = elfData[0].getTotalCalories()

elfData.forEach(elf => {
    if(elf.getTotalCalories() > maxCalories) {
        maxCalories = elf.getTotalCalories()
    }
});

console.log(maxCalories)