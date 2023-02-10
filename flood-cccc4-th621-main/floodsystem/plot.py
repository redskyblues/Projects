import matplotlib.pyplot as plt
import numpy as np
import matplotlib
from datetime import datetime, timedelta

def plot_water_levels(station, dates, levels):

    high_level = []
    low_level = []

    #initialise typical high level and low level for plotting
    for i in range(len(levels)):
        high_level.append(station.typical_range[1])
        low_level.append(station.typical_range[0])

    #plot
    plt.plot(dates, levels, label = 'Water levels for the past 10 days')
    plt.plot(dates, high_level, label = 'Typical high level')
    plt.plot(dates, low_level, label = 'Typical low level')

    #add plot details
    plt.xlabel('Date')
    plt.ylabel('Water level/m')
    plt.xticks(rotation=90)
    plt.title(station.name)
    plt.tight_layout()
    plt.legend()

    plt.show()

def plot_water_level_with_fit(station, dates, levels, p):
    high_level = []
    low_level = []

    #turn the dates into a list of floats
    list_of_dates = matplotlib.dates.date2num(dates)

    #find coefficients of each terms
    p_coeff = np.polyfit(list_of_dates - list_of_dates[0], levels, p)

    #number of dates shifted to fit with the polynomial
    date_shift = list_of_dates[0]

    #convert coefficients into polynomial 
    poly = np.poly1d(p_coeff)

    #initialise typical high level and low level for plotting
    for i in range(len(levels)):
        high_level.append(station.typical_range[1])
        low_level.append(station.typical_range[0])

    #plot
    plt.plot(dates, levels, label = 'Water levels for the past 10 days')
    plt.plot(dates, high_level, label = 'Typical high level')
    plt.plot(dates, low_level, label = 'Typical low level')
    plt.plot(dates, poly(list_of_dates - date_shift), label = 'Polynomial for to the power of' + str(p))

    #add plot details
    plt.xlabel('Date')
    plt.ylabel('Water level/m')
    plt.xticks(rotation=90)
    plt.title(station.name)
    plt.tight_layout()
    plt.legend()

    plt.show()