# By submitting this assignment, I agree to the following:
# "Aggies do not lie, cheat, or steal, or tolerate those who do."
# "I have not given or received any unauthorized aid on this assignment."
#
# Name:         Sumit Nalavade
# Section:      524
# Assignment:   Lab 12.17
# Date:         17 November 2022

import csv
import matplotlib.pyplot as plt
import numpy as np

# Create a Weather Data class to organize better


class Weather():
    month = 0
    day = 0
    year = 0
    averageWindSpeed = 0
    precipitation = 0
    averageTemp = 0
    maxTemp = 0
    maxTemp = 0

    def __init__(self, date, averageWindSpeed, precipitation, averageTemp, maxTemp, minTemp) -> None:
        dateArr = date.split("/")
        self.month = int(dateArr[0])
        self.day = int(dateArr[1])
        self.year = int(dateArr[2])
        self.averageWindSpeed = float(averageWindSpeed)
        self.precipitation = float(precipitation)
        self.averageTemp = float(averageTemp)
        self.maxTemp = float(maxTemp)
        self.minTemp = float(minTemp)


weatherDataFile = open("WeatherDataCLL.csv", "r")
weatherDataList = [Weather(x[0], x[1], x[2], x[3], x[4], x[5])
                   for x in list(csv.reader(weatherDataFile, delimiter=","))[1:]]
weatherDataFile.close()

daysList = [x for x in range(len(weatherDataList))]

# Create a line graph of maximum temperatures and average wind speeds vs dates


def createLineGraph():
    maxTempList = [x.maxTemp for x in weatherDataList]
    avgWindSpeedList = [x.averageWindSpeed for x in weatherDataList]

    fig, ax = plt.subplots()
    ax.plot(daysList, maxTempList, color="red", label="Max Temp")

    ax2 = ax.twinx()
    ax2.plot(daysList, avgWindSpeedList, color="blue", label="Avg Wind")

    plt.title("Maximum Temperature and Average Wind Speed")
    ax.set_xlabel("Dates")
    ax.set_ylabel("Maximum Temperature (F)")
    ax2.set_ylabel("Average Wind Speed (MPH)")

    h1, l1 = ax.get_legend_handles_labels()
    h2, l2 = ax2.get_legend_handles_labels()
    plt.legend(h1+h2, l1+l2, loc=3)

    plt.show()

# Create a histogram of average wind speeds vs number of days


def createHistogram():
    avgWindSpeedList = [x.averageWindSpeed for x in weatherDataList]

    plt.hist(avgWindSpeedList, ec='black', bins=30, color="green")

    plt.title("Histogram of Average Wind Speed")
    plt.xlabel("Average Wind Speed (MPH)")
    plt.ylabel("Number of days")

    plt.show()

# Create a scatterplot of average wind speed vs minimum temperatures


def createScatterplot():
    minTempList = [x.minTemp for x in weatherDataList]
    avgWindSpeedList = [x.averageWindSpeed for x in weatherDataList]

    plt.scatter(minTempList, avgWindSpeedList, color="black", s=10)

    plt.title("Average Wind Speed vs Minimum Temperature")
    plt.xlabel("Minimum Temperature (F)")
    plt.ylabel("Average Wind Speed (MPH)")

    plt.show()

# Create a bar chart showing average temperatures for each month as well as the max and min temperatures for each month


def createBarChart():
    monthsList = [x for x in range(1, 13)]
    monthsAvgTempData = {1: 0, 2: 0, 3: 0, 4: 0, 5: 0,
                         6: 0, 7: 0, 8: 0, 9: 0, 10: 0, 11: 0, 12: 0}
    monthsLowTemp = {1: 1000, 2: 1000, 3: 1000, 4: 1000, 5: 1000,
                     6: 1000, 7: 1000, 8: 1000, 9: 1000, 10: 1000, 11: 1000, 12: 1000}
    monthsHighTemp = {1: -1000, 2: -1000, 3: -1000, 4: -1000, 5: -1000,
                      6: -1000, 7: -1000, 8: -1000, 9: -1000, 10: -1000, 11: -1000, 12: -1000}

    for i in weatherDataList:
        monthsAvgTempData[i.month] += i.averageTemp

        if(monthsLowTemp[i.month] > i.minTemp):
            monthsLowTemp[i.month] = i.minTemp

        if(monthsHighTemp[i.month] < i.maxTemp):
            monthsHighTemp[i.month] = i.maxTemp

    for i in monthsAvgTempData:
        numPoints = len([x for x in weatherDataList if x.month == i])

        monthsAvgTempData[i] /= numPoints

    plt.bar(monthsList, list(monthsAvgTempData.values()), color="green")

    plt.plot(monthsList, list(monthsLowTemp.values()),
             color="blue", label="Low T")
    plt.plot(monthsList, list(monthsHighTemp.values()),
             color="red", label="High T")

    plt.title("Temperature by month")
    plt.xlabel("Month")
    plt.ylabel("Average Temperature (F)")
    plt.legend(loc="upper left")

    plt.show()


createLineGraph()
createHistogram()
createScatterplot()
createBarChart()
