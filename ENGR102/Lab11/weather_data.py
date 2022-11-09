# By submitting this assignment, I agree to the following:
# "Aggies do not lie, cheat, or steal, or tolerate those who do."
# "I have not given or received any unauthorized aid on this assignment."
#
# Name:         Sumit Nalavade
# Section:      524
# Assignment:   Lab 11.13
# Date:         9 November 2022

monthsDict = { "January": 1, "February": 2, "March": 3, "April": 4, "May": 5, "June": 6, "July": 7, "August": 8, "September": 9, "October": 10, "November": 11, "December": 12 }

# Class to create a weather object with the following properties
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

weatherDataObjArr = []

weatherDataFile = open("WeatherDataCLL.csv", "r")
for rawWeatherData in list(weatherDataFile)[1:]:
    weatherDataArr = rawWeatherData.split(",")

    weatherData = Weather(weatherDataArr[0], weatherDataArr[1], weatherDataArr[2], weatherDataArr[3], weatherDataArr[4], weatherDataArr[5])
    weatherDataObjArr.append(weatherData)

def getMaxTemp():
    maxTemp = 0
    for weatherDataObj in weatherDataObjArr:
        temp = weatherDataObj.maxTemp
        if(temp > maxTemp):
            maxTemp = temp

    return maxTemp

def getMinTemp():
    minTemp = weatherDataObjArr[0].minTemp
    
    for weatherDataObj in weatherDataObjArr:
            temp = weatherDataObj.minTemp
            if(temp < minTemp):
                minTemp = temp

    return minTemp

def getAveragePrecipitation():
    totalPrecipitation = 0
    for weatherDataObj in weatherDataObjArr:
        totalPrecipitation += weatherDataObj.precipitation
    
    return totalPrecipitation / len(weatherDataObjArr)

def getMeanMaximumDailyTemperature(monthString, year):
    month = monthsDict[monthString]

    totalMaxDailyTemp = 0
    count = 0

    for weatherDataObj in weatherDataObjArr:
        if(weatherDataObj.month == month and weatherDataObj.year == year):
            count += 1
            totalMaxDailyTemp += weatherDataObj.maxTemp
    
    return round((totalMaxDailyTemp/count), 1)

def getMeanDailyWindSpeed(monthString, year):
    month = monthsDict[monthString]

    totalDailyWindSpeed = 0
    count = 0

    for weatherDataObj in weatherDataObjArr:
        if(weatherDataObj.month == month and weatherDataObj.year == year):
            count += 1
            totalDailyWindSpeed += weatherDataObj.averageWindSpeed
    
    return round((totalDailyWindSpeed/count), 2)

def getPercentageOfDaysWithPrecipitation(monthString, year):
    month = monthsDict[monthString]
    
    countTotalDays = 0
    countDaysWithPrecipitation = 0

    for weatherDataObj in weatherDataObjArr:
        if(weatherDataObj.month == month and weatherDataObj.year == year):
           countTotalDays += 1
           if(weatherDataObj.precipitation > 0):
            countDaysWithPrecipitation += 1

    return (countDaysWithPrecipitation/countTotalDays) * 100
    


print(f"3-year maximum temperature: {int(getMaxTemp())} F")
print(f"3-year minimum temperature: {int(getMinTemp())} F")
print(f"3-year average precipitation: {getAveragePrecipitation():.3f} inches")

month = input("Please enter a month: ")
year = int(input("Please enter a year: "))

print(f"For {month} {year}:")
print(f"Mean maximum daily temperature: {getMeanMaximumDailyTemperature(month, year):.1f} F")
print(f"Mean daily wind speed: {getMeanDailyWindSpeed(month, year):.2f} mph")
print(f"Percentage of days with precipitation: {getPercentageOfDaysWithPrecipitation(month, year):.1f}%")