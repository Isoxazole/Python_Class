"""
Homework 10, Exercise 1
William Morris
5/04/19
This program reads data from a csv file and creates 3 subplots on one sheet.
The data shows the temperature, precipitation, and snowfall for colorado springs.

"""

import csv
from datetime import datetime
import re

from matplotlib import pyplot as plt

filename = 'history_export_colorado_springs_2018_2.csv'
with open(filename) as f:
    reader = csv.reader(f)
    header_row = next(reader)

    dates, avgTemps, totalPrecips, totalSnowFalls, maxTemps, minTemps = [], [], [], [], [], []

    # Read in the data to variables
    for row in reader:
        if re.search('[a-zA-Z]', "".join(row)) or len(set(row)) == 1:
            continue
        try:
            year = int(row[0])
            month = int(row[1])
            day = int(row[2])
            hour = int(row[3])
            minute = int(row[4])
            avgTemp = float(row[5])
            totalPrecip = float(row[6])
            totalSnowFall = float(row[7])
            maxTemp = float(row[8])
            minTemp = float(row[9])
            current_date = datetime(year, month, day, hour, minute)

        except Exception:
            print("error")
        else:
            # append the data read in to lists
            dates.append(current_date)
            avgTemps.append(avgTemp)
            totalPrecips.append(totalPrecip)
            totalSnowFalls.append(totalSnowFall)
            maxTemps.append(maxTemp)
            minTemps.append(minTemp)

# plot data for the temperatures.
plt.subplot(3, 1, 1)
plt.plot(dates, maxTemps, c='red', alpha=0.5, label='Max Temp')
plt.plot(dates, minTemps, c='blue', alpha=0.5, label='Min Temp')
plt.plot(dates, avgTemps, c='green', alpha=0.5, label='Avg Temp')
plt.fill_between(dates, maxTemps, minTemps, facecolor='blue', alpha=0.1)

# Format plot.
title = "Colorado Springs History Report 2018"
plt.title(title)
plt.ylabel("Temperature (F)" )
plt.tick_params(axis='both', which='major')
# Get rid of bottom tick marks
plt.tick_params(axis='x', which='both', bottom=False, top=False, labelbottom=False)
plt.legend()

# plot the precipitation amount
plt.subplot(3, 1, 2)
plt.plot(dates, totalPrecips, c='blue', label='Precipitation')
plt.ylabel("mm")
plt.tick_params(axis='x', which='both', bottom=False, top=False, labelbottom=False)
plt.legend()

# plot the snowfall amount
plt.subplot(3, 1, 3)
plt.plot(dates, totalSnowFalls, c='blue', label='Snowfall')
plt.ylabel("cm")

plt.legend()
plt.show()