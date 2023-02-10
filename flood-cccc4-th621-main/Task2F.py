from floodsystem.stationdata import build_station_list, update_water_levels
from floodsystem.datafetcher import fetch_measure_levels
from floodsystem.plot import plot_water_levels, plot_water_level_with_fit
import datetime

def run():
    stations = build_station_list()
    update_water_levels(stations)
    latest_water_level = []

    #add tuple of station and latest water level of that station to latest_water_level
    for station in stations:
        if type(station.relative_water_level()) == float:
            latest_water_level.append([station, station.relative_water_level()])
    
    #sort sorted_watre_level by ascending relative_water_level
    sorted_water_level = sorted(latest_water_level, reverse=True, key=lambda level: level[1])

    #two days
    dt = 2

    #plot water levels for 5 stations at which the current relative level is greatest
    for i in range(5):
        dates, levels = fetch_measure_levels(sorted_water_level[i][0].measure_id, dt=datetime.timedelta(days=dt))      
        plot_water_level_with_fit(sorted_water_level[i][0], dates, levels, 4)

if __name__ == "__main__":
    run()
