from floodsystem.stationdata import build_station_list, update_water_levels
from floodsystem.flood import stations_highest_rel_level


def run():
    stations = build_station_list()
    update_water_levels(stations)
    N = 10

    highest = stations_highest_rel_level(stations, N)

    for i in highest:
        print("{} {}" .format(i.name, i.relative_water_level()))


if __name__ == "__main__":
    run()
