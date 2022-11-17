# By submitting this assignment, I agree to the following:
#   "Aggies do not lie, cheat, or steal, or tolerate those who do."
#   "I have not given or received any unauthorized aid on this assignment."
#
# Name:         Austin
#               Christopher
#               Reed
#               Eddy
# Section:      468
# Assignment:   12 - 17 plotting data
# Date:         November 15, 2022

import numpy
import matplotlib.pyplot as plt

readFile = open('WeatherDataCLL.csv', 'r')
days = []
temp_max = []   # -2 index
temp_min = []   # -1 index
rain = []
dates = []
for line in readFile:
    try:
        line = line.rstrip('\n')
        sngl_day = line.split(',')
        temp_min.append(int(sngl_day[-1]))
        temp_max.append(int(sngl_day[-2]))
        rain.append(float(sngl_day[2]))
        days.append(sngl_day)
    except ValueError:
        pass

# x for plot 1
day_num_plt1x = []
for i in range(len(days)):
    day_num_plt1x.append(i)

# y1 for plot 1, max temp
max_temp_plt1y = []
for day in days:
    max_temp_plt1y.append(day[-2])

# y2 for plot 1, wind speed average
avg_windspeed_plt1y = []
for day in days:
    avg_windspeed_plt1y.append(day[1])

left_axis = plt.subplot(2, 2, 1)
right_axis = left_axis.twinx()
plt.legend(loc='lower left')
left_axis.set_xlabel('date')
left_axis.plot(day_num_plt1x, max_temp_plt1y, 'r-', label='Max Temp')
left_axis.set_ylabel('Maximum Temperature, F')
right_axis.plot(day_num_plt1x, avg_windspeed_plt1y, 'b-', label='Avg Wind')
right_axis.set_ylabel('Average wind speed, mph')
plt.title('Maximum Temperature and Average Wind Speed')
plt.subplot(2, 2, 2)
plt.tight_layout()
plt.show()

print(f"day_num_plt1x: {day_num_plt1x}")