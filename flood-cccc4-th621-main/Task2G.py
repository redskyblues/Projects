from floodsystem.stationdata import build_station_list, update_water_levels
from floodsystem.datafetcher import fetch_measure_levels
from floodsystem.analysis import polyfit, latest_gradient
import datetime
import numpy as np

'''Use relative water level of the station to determine what risk the town is at
If it is larger than 2, the town is in severe risk
If it is between 1 and 2, and water level is rising, the town is in high risk
If it is between 1 and 2, and water level is dropping, the town is in moderate risk
If it is between 0.5 and 1, the town is in moderate risk
If it is below 0.5, the town is in low risk

The risk of flooding of a town is goverened by the station with the highest relative water level
For example,
If a town T has station A, B, C and D which has relative water level of 2.5, 1.5, 1.2 and 0.4
Then town T is in severe risk'''

def run():
    stations = build_station_list()
    update_water_levels(stations)

    #analyse water level of past 7 days
    dt = 7

    #initialise dictionary to put name of towns and risk level into
    town_risk = {
    }

    severe = []
    high = []
    moderate = []
    low = []

    station_added = 0

    for station in stations:
        if station.town not in town_risk:
            town_risk[station.town] = 'Data N/A'

    print (town_risk)

    for station in stations:
        dates, levels = fetch_measure_levels(station.measure_id, dt=datetime.timedelta(days=dt))
        if station.relative_water_level() == None:
            pass
        elif station.latest_level == None:
            pass
        else:
            if station.relative_water_level() > 2:
                town_risk[station.town] = 'Severe'
            elif station.relative_water_level() < 2 and station.relative_water_level() > 1:
                if type(latest_gradient(dates, levels, 4)) == float:
                    if latest_gradient(dates, levels, 4) > 0 and town_risk[station.town] != 'Severe':
                        town_risk[station.town] = 'High'
                    elif latest_gradient(dates, levels, 4) < 0 and town_risk[station.town] != 'Severe' and town_risk[station.town] != 'High':
                        town_risk[station.town] = 'Moderate'
            elif station.relative_water_level() < 1 and station.relative_water_level() > 0.5:
                if town_risk[station.town] != 'Severe' and town_risk[station.town] != 'High':
                        town_risk[station.town] = 'Moderate'
            elif station.relative_water_level() < 0.5 and town_risk[station.town] != 'Severe' and town_risk[station.town] != 'High' and town_risk[station.town] != 'Moderate':
                town_risk[station.town] = 'Low'
        
        station_added += 1
        percent_added = (station_added/len(stations))*100
        print (percent_added, '%', 'finished')
    
    #add town names to list of towns of corresponding risk
    for k, v in town_risk.items():
        if v == 'Severe':
            severe.append(k)
        elif v == 'High':
            high.append(k)
        elif v == 'Moderate':
            moderate.append(k)
        elif v == 'Low':
            low.append(k)

    print('The following towns have severe risk of flooding', severe)
    print('The following towns have high risk of flooding', high)
    print('The following towns have moderate risk of flooding', moderate)
    print('The following towns have low risk of flooding', low)

    return town_risk, severe, high, moderate, low
    
        
        
if __name__ == "__main__":
    run()