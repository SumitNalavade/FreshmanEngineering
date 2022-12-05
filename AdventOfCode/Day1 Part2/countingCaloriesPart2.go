package main

import (
	"fmt"
	"io/ioutil"
	"strconv"
	"strings"
	"sort"
)

func getInput() []string {
	data, _ := ioutil.ReadFile("./input.txt")

	return strings.Split(string(data), "\n\n")
}

func getTotalElfCalories(elfCalories string) int {
	totalCalories := 0

	splitElfCalories := strings.Split(elfCalories, "\n")

	for _, calories := range(splitElfCalories) {
		intCalories, _ := strconv.Atoi(calories)
		totalCalories += intCalories
	}

	return totalCalories
}

func main() {
	sumCalories := 0
	var totalCalories []int

	for _, calories := range getInput() {
		totalCalories = append(totalCalories, getTotalElfCalories(calories))
	}

	sort.Ints(totalCalories)

	totalCaloriesLength := len(totalCalories)
	greatestCalories := [3]int{totalCalories[totalCaloriesLength - 1], totalCalories[totalCaloriesLength - 2], totalCalories[totalCaloriesLength - 3]}

	for _, calories := range greatestCalories {
		sumCalories += calories
	}
	
	fmt.Printf("The top tree elves with the most calrories have a total of %v calories", sumCalories)
}