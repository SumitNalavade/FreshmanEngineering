package main

import (
	"fmt"
	"io/ioutil"
	"strconv"
	"strings"
	// "io/ioutil"
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
	var totalCalories []int

	for _, calories := range getInput() {
		totalCalories = append(totalCalories, getTotalElfCalories(calories))
	}

	maxValue := totalCalories[0]
	for _, calories := range totalCalories {
		if(calories > maxValue) {
			maxValue = calories
		}
	}

	fmt.Printf("The elf with the most calories has %v calories", maxValue)
}