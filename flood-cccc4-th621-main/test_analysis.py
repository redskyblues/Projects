from floodsystem.analysis import polyfit, latest_gradient
import matplotlib.pyplot as plt
import matplotlib
import numpy as np
import datetime

def test_analysis():
    base = datetime.datetime.today()
    date_list = [base - datetime.timedelta(days=x) for x in range(7)]
    list_of_dates = matplotlib.dates.date2num(date_list)

    x = [0, -1, -2, -3, -4, -5, -6]
    #y = x**3 + 2x**2 + 3x + 4
    y = [4, 2, -2, -14, -40, -86, -158]

    func_coeff = polyfit(date_list, y, 3)[0].coefficients
    for i in range(len(func_coeff)):
        rounded = round(func_coeff[i], 2)
        func_coeff[i] = rounded

    true_coeff = [1.00, 2.00, 3.00, 4.00]
    for i in range(len(true_coeff)):
        assert func_coeff[i] == true_coeff[i]

    gradient = round(latest_gradient(date_list, y, 3), 2)

    assert gradient == 3.00

test_analysis()