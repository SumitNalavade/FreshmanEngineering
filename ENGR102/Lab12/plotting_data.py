import csv
import matplotlib.pyplot as plt
import numpy as np

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
weatherDataList = [Weather(x[0], x[1], x[2], x[3], x[4], x[5]) for x in list(csv.reader(weatherDataFile, delimiter=","))[1:]]
weatherDataFile.close()

daysList = [x for x in range(len(weatherDataList))]

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

def createHistogram():
    avgWindSpeedList = [x.averageWindSpeed for x in weatherDataList]

    plt.hist(avgWindSpeedList, ec='black', bins=30, color="green")
    
    plt.title("Histogram of Average Wind Speed")
    plt.xlabel("Average Wind Speed (MPH)")
    plt.ylabel("Number of days")

    plt.show()

def createScatterplot():
    minTempList = [x.minTemp for x in weatherDataList]
    avgWindSpeedList = [x.averageWindSpeed for x in weatherDataList]

    plt.scatter(minTempList, avgWindSpeedList, color="black", s=10)

    plt.title("Average Wind Speed vs Minimum Temperature")
    plt.xlabel("Minimum Temperature (F)")
    plt.ylabel("Average Wind Speed (MPH)")

    plt.show()

createScatterplot()