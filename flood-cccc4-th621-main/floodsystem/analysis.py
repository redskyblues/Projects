import matplotlib.pyplot as plt
import matplotlib
import numpy as np
from datetime import datetime, timedelta

def polyfit(dates, levels, p):
    #turn the dates into a list of floats
    list_of_dates = matplotlib.dates.date2num(dates)

    #find coefficients of each terms
    p_coeff = np.polyfit(list_of_dates - list_of_dates[0], levels, p)

    #convert coefficients into polynomial    
    result = [np.poly1d(p_coeff), list_of_dates[0]]

    return result

def latest_gradient(dates, levels, p):
    #turn the dates into a list of floats
    list_of_dates = matplotlib.dates.date2num(dates)

    #Eliminate IndexError: index 0 is out of bounds
    if len(list_of_dates) == 0:
        latest_trend = 'Unavailable'

    #find coefficients of each terms
    else:
        p_coeff = np.polyfit(list_of_dates - list_of_dates[0], levels, p)

        gradient_func = np.polyder(np.poly1d(p_coeff))

        latest_trend = gradient_func(0)

    return latest_trend